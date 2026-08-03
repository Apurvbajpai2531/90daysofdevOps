# 🚀 Day 80 – Helm Project: Multi-Environment Deployment & CI/CD

## 📖 Overview

Day 80 marks the completion of my **Helm learning journey** in the **#90DaysOfDevOps** challenge.

I transformed the AI-BankApp Helm Chart into a production-ready deployment by introducing **environment-specific configurations**, **Helm Hooks**, **chart packaging**, and understanding how Helm integrates into a **GitOps CI/CD pipeline** with ArgoCD.

This project demonstrates how a **single Helm Chart** can deploy applications across **Development, Staging, and Production** environments without duplicating Kubernetes manifests.

---

# 🎯 Objectives

* Create environment-specific Helm values files
* Deploy the same application across multiple environments
* Add Helm Hooks for database readiness
* Package and version Helm Charts
* Understand GitOps integration with Helm
* Learn production Helm best practices

---

# 🛠️ Technologies Used

* Helm
* Kubernetes
* Kind
* Docker
* Spring Boot
* MySQL
* Ollama AI
* ArgoCD
* GitHub Actions
* GitOps

---

# 🌍 Multi-Environment Deployment

| Environment | Replicas | MySQL Storage | Gateway | Autoscaling |
| ----------- | -------: | ------------: | ------- | ----------- |
| Development |        1 |           2Gi | ❌       | Disabled    |
| Staging     |      2–3 |           5Gi | ❌       | Enabled     |
| Production  |      2–4 |          20Gi | ✅       | Enabled     |

Each environment uses its own `values-*.yaml` file while sharing the same Helm Chart.

---

# ⚙️ Helm Features Implemented

* Environment-specific values
* Helm Hooks (Pre-install & Pre-upgrade)
* Helm Test
* Chart Packaging
* Chart Versioning
* Release Management
* Production Configuration

---

# 🔄 Helm Release Lifecycle

```text
helm lint
      │
      ▼
helm template
      │
      ▼
helm install
      │
      ▼
helm test
      │
      ▼
helm upgrade
      │
      ▼
helm rollback
      │
      ▼
helm package
```

---

# 🔗 GitOps Workflow

```text
Developer Push
      │
GitHub Actions
      │
Build Docker Image
      │
Update values-prod.yaml
      │
Commit Changes
      │
ArgoCD Detects Changes
      │
helm upgrade
      │
Kubernetes Cluster
```

---

# 📦 Helm Hooks

Implemented:

* **Pre-install Hook** → Wait for MySQL before deploying BankApp
* **Pre-upgrade Hook** → Validate database availability during upgrades
* **Helm Test** → Verify Spring Boot health endpoint after deployment

---

# 📊 Helm vs Raw Manifests vs Kustomize

| Feature           | Raw YAML | Kustomize | Helm      |
| ----------------- | -------- | --------- | --------- |
| Reusable          | ❌        | ✅         | ✅         |
| Templates         | ❌        | ❌         | ✅         |
| Multi Environment | Limited  | Good      | Excellent |
| Package Manager   | ❌        | ❌         | ✅         |
| Rollback          | ❌        | ❌         | ✅         |
| CI/CD Friendly    | Medium   | High      | Excellent |

---

# 🚀 Production Best Practices

* Use `helm upgrade --install`
* Enable `--atomic`
* Use `--wait`
* Version Helm Charts
* Keep environment-specific values separate
* Use External Secrets or Vault instead of storing secrets in `values.yaml`
* Use Helm Diff before production upgrades

---

# 📚 Key Learnings

* One Helm Chart can support multiple environments.
* Values files eliminate configuration duplication.
* Helm Hooks improve deployment reliability.
* Packaging makes charts easy to distribute.
* Helm integrates seamlessly with GitOps workflows using ArgoCD.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Follow the repository to track my complete DevOps learning journey.
