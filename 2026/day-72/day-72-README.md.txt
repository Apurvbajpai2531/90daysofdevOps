# 🚀 Day 72 – Ansible Project: Automating Docker & Nginx Deployment

## 📖 Overview

Day 72 brings together everything learned throughout the Ansible journey into a real-world deployment project.

Using **Ansible Roles**, I automated the complete deployment of a Dockerized application with **Nginx configured as a Reverse Proxy**. The project also secures Docker Hub credentials using **Ansible Vault**, making the deployment modular, repeatable, and production-ready.

---

## 🎯 Objectives

* Build reusable Ansible Roles
* Install and Configure Docker
* Deploy Containerized Applications
* Configure Nginx Reverse Proxy
* Secure Credentials using Ansible Vault
* Perform End-to-End Automated Deployment

---

## 🛠️ Tech Stack

* Ansible
* Docker
* Docker Compose
* Nginx
* AWS EC2
* Jinja2 Templates
* Ansible Vault
* Linux
* YAML

---

## 📂 Project Structure

```text id="n81fgt"
ansible-docker-project/
├── ansible.cfg
├── inventory.ini
├── site.yml
├── group_vars/
│   ├── all.yml
│   └── web/
│       ├── vars.yml
│       └── vault.yml
├── roles/
│   ├── common/
│   ├── docker/
│   └── nginx/
├── templates/
├── requirements.yml
└── day-72-ansible-project.md
```

---

## 🚀 Features Implemented

### ✅ Common Role

* System Updates
* Install Common Packages
* Configure Timezone
* Configure Hostname
* Create Deploy User

### ✅ Docker Role

* Install Docker Engine
* Install Docker Compose
* Docker Hub Login
* Pull Docker Images
* Run Containers
* Health Check using URI Module

### ✅ Nginx Role

* Install Nginx
* Configure Reverse Proxy
* Validate Configuration
* Reload Services
* Route Traffic to Docker Containers

### ✅ Ansible Vault

* Encrypt Docker Hub Credentials
* Secure Secrets
* Vault Password File
* CI/CD Friendly Configuration

---

## 📌 Deployment Workflow

```text id="vg8el0"
Ansible Control Node
        │
        ▼
Apply Common Role
        │
        ▼
Install Docker
        │
        ▼
Pull Docker Image
        │
        ▼
Run Container (Port 8080)
        │
        ▼
Configure Nginx
        │
        ▼
Reverse Proxy (Port 80)
        │
        ▼
Production Ready Application
```

---

## 💻 Commands Used

```bash id="txs9vl"
ansible-playbook site.yml --check --diff

ansible-playbook site.yml

ansible-playbook site.yml --tags docker

ansible-playbook site.yml --tags nginx

docker ps

curl http://localhost:8080

curl http://localhost
```

---

## 🎯 Key Learnings

* Combined all Ansible concepts into one project.
* Built reusable automation with Roles.
* Used Jinja2 Templates for dynamic configuration.
* Protected secrets using Ansible Vault.
* Automated Docker deployment end-to-end.
* Configured Nginx as a Reverse Proxy.
* Verified idempotent deployments using repeated playbook runs.

---

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ If you found this project useful, feel free to Star the repository.

Happy Learning! 🚀
