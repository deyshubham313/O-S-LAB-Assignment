import os
import time

def cpu_task(name, duration=5):
    start = time.time()
    while time.time() - start < duration:
        _ = 0
        for i in range(100000):
            _ += i * i
    print(f"Process {name} (PID={os.getpid()}) finished.")

if __name__ == "__main__":
    print("—— PROCESS PRIORITIZATION DEMO ——")

    for i in range(3):
        pid = os.fork()
        if pid == 0:
            os.nice(i * 5)
            print(f"Child {i} started with nice value {i*5}, PID={os.getpid()}, PPID={os.getppid()}")
            cpu_task(f"Child {i}")
            os._exit(0)

    for _ in range(3):
        os.wait()
    print("All child processes completed.")

