import logging
import multiprocessing as mp
import time
import os

LOGFILE = "process_log.txt"

def setup_logging():
    logging.basicConfig(
        filename=LOGFILE,
        level=logging.INFO,
        format="%(asctime)s [%(processName)s:%(process)d] %(levelname)s: %(message)s"
    )

    logging.getLogger().addHandler(logging.StreamHandler())

def worker(name, duration):
    logging.info(f"Worker '{name}' starting (PID={os.getpid()})")
    t0 = time.time()
    time.sleep(duration)
    elapsed = time.time() - t0
    logging.info(f"Worker '{name}' finished (PID={os.getpid()}) elapsed={elapsed:.2f}s")

def main():
    setup_logging()
    logging.info("System startup simulation beginning")

    tasks = [
        ("init_services", 2),
        ("mount_filesystems", 1),
        ("network_manager", 3),
        ("login_manager", 1.5),
        ("cron_jobs", 0.8),
    ]

    procs = []

    for name, dur in tasks:
        p = mp.Process(target=worker, args=(name, dur), name=name)
        p.start()
        procs.append(p)

        time.sleep(0.2)

    for p in procs:
        p.join()

    logging.info("Startup simulation complete")

if __name__ == "__main__":
    main()

