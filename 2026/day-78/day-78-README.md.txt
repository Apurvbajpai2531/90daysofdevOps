# 🚀 Day 78 – Introduction to Helm & Chart Basics

## 📖 Overview

On **Day 78** of my **#90DaysOfDevOps** journey, I started learning **Helm**, the package manager for Kubernetes.

Instead of manually managing multiple Kubernetes YAML files, I learned how Helm simplifies deployments through reusable, versioned, and configurable **Charts**. I deployed a **MySQL database** using the Bitnami Helm Chart, customized it with a values file, explored chart structure, and practiced release management with upgrades and rollbacks.

---

# 🎯 Objectives

* Install and configure Helm
* Understand Helm concepts
* Deploy MySQL using Bitnami Helm Chart
* Customize deployments using values.yaml
* Manage Helm releases (Install, Upgrade, Rollback, Uninstall)
* Explore Helm chart structure
* Compare raw Kubernetes manifests vs Helm

---

# 🛠️ Technologies Used

* Kubernetes
* Helm
* Kind Cluster
* Docker
* MySQL
* Bitnami Charts
* YAML

---

# 📂 Project Structure

```text
helm-lab/
├── mysql-values.yaml
├── screenshots/
│   ├── helm-list.png
│   ├── helm-history.png
│   ├── mysql-running.png
│   └── chart-structure.png
└── day-78-helm-intro.md
```

---

# 📦 Helm Concepts

### 📌 Chart

A Helm Chart is a reusable package containing Kubernetes manifests, templates, metadata, and default configuration.

### 📌 Release

A Release is a deployed instance of a Helm Chart running inside a Kubernetes cluster.

### 📌 Repository

A Repository stores and distributes Helm Charts, similar to Docker Hub for container images.

### 📌 Values

Values are configuration parameters used to customize deployments without modifying templates.

---

# 🚀 Deploying MySQL with Helm

Added the Bitnami repository:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Installed MySQL:

```bash
helm install bankapp-mysql bitnami/mysql
```

Customized deployment using:

```yaml
auth:
  rootPassword: Test@123
  database: bankappdb

primary:
  persistence:
    size: 5Gi
```

---

# 📊 Helm Release Lifecycle

* Install
* Upgrade
* Rollback
* History
* Uninstall

Commands practiced:

```bash
helm install
helm upgrade
helm history
helm rollback
helm uninstall
```

---

# 📂 Helm Chart Structure

```text
mysql/
├── Chart.yaml
├── values.yaml
├── charts/
├── templates/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── secrets.yaml
│   ├── NOTES.txt
│   └── _helpers.tpl
```

### Important Files

* **Chart.yaml** → Metadata about the chart
* **values.yaml** → Default configuration values
* **templates/** → Kubernetes resource templates
* **charts/** → Dependencies
* **NOTES.txt** → Post-install instructions

---

# ⚖️ Raw Kubernetes vs Helm

| Raw YAML             | Helm                        |
| -------------------- | --------------------------- |
| Multiple YAML files  | Single reusable chart       |
| Manual configuration | Values-driven configuration |
| No built-in rollback | `helm rollback` support     |
| Difficult upgrades   | Versioned releases          |
| Hardcoded values     | Environment-specific values |
| Less reusable        | Highly reusable             |

---

# 📚 Key Learnings

* Helm simplifies Kubernetes deployments.
* Charts package Kubernetes resources into reusable units.
* Values files eliminate hardcoded configurations.
* Release history makes upgrades and rollbacks safe.
* Community charts accelerate production deployments.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Feel free to explore the repository and follow my DevOps learning journey!

Happy Learning! 🚀
