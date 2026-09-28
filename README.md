# Personal Firewall (Cross-Platform)

A lightweight Python-based personal firewall that filters network traffic based on user-defined rules. This project includes real-time packet sniffing, logging of suspicious packets, and a simple graphical user interface (GUI) for live traffic monitoring. It is designed to run on both Windows and Linux platforms.

## Features

- Cross-platform support (Windows and Linux)
- Live packet sniffing using Scapy
- Rule engine for filtering traffic by IP, port, and protocol
- Logging of suspicious packets for auditing
- Simple GUI for real-time monitoring using Tkinter
- Optional integration with `iptables` on Linux for system-level control

## Project Structure
personal_firewall/
├── main.py # GUI application entry point
├── packet_sniffer.py # Packet capture and filtering
├── rule_engine.py # Firewall rule evaluation
├── logs/
│ └── suspicious.log # Log file for flagged packets
└── README.md # Project documentation


## Requirements

- Python 3.8 or above
- Scapy
- Tkinter (usually included with Python)
- Administrator/root privileges for packet sniffing

## Installation
1. Clone the repository:
2. Install dependencies:
3. (Optional) If using Linux and want to apply rules at the system level:
   
## Usage

Run the firewall GUI using:
This will open the GUI window and begin sniffing packets on the default interface. You can modify `packet_sniffer.py` to change interfaces or rule behavior.

## Rule Configuration

You can define firewall rules in `rule_engine.py`. Rules can allow or block packets based on:

- Source/Destination IP
- Source/Destination Port
- Protocol (TCP, UDP, ICMP)

## Logging

All packets that are flagged as suspicious or blocked are logged in `logs/suspicious.log` for audit purposes.

## Notes

- Running as administrator or root may be required to sniff packets depending on the OS.
- On Linux, integration with `iptables` allows actual blocking at the system level. On Windows, blocking is simulated at the application level.
