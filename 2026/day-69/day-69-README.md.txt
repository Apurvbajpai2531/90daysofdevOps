# 🚀 Day 69 – Ansible Playbooks & Essential Modules

## 📖 Overview

Today I moved beyond Ansible ad-hoc commands and started writing **Ansible Playbooks**—the core of Infrastructure Automation.

I learned how to automate package installation, service management, file operations, handlers, multiple plays, and idempotent configuration management using YAML-based playbooks.

---

## 🎯 Objectives

* Learn Ansible Playbooks
* Understand Plays & Tasks
* Work with Essential Modules
* Configure Handlers
* Explore Idempotency
* Execute Multiple Plays
* Practice Production Debugging

---

## 🛠️ Technologies Used

* Ansible
* AWS EC2
* YAML
* Amazon Linux
* Nginx
* SSH

---

## 📂 Project Structure

```text
ansible-playbooks/
├── ansible.cfg
├── inventory.ini
├── install-nginx.yml
├── essential-modules.yml
├── nginx-config.yml
├── multi-play.yml
├── files/
│   ├── app.conf
│   └── nginx.conf
├── day-69-playbooks.md
└── screenshots/
    ├── playbook-run.png
    ├── idempotency.png
    └── handlers.png
```

---

## 📚 What I Learned

### ✅ Playbook Structure

* Plays
* Hosts
* Tasks
* Modules
* Handlers

### ✅ Essential Modules

* yum / apt
* service
* copy
* file
* command
* shell
* lineinfile

### ✅ Handlers

Used **notify** to restart Nginx only when configuration files changed.

### ✅ Idempotency

Running the same playbook multiple times produced **no unnecessary changes**, ensuring consistent server configuration.

### ✅ Debugging

Practiced:

* `--check`
* `--diff`
* `-v`
* `-vv`
* `-vvv`

---

## 🚀 Commands Used

```bash
ansible-playbook install-nginx.yml
ansible-playbook essential-modules.yml
ansible-playbook nginx-config.yml
ansible-playbook multi-play.yml
ansible-playbook install-nginx.yml --check
ansible-playbook nginx-config.yml --check --diff
ansible-playbook install-nginx.yml -vvv
```

---

## 🎯 Key Learnings

* Playbooks automate repetitive tasks.
* YAML indentation is critical.
* Handlers restart services only when required.
* Idempotency ensures predictable automation.
* Modules simplify server management.
* Multiple plays can target different server groups within one playbook.

---
]

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofDevops

---

⭐ Thanks to **TrainWithShubham** for another practical DevOps learning challenge.
