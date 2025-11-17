import os

pid = input("Enter PID of the process to inspect: ")
proc_path = f"/proc/{pid}"

try:
    exe_path = os.readlink(f"{proc_path}/exe")
    print(f"Executable path for PID {pid}: {exe_path}")
except Exception as e:
    print(f"Could not read executable path: {e}")

fd_path = f"{proc_path}/fd"
try:
    fds = os.listdir(fd_path)
    print(f"Open file descriptors for PID {pid}: {fds}")
except Exception as e:
    print(f"Could not list file descriptors: {e}")

