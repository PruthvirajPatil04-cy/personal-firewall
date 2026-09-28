# 🔥 Personal Firewall

A Python-based personal firewall designed to monitor, analyze, and filter network traffic using configurable security rules. The project demonstrates fundamental concepts of **network security, packet filtering, traffic monitoring, and security logging**.

> **Educational Project:** This project is intended for learning and cybersecurity experimentation in authorized environments.

---

## 📌 Overview

A firewall acts as a security barrier between a trusted system/network and potentially untrusted network traffic.

This project provides a personal firewall application capable of monitoring network traffic and applying predefined rules to determine whether traffic should be **allowed or blocked**.

The project can be extended with additional filtering rules, logging capabilities, packet analysis, and a graphical interface.

---

## 🎯 Objectives

* Monitor incoming and outgoing network traffic.
* Analyze basic packet information.
* Filter traffic according to predefined rules.
* Allow or block network connections.
* Maintain logs of firewall activity.
* Understand practical network security concepts.
* Learn how firewall rules interact with network traffic.

---

## 🛠️ Technologies Used

| Technology          | Purpose                      |
| ------------------- | ---------------------------- |
| Python              | Core application             |
| Scapy               | Packet capture and analysis  |
| iptables / nftables | Linux traffic filtering      |
| JSON                | Firewall rule configuration  |
| Logging             | Security event recording     |
| Tkinter             | Optional graphical interface |

---

## ⚙️ Key Features

### 1. Traffic Monitoring

The firewall can monitor network traffic and extract information such as:

* Source IP address
* Destination IP address
* Source port
* Destination port
* Network protocol
* Packet information

### 2. Rule-Based Filtering

Traffic can be controlled using configurable rules.

Example:

```text
ALLOW TCP 443
BLOCK TCP 23
BLOCK 192.168.1.50
ALLOW UDP 53
```

### 3. Packet Filtering

The firewall analyzes traffic and determines whether it matches an existing security rule.

```text
Network Traffic
       ↓
Packet Capture
       ↓
Packet Analysis
       ↓
Rule Matching
    ↙       ↘
MATCH      NO MATCH
  ↓            ↓
BLOCK/ALLOW   DEFAULT RULE
       ↓
     Logging
```

### 4. Security Logging

Firewall events can be recorded for later analysis.

Example:

```text
[BLOCKED] 192.168.1.50 → TCP → Port 23
[ALLOWED] 8.8.8.8 → UDP → Port 53
[ALLOWED] Web Server → TCP → Port 443
```

---

## 📁 Project Structure

```text
personal-firewall/
│
├── firewall/
│   ├── __init__.py
│   ├── monitor.py
│   ├── rules.py
│   ├── filt
```

