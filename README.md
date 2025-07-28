<h1 align="center">📡 Python Ping Application</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Socket%20Programming-Enabled-green?style=flat-square" />
  <img src="https://img.shields.io/badge/ICMP-Packet%20Level-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/License-CC--BY--NC--ND%204.0-lightgrey?style=flat-square&logo=creativecommons" />
</p>

---

## 📘 Project Overview

This is a raw socket-based ICMP Ping tool developed in Python.

It replicates the core behavior of the native `ping` command by manually crafting ICMP Echo Request packets and parsing ICMP Echo Replies, giving you low-level control and visibility into how networking protocols operate.

This project is especially useful for:
- 🔐 Cybersecurity students learning about network reconnaissance and packet inspection.
- 🌐 Networking learners interested in understanding the ICMP protocol, TTL, latency, and diagnostic utilities.

---

## 🚀 Key Features

- 🧮 Manual construction of ICMP Echo Request packets
- 🔁 Checksum validation for ICMP integrity
- 📥 Parsing of ICMP Echo Replies (incl. RTT and TTL)
- ⏱️ Real-time round-trip time (RTT) calculation
- ⚙️ Cross-platform (Windows/Linux with admin/root access)
- 👨‍💻 Educational tool for learning protocol-level internals

---

## 🎥 Live Demonstration

Watch the tool in action on YouTube:  
🎬 [Video Demo – Python Ping Application](https://youtu.be/03eXKgsISiM?si=DI5meqN5Oqwm7roc)

---

## 🖼️ Screenshots

<p align="center">
  <img width="600" alt="Yahoo Ping Output" src="https://github.com/user-attachments/assets/d0eab85e-516c-441f-8299-4c78211a68a3" />
  <br/>
  <em>Ping results for <code>yahoo.com</code></em>
</p>

<p align="center">
  <img width="600" alt="Google Ping Output" src="https://github.com/user-attachments/assets/5f0751af-bc4b-45bc-ae34-c3ce69067473" />
  <br/>
  <em>Ping results for <code>google.com</code></em>
</p>

<p align="center">
  <img width="600" alt="Facebook Ping Output" src="https://github.com/user-attachments/assets/20739e2b-9206-431e-b2f9-a629960153c3" />
  <br/>
  <em>Ping results for <code>facebook.com</code></em>
</p>

---

## ⚙️ How to Run

> **Note:** This tool uses raw sockets, which require **administrator/root privileges**.

### 🧪 Steps

```bash
# Linux or macOS (use sudo)
sudo python ping.py

# Windows (run your terminal as Administrator)
python ping.py

```

## 📁 Project Structure

