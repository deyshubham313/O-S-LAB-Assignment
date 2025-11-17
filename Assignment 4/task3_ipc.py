import os
import sys
# ipc_pipe_fork.py
# Simple IPC using os.pipe() and os.fork()
# Parent sends a message to child; child reads it and prints it.

def parent_child_communication():
    # Create pipe (r = read end, w = write end)
    r, w = os.pipe()

    pid = os.fork()

    if pid == 0:
        # -------- CHILD PROCESS --------
        os.close(w)  # Child doesn't write

        rfd = os.fdopen(r, 'r')
        msg = rfd.read()  # read everything sent by parent
        print(f"Child (pid {os.getpid()}): received from parent: {msg.strip()}")

        rfd.close()
        sys.exit(0)

    else:
        # -------- PARENT PROCESS --------
        os.close(r)  # Parent doesn't read

        wfd = os.fdopen(w, 'w')
        message = "Hello child! This is the parent.\n"
        wfd.write(message)
        wfd.flush()
        wfd.close()

        # Wait for child to finish
        pid_done, status = os.waitpid(pid, 0)
        print(f"Parent: child {pid_done} exited with status {status}")

if __name__ == "__main__":
    parent_child_communication()

