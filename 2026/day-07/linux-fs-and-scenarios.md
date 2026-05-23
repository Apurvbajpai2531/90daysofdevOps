# Day 07 - Linux File System Hierarchy & Scenario-Based Practice

## Part 1: Linux File System Hierarchy

### /

Purpose:
Root directory. Everything in Linux starts from here.

I would use this when:
I need to navigate the entire filesystem.

---

### /home

Purpose:
Stores home directories of normal users.

I would use this when:
I need to access user files and personal data.

---

### /root

Purpose:
Home directory of the root user.

I would use this when:
I am working as the root administrator.

---

### /etc

Purpose:
Stores system configuration files.

Examples:
- hostname
- hosts
- passwd

I would use this when:
I need to modify system settings.

---

### /var/log

Purpose:
Stores system and application logs.

Examples:
- syslog
- auth.log

I would use this when:
I am troubleshooting errors and services.

---

### /tmp

Purpose:
Stores temporary files.

I would use this when:
I need temporary storage for testing.

---

### /bin

Purpose:
Contains essential Linux commands.

Examples:
- ls
- cp
- mv

I would use this when:
I need basic system commands.

---

### /usr/bin

Purpose:
Contains user command binaries.

Examples:
- git
- docker
- python3

I would use this when:
I need commonly used applications.

---

### /opt

Purpose:
Stores optional or third-party software.

Examples:
- Jenkins
- Custom applications

I would use this when:
I install software manually.

---

## Hands-On Commands

```bash
du -sh /var/log/* 2>/dev/null | sort -h | tail -5
cat /etc/hostname
ls -la ~
```

# Part 2: Scenario-Based Practice

## Scenario 1: Service Not Starting

### Step 1
```bash
systemctl status myapp
```
Why: Check if service is running or failed.

### Step 2
```bash
journalctl -u myapp -n 50
```
Why: Check recent logs.

### Step 3
```bash
systemctl is-enabled myapp
```
Why: Verify startup configuration.

### Step 4
```bash
journalctl -xe
```
Why: View detailed system errors.

---

## Scenario 2: High CPU Usage

### Step 1
```bash
top
```
Why: View live CPU usage.

### Step 2
```bash
htop
```
Why: Interactive process monitoring.

### Step 3
```bash
ps aux --sort=-%cpu | head -10
```
Why: Find top CPU-consuming processes.

### Step 4
```bash
ps -p <PID> -f
```
Why: View process details.

---

## Scenario 3: Finding Service Logs

### Step 1
```bash
systemctl status docker
```
Why: Check service status.

### Step 2
```bash
journalctl -u docker -n 50
```
Why: View last 50 log entries.

### Step 3
```bash
journalctl -u docker -f
```
Why: Follow logs in real time.

---

## Scenario 4: File Permission Issue

### Step 1
```bash
ls -l /home/user/backup.sh
```
Why: Check permissions.

### Step 2
```bash
chmod +x /home/user/backup.sh
```
Why: Add execute permission.

### Step 3
```bash
ls -l /home/user/backup.sh
```
Why: Verify permission change.

### Step 4
```bash
./backup.sh
```
Why: Run the script.
