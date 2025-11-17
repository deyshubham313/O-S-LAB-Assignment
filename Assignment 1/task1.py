import os

def create_processes(n):
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print("Child", i+1)
            print("PID:", os.getpid())
            print("Parent PID:", os.getppid())
            print("Hello from child", i+1)
            os._exit(0)
        else:
            os.wait()

if __name__ == "__main__":
    n = int(input("Enter number of child processes: "))
    create_processes(n)
    print("Parent: All children finished.")


