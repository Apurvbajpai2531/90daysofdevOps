# Linux Architecture, Processes, and systemd 🚀

## Core Components of Linux

### 1. Kernel
The kernel is the core part of Linux.

Responsibilities:
- Manages CPU and memory
- Handles hardware communication
- Manages processes
- Handles file systems and networking

The kernel acts as a bridge between hardware and software.

---

### 2. User Space
User space is where users and applications run.

Examples:
- Bash
- VS Code
- Docker
- Chrome

Applications communicate with hardware through the kernel.

---

### 3. Init / systemd
systemd is the init system used in modern Linux distributions.

Responsibilities:
- Starts services during system boot
- Restarts failed services
- Manages logs
- Controls background services

Example services:
- nginx
- docker
- ssh

---

# Process Management in Linux

A process is a running instance of a program.

Each process contains:
- PID (Process ID)
- Parent Process
- CPU usage
- Memory allocation

Linux uses a scheduler to manage processes efficiently.

---

# Process States

| State | Meaning |
|------|------|
| Running (R) | Process actively using CPU |
| Sleeping (S) | Waiting for resources/input |
| Stopped (T) | Process execution paused |
| Zombie (Z) | Process completed but not cleaned |
| Idle | Waiting for execution |

---

# Useful systemd Commands

```bash
systemctl status nginx
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl enable nginx
```

---

# 5 Linux Commands Used Daily

```bash
ps aux
top
htop
systemctl status
journalctl -xe
```

---

# Why This Matters in DevOps

Understanding Linux internals helps DevOps engineers to:

- Debug crashed services faster
- Fix CPU and memory issues
- Monitor production systems
- Understand logs and service restarts confidently

#90DaysOfDevOps 🚀