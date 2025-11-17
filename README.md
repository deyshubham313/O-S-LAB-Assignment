🖥️ Operating Systems Lab Assignments (OS_LAB_ASSIGN)

This repository contains solutions to the Operating Systems Lab assignments, showcasing key OS concepts such as process management, inter-process communication (IPC), synchronization, CPU scheduling, and system simulation.

Repository Structure
File/Folder	Description
Assignment1/	Contains Python scripts (task1.py to task5.py) demonstrating core OS concepts like process creation, IPC, synchronization, and CPU scheduling simulations.
Assignment2/	Simulates system startup, process creation, and termination using Python's multiprocessing module and logging for process tracking.
Assignment3/	Implements CPU scheduling algorithms: FCFS (First Come First Serve), SJF (Shortest Job First, non-preemptive), SRTF (Shortest Remaining Time First, preemptive SJF), and Round Robin (RR).
ASSIGNMENT1.OS.pdf	PDF report for Assignment 1, including both theoretical explanations and practical results.
ASSIGNMENT2.OS.pdf	PDF report for Assignment 2, covering the system startup simulation and analysis.
ASSIGNMENT3.OS.pdf	PDF report for Assignment 3, analyzing the various CPU scheduling algorithms.
README.md	This file, providing an overview of the repository and usage instructions.
Key Concepts Covered

Process Management: Creation, termination, and synchronization of processes.

Inter-process Communication (IPC): Shared memory, message passing, etc.

CPU Scheduling: Simulating scheduling algorithms like FCFS, SJF, SRTF, and Round Robin.

System Calls: Usage of system calls like os.fork(), os.wait(), etc.

File Descriptors: Demonstrating usage in task scripts.

Requirements

Python 3.x: Ensure you have Python 3 installed. (Recommended version: 3.6+)

Linux Environment: Some scripts require Linux-specific functionality (e.g., os.fork(), /proc filesystem access).

Basic OS Concepts: Familiarity with OS concepts like process scheduling, inter-process communication (IPC), and system calls.

How to Run
Assignment 1: Process Management & CPU Scheduling
cd OS_LAB/Assignment1
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
python3 task5.py

Assignment 2: System Startup & Process Creation
cd OS_LAB/Assignment2
python3 <script_name>.py
# Check 'process_log.txt' for detailed logs of system startup and process handling.

Assignment 3: CPU Scheduling Algorithms
cd OS_LAB/Assignment3
python3 fcfs.py     # First Come First Serve (FCFS)
python3 sjf.py      # Shortest Job First (non-preemptive)
python3 srtf.py     # Shortest Remaining Time First (preemptive)
python3 rr.py       # Round Robin (RR)

Detailed Overview of Each Assignment
Assignment 1: Process Creation & Scheduling Simulations

Task 1: Process creation using os.fork().

Task 2: Implementing Inter-process communication (IPC) via pipes and shared memory.

Task 3: Synchronization of processes using threading and semaphores.

Task 4: CPU scheduling simulation using FCFS and SJF algorithms.

Task 5: Implementing a preemptive CPU scheduler for SRTF.

Assignment 2: System Startup Simulation

Simulates a system startup process using Python’s multiprocessing library.

Logs process creation, termination, and inter-process interaction with the help of logging module.

Tracks process states and provides an output log (process_log.txt).

Assignment 3: CPU Scheduling Algorithms

Implements popular CPU scheduling algorithms in Python:

FCFS: Non-preemptive scheduling based on the order of arrival.

SJF: Non-preemptive scheduling where the shortest job is executed first.

SRTF: Preemptive version of SJF, where the process with the shortest remaining time is given priority.

Round Robin: Time-sharing scheduling algorithm where each process gets an equal time slice (quantum).

Contributing

If you'd like to contribute, feel free to fork the repository and submit pull requests for any improvements or additions!

License

This repository is intended for educational purposes and is licensed under the MIT License.

Additional Suggestions:

Unit Tests: Consider adding basic unit tests to validate each algorithm. This will make it easier to verify correctness as you modify or extend the code.

Example Output: It would be great to include example outputs for each script. This can help users verify their results without having to dig into the code.

Detailed Explanations: A brief explanation or docstring in each Python script (e.g., for each function) would help users understand the code’s functionality.
