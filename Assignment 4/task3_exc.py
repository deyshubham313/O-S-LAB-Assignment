# Parent writes lines to a pipe, child execs 'grep' to filter "ok"
# Demonstrates: fork + pipe + dup2 + execvp

import os
import sys
import time

def run_exec_pipe():
    # Create pipe
    r, w = os.pipe()
    pid = os.fork()

    if pid == 0:
        # ----------------- CHILD PROCESS -----------------
        # Close write-end in child
        os.close(w)

        # Replace child's STDIN with the read-end of the pipe
        os.dup2(r, 0)

        # Close original file descriptor after duplicating
        os.close(r)

        # Execute: grep "ok"
        os.execvp("grep", ["grep", "ok"])

        # If exec fails:
        print("Exec failed!", file=sys.stderr)
        sys.exit(1)

    else:
        # ----------------- PARENT PROCESS -----------------
        os.close(r)  # Parent does not read

        wfd = os.fdopen(w, 'w')

        lines = [
            "this is ok\n",
            "this is not\n",
            "ok indeed\n"
        ]

        for line in lines:
            wfd.write(line)
            wfd.flush()
            time.sleep(0.2)

        wfd.close()

        pid_done, status = os.waitpid(pid, 0)
        exit_code = os.WEXITSTATUS(status)

        print(f"Parent: child {pid_done} exited with code {exit_code}")

if __name__ == "__main__":
    run_exec_pipe()

