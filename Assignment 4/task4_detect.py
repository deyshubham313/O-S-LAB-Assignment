# detect_vm.py – Detect whether system is running inside a Virtual Machine

import subprocess
import os

VM_KEYWORDS = [
    "kvm", "qemu", "vmware", "virtualbox",
    "hyper-v", "xen", "bochs", "parallels",
    "google", "amazon", "azure"
]

def check_lscpu():
    """Check virtualization info from lscpu."""
    try:
        output = subprocess.check_output(["lscpu"]).decode().lower()
        for key in VM_KEYWORDS:
            if key in output:
                return True, f"Detected VM keyword '{key}' in lscpu"
        return False, "No VM indicators found in lscpu"
    except FileNotFoundError:
        return False, "lscpu not found"

def check_dmi():
    """Check DMI sys_vendor / product_name."""
    paths = [
        "/sys/class/dmi/id/product_name",
        "/sys/class/dmi/id/sys_vendor"
    ]
    collected = ""

    for p in paths:
        try:
            collected += open(p).read().lower() + " "
        except:
            pass

    for key in VM_KEYWORDS:
        if key in collected:
            return True, f"Detected VM keyword '{key}' in DMI info"

    return False, "No virtualization info found in DMI"

def check_cpuinfo():
    """Check hypervisor flag in cpuinfo."""
    try:
        data = open("/proc/cpuinfo").read().lower()
        if "hypervisor" in data:
            return True, "Found 'hypervisor' flag in cpuinfo"
        return False, "No hypervisor flag in cpuinfo"
    except:
        return False, "cpuinfo not readable"

def detect_vm():
    print("====== VM DETECTION REPORT ======\n")

    checks = [
        ("LSCPU", check_lscpu()),
        ("DMI", check_dmi()),
        ("CPUINFO", check_cpuinfo())
    ]

    vm_found = False
    for label, (status, message) in checks:
        print(f"[{label}] {message}")
        if status:
            vm_found = True

    print("\n=================================")
    if vm_found:
        print("RESULT: Virtual Machine detected")
    else:
        print("RESULT: No Virtual Machine detected")
    print("=================================")

if __name__ == "__main__":
    detect_vm()
