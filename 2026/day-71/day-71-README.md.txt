# 🚀 Day 71 – Ansible Roles, Galaxy, Templates & Vault

## 📖 Overview

Day 71 focused on writing **production-grade Ansible automation** by organizing playbooks into reusable **Roles**, creating dynamic configuration files with **Jinja2 Templates**, leveraging community roles through **Ansible Galaxy**, and protecting sensitive information using **Ansible Vault**.

This approach makes automation modular, reusable, secure, and easier to maintain in real-world DevOps environments.

---

## 🎯 Objectives

* Build a custom Ansible Role
* Create dynamic Jinja2 Templates
* Install and use Galaxy Roles
* Secure secrets with Ansible Vault
* Combine Roles, Templates, and Vault into one automation workflow

---

## 🛠️ Technologies Used

* Ansible
* AWS EC2
* Jinja2
* Ansible Galaxy
* Ansible Vault
* Nginx
* Docker
* YAML

---

## 📂 Project Structure

```text
ansible-practice/
├── ansible.cfg
├── inventory.ini
├── group_vars/
│   └── db/
│       └── vault.yml
├── roles/
│   └── webserver/
│       ├── defaults/
│       ├── files/
│       ├── handlers/
│       ├── meta/
│       ├── tasks/
│       ├── templates/
│       └── vars/
├── templates/
│   └── db-config.j2
├── requirements.yml
├── site.yml
└── day-71-roles-templates-vault.md
```

---

## 🚀 Topics Covered

### ✅ Ansible Roles

* Structured automation
* Reusable tasks
* Handlers
* Defaults
* Templates
* Variables

### ✅ Jinja2 Templates

* Dynamic Nginx Virtual Host
* Dynamic HTML Page
* Database Configuration Templates
* Variable Rendering
* Default Filters

### ✅ Ansible Galaxy

* Installed community roles
* Used `requirements.yml`
* Installed Docker role
* Managed reusable automation

### ✅ Ansible Vault

* Encrypted passwords
* Protected API keys
* Managed secrets securely
* Used Vault Password File
* Integrated secrets into playbooks

---

## 🔒 Key Learnings

* Roles organize large Ansible projects.
* Templates generate configuration files dynamically.
* Galaxy saves time by reusing trusted community roles.
* Vault keeps credentials encrypted and secure.
* Modular automation is easier to scale and maintain.

---

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ If you found this repository helpful, consider giving it a Star.
