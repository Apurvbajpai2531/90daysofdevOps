# 🚀 Day 70 – Variables, Facts, Conditionals & Loops in Ansible

## 📖 Overview

Today's focus was making Ansible playbooks **dynamic and intelligent**. Instead of writing static automation, I learned how to use **variables, facts, conditionals, loops, and registered outputs** to build reusable playbooks that adapt automatically to different hosts, operating systems, and environments.

This is a major step toward writing production-ready Infrastructure as Code.

---

## 🎯 Objectives

* Work with Ansible Variables
* Understand Variable Precedence
* Use `group_vars` and `host_vars`
* Gather System Facts
* Apply Conditional Execution
* Automate Bulk Operations with Loops
* Generate Dynamic Server Reports

---

## 🛠️ Technologies Used

* Ansible
* AWS EC2
* Amazon Linux
* YAML
* SSH
* Linux Commands

---

## 📂 Project Structure

```text
ansible-practice/
├── ansible.cfg
├── inventory.ini
├── group_vars/
│   ├── all.yml
│   ├── web.yml
│   └── db.yml
├── host_vars/
│   └── web-server.yml
├── playbooks/
│   ├── variables-demo.yml
│   ├── facts-demo.yml
│   ├── conditional-demo.yml
│   ├── loops-demo.yml
│   └── server-report.yml
└── day-70-variables-loops.md
```

---

## 📚 What I Learned

### ✅ Variables

* Playbook Variables
* Extra Variables (`-e`)
* `group_vars`
* `host_vars`
* Variable Precedence

### ✅ Ansible Facts

Collected dynamic system information such as:

* Operating System
* Distribution Version
* Hostname
* IP Address
* Total RAM
* CPU Information
* Network Interfaces

### ✅ Conditionals

Used `when` statements to:

* Install packages based on server roles
* Execute OS-specific tasks
* Apply production-only configurations
* Run tasks based on available memory

### ✅ Loops

Automated repetitive tasks:

* Creating multiple users
* Creating directories
* Installing packages
* Displaying loop results

### ✅ Register & Debug

Captured command outputs and generated dynamic server health reports using:

* Disk Usage
* Memory Information
* Running Services
* System Facts

---

## 🚀 Commands Practiced

```bash
ansible-playbook variables-demo.yml
ansible-playbook facts-demo.yml
ansible-playbook conditional-demo.yml
ansible-playbook loops-demo.yml
ansible-playbook server-report.yml

ansible web-server -m setup
ansible web-server -m setup -a "filter=ansible_distribution*"
```

---

## 🎯 Key Learnings

* Variables make playbooks reusable.
* Facts provide real-time system information.
* Conditionals ensure tasks run only where required.
* Loops simplify repetitive operations.
* Registered variables enable intelligent automation.
* One playbook can behave differently for each server.

---
## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofDevops

---

⭐ Thanks to **TrainWithShubham** for another practical DevOps learning experience.
