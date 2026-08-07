# 🚀 Day 84 – Introduction to GitOps and ArgoCD

## 📖 Overview

Day 84 marks the beginning of my **GitOps** journey in the **#90DaysOfDevOps** challenge.

Until now, applications were deployed using `kubectl apply`. Today I explored a production-ready GitOps workflow using **ArgoCD**, where Git becomes the single source of truth and the Kubernetes cluster continuously reconciles itself with the desired state stored in the repository.

I also studied the AI-BankApp GitOps architecture, deployed the application through ArgoCD, explored the ArgoCD UI, and observed how automatic synchronization and self-healing work.

---

# 🎯 Objectives

* Understand GitOps principles
* Compare GitOps with traditional CI/CD
* Explore ArgoCD architecture and UI
* Deploy AI-BankApp using ArgoCD
* Understand automated synchronization
* Test ArgoCD self-healing capabilities

---

# 🛠️ Technologies Used

* Amazon EKS
* Kubernetes
* ArgoCD
* GitHub
* GitHub Actions
* Terraform
* Docker
* Spring Boot

---

# 🔄 GitOps Workflow

```text
Developer
    │
Git Push
    │
GitHub Repository
    │
GitHub Actions CI
(Build • Test • Docker Image)
    │
Update Kubernetes Manifests
    │
ArgoCD
    │
Continuous Sync
    │
Amazon EKS Cluster
```

---

# ⚙️ What I Explored

* GitOps Principles
* ArgoCD Dashboard
* Application Manifest
* Automated Sync
* Self-Healing
* Drift Detection
* Git as the Single Source of Truth

---

# 🔍 GitOps vs Traditional CI/CD

| Traditional CI/CD          | GitOps                        |
| -------------------------- | ----------------------------- |
| Pipeline pushes changes    | ArgoCD pulls changes          |
| Manual kubectl apply       | Automatic synchronization     |
| Manual rollback            | Git revert                    |
| Limited drift detection    | Continuous reconciliation     |
| CI requires cluster access | ArgoCD manages cluster access |

---

# 🧩 ArgoCD Features

* Automatic Synchronization
* Continuous Reconciliation
* Self-Healing
* Drift Detection
* Automatic Namespace Creation
* Resource Pruning
* Visual Resource Tree
* Sync History

---

# 🧪 Self-Healing Tests

During the lab I explored how ArgoCD restores the desired state by:

* Scaling deployments manually
* Deleting Kubernetes resources
* Modifying configuration

ArgoCD detects configuration drift and automatically reconciles the cluster back to the state defined in Git.

---

# 📚 Key Learnings

* Git becomes the single source of truth.
* Every infrastructure change should happen through Git commits.
* ArgoCD continuously watches repositories for changes.
* Manual cluster modifications are automatically corrected through reconciliation.
* GitOps improves reliability, consistency, and auditability.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Follow the repository to explore my complete DevOps learning journey.
