#!/usr/bin/env bash
# system_info.sh – Print detailed system information

echo "=============================="
echo "     SYSTEM INFORMATION"
echo "=============================="

echo
echo "--- Kernel Version ---"
uname -a
echo

echo "--- CPU Information (lscpu) ---"
lscpu || echo "lscpu command not available"
echo

echo "--- Memory Info (free -h) ---"
free -h || echo "free command not available"
echo

echo "--- Block Devices (lsblk) ---"
lsblk || echo "lsblk command not available"
echo

echo "--- Network Interfaces (ip addr) ---"
ip -c addr || echo "ip command not available"
echo

echo "--- System Uptime ---"
uptime || echo "uptime command not available"
echo

echo "--- DMI / Hardware Vendor Info ---"
if command -v dmidecode >/dev/null 2>&1; then
    if [ "$(id -u)" -eq 0 ]; then
        dmidecode -t system
    else
        echo "dmidecode exists but requires sudo permissions."
        echo "Run: sudo dmidecode -t system"
    fi
else
    echo "dmidecode not installed."
fi

echo
echo "--- PCI Devices (lspci) ---"
if command -v lspci >/dev/null 2>&1; then
    lspci | head -n 20
else
    echo "lspci not available."
fi

echo
echo "======= END OF REPORT ======="
