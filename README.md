# 📡 Python Ping Application

A raw socket-based ICMP Ping tool developed using Python.  
This application replicates the core functionality of the `ping` command by constructing, sending, and interpreting ICMP packets manually.

---

## 🚀 Features

- Calculates checksum for ICMP packet integrity
- Sends raw ICMP Echo Requests using sockets
- Receives and parses ICMP Echo Replies
- Calculates round-trip time (RTT) and TTL
- Cross-platform (Linux/Windows with admin/root access)

---

## 📷 Screenshots

> ICMP Ping output with response time and TTL:

![Ping Output](https://i.imgur.com/YOUR_IMAGE_ID_HERE.png) <!-- Replace with actual image link -->

---

## 🎥 Video Demonstration

Watch how it works in real-time:  
👉 [Video Demo – Python Ping Application](https://youtu.be/YOUR_VIDEO_LINK_HERE) <!-- Replace with your actual YouTube link -->

---

## ⚙️ How to Run

> Make sure to run the script as **Administrator/root**, as raw sockets require elevated privileges.

```bash
sudo python ping.py

ping-application-python/
├── ping.py         # Main script
├── LICENSE         # CC BY-NC-ND 4.0 License
└── README.md       # Project documentation
