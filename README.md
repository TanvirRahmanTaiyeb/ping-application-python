<h1 align="center">📡 Python Ping Application</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python" />
  <img src="https://img.shields.io/badge/Socket%20Programming-Enabled-green?style=flat-square" />
  <img src="https://img.shields.io/badge/ICMP-Packet%20Level-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/License-CC--BY--NC--ND%204.0-lightgrey?style=flat-square&logo=creativecommons" />
</p>

---

## 📘 Project Overview

This is a raw socket-based ICMP Ping tool written in Python.  
It replicates the fundamental behavior of the native `ping` command by crafting and sending ICMP Echo Request packets and interpreting the replies.

This project is designed to help understand low-level network programming concepts and how the Internet Control Message Protocol works under the hood.

---

## 🚀 Key Features

- 🧮 Manual construction of ICMP Echo Request packets
- 🔁 Checksum validation for data integrity
- 📥 ICMP Echo Reply parsing with round-trip time (RTT)
- ⏱️ Time-to-Live (TTL) calculation
- ⚙️ Cross-platform (Windows/Linux – requires admin/root privileges)
- 📚 Great for educational and network diagnostics purposes

---

## 🎥 Live Demonstration

Watch the tool in action:  
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

> **Important:** This script requires **elevated privileges** (Admin on Windows / root on Linux) to send raw ICMP packets.

```bash
sudo python ping.py
