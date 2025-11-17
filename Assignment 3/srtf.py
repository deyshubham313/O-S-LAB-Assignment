# srtf.py - Shortest Remaining Time First (Preemptive Scheduling)

def read_processes():
    n = int(input("Number of processes: ").strip())
    procs = []
    for i in range(n):
        default_name = f"P{i+1}"
        line = input(f"Process {i+1} (name arrival burst) [e.g. {default_name} 0 5]: ").strip()
        parts = line.split()
        name = parts[0] if len(parts) >= 1 else default_name
        at = int(parts[1]) if len(parts) >= 2 else 0
        bt = int(parts[2]) if len(parts) >= 3 else 0
        procs.append({"name": name, "arrival": at, "burst": bt, "remaining": bt})
    return procs

def srtf(procs):
    n = len(procs)
    time = 0
    completed = 0
    last_proc = None
    while completed < n:
        # find process with shortest remaining time at current time
        available = [p for p in procs if p["arrival"] <= time and p["remaining"] > 0]
        if available:
            current = min(available, key=lambda p: p["remaining"])
            if "start" not in current:
                current["start"] = time
            current["remaining"] -= 1
            time += 1
            if current["remaining"] == 0:
                current["completion"] = time
                current["turnaround"] = current["completion"] - current["arrival"]
                current["waiting"] = current["turnaround"] - current["burst"]
                completed += 1
        else:
            time += 1
    return procs

def print_table(procs):
    print("\n{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
        "Process","Arrival","Burst","Start","Completion","Waiting"))
    for p in procs:
        print("{:<8} {:<8} {:<8} {:<8} {:<12} {:<8}".format(
            p["name"], p["arrival"], p["burst"], p.get("start",0), p["completion"], p["waiting"]))
    avg_wait = sum(p["waiting"] for p in procs)/len(procs)
    avg_turn = sum(p["turnaround"] for p in procs)/len(procs)
    print(f"\nAverage waiting time: {avg_wait:.2f}")
    print(f"Average turnaround time: {avg_turn:.2f}")

if __name__ == "__main__":
    procs = read_processes()
    res = srtf(procs)
    print_table(res)
