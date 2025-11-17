import os
import time

# ZOMBIE PROCESS
print("----- ZOMBIE PROCESS -----")
pid = os.fork()

if pid == 0:
    print(f"Child (Zombie) PID = {os.getpid()}")
    os._exit(0)
else:
    print(f"Parent PID = {os.getpid()} | Child PID = {pid} created")
    print("Sleeping for 10 seconds so child becomes zombie...")
    time.sleep(10)
    print("Parent done sleeping. You can check zombie with 'ps -el | grep defunct'.")

time.sleep(2)

# ORPHAN PROCESS
print("\n----- ORPHAN PROCESS -----")
pid2 = os.fork()

if pid2 == 0:
    print(f"Orphan Child PID = {os.getpid()} starting...")
    time.sleep(5)
    print(f"Orphan Child PID = {os.getpid()} done.")
else:
    print(f"Parent PID = {os.getpid()} exiting immediately, child becomes orphan")
    os._exit(0)


