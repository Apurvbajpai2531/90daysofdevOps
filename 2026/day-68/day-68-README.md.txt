# 🚀 Day 68 – Introduction to Ansible & Inventory Setup

## 📖 Overview

Today I began my **Ansible** journey by learning the fundamentals of **Configuration Management**. After provisioning infrastructure with Terraform, I explored how Ansible automates software installation, server configuration, user management, and system administration across multiple servers.

I configured an **Ansible Control Node**, created an **Inventory** with multiple AWS EC2 instances, and successfully executed my first **ad-hoc commands** over SSH—without installing any agents on the managed nodes.

---

## 🎯 Objectives

* Understand Configuration Management
* Learn Ansible Architecture
* Install Ansible
* Create an Inventory
* Connect multiple EC2 instances
* Execute Ad-hoc Commands
* Explore Inventory Groups & Host Patterns

---

## 🛠️ Technologies Used

* Ansible
* AWS EC2
* SSH
* Amazon Linux / Ubuntu
* AWS Security Groups
* Terraform (for provisioning)

---

## 📂 Project Structure

```text
ansible-practice/
├── ansible.cfg
├── inventory.ini
├── hello.txt
├── day-68-ansible-intro.md
└── screenshots/
    ├── ansible-ping.png
    ├── inventory.png
    └── adhoc-commands.png
```

---

## 📚 What I Learned

### ✅ Configuration Management

* Automates server configuration
* Ensures consistency
* Reduces manual effort
* Eliminates configuration drift

### ✅ Ansible Architecture

* Control Node
* Managed Nodes
* Inventory
* Modules
* Playbooks

### ✅ Inventory Groups

* Web Servers
* App Servers
* Database Servers
* Group of Groups

### ✅ Ad-hoc Commands

Executed:

* Ping
* Uptime
* Free Memory
* Disk Usage
* Install Git
* Copy File

### ✅ Important Concepts

* Agentless Architecture
* SSH-based Communication
* Inventory Management
* `command` vs `shell`
* `--become` privilege escalation

---

## 🚀 Commands Used

```bash
ansible --version
ansible all -m ping
ansible all -m command -a "uptime"
ansible all -m command -a "df -h"
ansible web -m yum -a "name=git state=present" --become
ansible all -m copy -a "src=hello.txt dest=/tmp/hello.txt"
```

---

## 🎯 Key Learnings

* Ansible is completely agentless.
* SSH is enough to manage remote servers.
* Inventory organizes infrastructure efficiently.
* Ad-hoc commands are useful for quick administrative tasks.
* Playbooks will automate repeatable workflows.

---
## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofDevops


---

⭐ Thanks to **TrainWithShubham** for another practical DevOps learning session.
