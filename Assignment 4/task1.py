import subprocess
import sys

scripts = ['script1.py', 'script2.py', 'script3.py']

if __name__ == "__main__":
    for script in scripts:
        print(f"\n=== Executing {script} ===")
        result = subprocess.run(['python3', script])
        if result.returncode == 0:
            print(f"{script} executed successfully.\n")
        else:
            print(f"Error while executing {script} (exit code {result.returncode}).\n")
            sys.exit(result.returncode)






