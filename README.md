# 🖥️ Operating Systems Lab Assignments (OS_LAB_ASSIGN)

This repository contains all of my Operating Systems Lab assignments completed as part of my coursework.  
Each task demonstrates core OS concepts like process management, system calls, file descriptors, process scheduling, and system simulation.

---

## Repository Structure

| File/Folder                | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `Assignment1/`             | Contains **task1.py** to **task5.py**, demonstrating core OS concepts: process creation, IPC, synchronization, and CPU scheduling simulations. |
| `Assignment2/`             | Contains Python scripts simulating **system startup, process creation, and termination** using multiprocessing and logging. |
| `Assignment3/`             | Contains CPU scheduling algorithm implementations: `fcfs.py`, `sjf.py` (non-preemptive), `srtf.py` (preemptive SJF), `rr.py` (Round Robin). |
| `ASSIGNMENT1.OS.pdf`       | PDF submission of Assignment 1 (theory + practical report).                 |
| `ASSIGNMENT2.OS.pdf`       | PDF submission of Assignment 2 (system startup simulation report).          |
| `ASSIGNMENT3.OS.pdf`       | PDF submission of Assignment 3 (CPU scheduling algorithms report).          |
| `README.md`                | This file.                                                                  |

---

## **Requirements**
- Python 3.x
- Linux environment (required for `os.fork()`, `/proc` inspection, and scheduling simulations)
- Basic knowledge of OS concepts like process management and CPU scheduling

---

## **How to Run**

```bash
### Assignment 1
cd OS_LAB/Assignment1
python3 task1.py
python3 task2.py
python3 task3.py
python3 task4.py
python3 task5.py

### Assignment 2
cd OS_LAB/Assignment2
python3 <script_name>.py
# Check process_log.txt for output logs

### Assignment 3
cd OS_LAB/Assignment3
python3 fcfs.py     # First Come First Serve
python3 sjf.py      # Shortest Job First (non-preemptive)
python3 srtf.py     # Shortest Remaining Time First (preemptive SJF)
python3 rr.py       # Round Robin


