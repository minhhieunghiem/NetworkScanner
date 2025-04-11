# Network Scanner

A simple Python-based network scanner using ARP requests to detect active devices on a local network.

##  Description

This tool sends ARP requests to a target IP range and lists all devices that respond, displaying their IP and MAC addresses. It's a useful utility for quickly checking who is connected to your network.

Built using:
- [`argparse`](https://docs.python.org/3/library/argparse.html) for CLI parsing
- [`scapy`](https://scapy.net/) for crafting and sending network packets

##  Features

- Scan a target IP range using ARP
- Get a list of connected devices with IP and MAC addresses

## Usage
Run the script with the -t option to specify the target IP address (in CIDR notation)

Example:

`python NetworkScanner.py -t 192.168.1.1/24`

## Requirements

- Python 3.6+
- `scapy` library

## Notes

This script must be run with administrative/root privileges to send ARP packets.
