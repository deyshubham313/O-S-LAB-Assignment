import os

def main():
    n = int(input("Enter number of child processes: "))
    commands = [["ls", "-l"], ["date"], ["ps"]]

    for i in range(n):
        pid = os.fork()
        if pid == 0:
            print(f"\nChild {i+1}: PID = {os.getpid()}, Parent PID = {os.getppid()}")
            print(f"Executing command: {commands[i % len(commands)]}")
            os.execvp(commands[i % len(commands)][0], commands[i % len(commands)])
        else:
            os.wait()

    print("\nParent: All child processes have executed commands.")

if __name__ == "__main__":
    main()
