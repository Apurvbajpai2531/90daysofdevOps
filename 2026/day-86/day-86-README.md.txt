# 🚀 Day 86 – GitOps Project: End-to-End CI/CD Pipeline with AI-BankApp

## 📖 Overview

Day 86 brings the **GitOps block** together into a complete end-to-end CI/CD pipeline.

A developer pushes a code change to GitHub. **GitHub Actions** builds and tests the application, creates and pushes a Docker image, updates the Kubernetes deployment manifest with the Git commit SHA, and commits that change back to Git. **ArgoCD** detects the new desired state and automatically synchronizes it to **Amazon EKS**.

The result is a fully automated path from **code change to Kubernetes deployment**, with Git remaining the source of truth.

---

## 🏗️ End-to-End GitOps Pipeline

```text
Developer
    │
    │ git push
    ▼
GitHub
    │
    ▼
GitHub Actions
    │
    ├── Checkout
    ├── Setup JDK 21
    ├── Maven Build
    ├── Run Tests
    ├── Build Docker Image
    ├── Push Image → DockerHub
    ├── Update Kubernetes Manifest
    └── Commit Manifest [skip ci]
    │
    ▼
Git Repository
    │
    ▼
ArgoCD
    │
    ├── Detect Git change
    ├── Compare desired vs live state
    ├── Sync
    └── Rolling Update
    │
    ▼
Amazon EKS
    │
    └── AI-BankApp
```

The GitHub Actions → ArgoCD handoff is the critical part: Actions commits the new image tag into Git, ArgoCD detects the change, and then synchronizes the cluster.

---

# ⚙️ GitHub Actions CI Pipeline

The workflow runs when application code changes on the `feat/gitops` branch, including changes under `src/`, `pom.xml`, or `Dockerfile`. It can also be started manually with `workflow_dispatch`.

### Pipeline Steps

| Step            | What happens                           |
| --------------- | -------------------------------------- |
| Checkout        | Clone repository                       |
| JDK 21          | Configure Java + Maven cache           |
| Maven Build     | Package application                    |
| Tests           | Run Maven tests                        |
| Image Tag       | Generate short Git SHA                 |
| DockerHub Login | Authenticate using secrets             |
| Build & Push    | Push Docker image                      |
| Update Manifest | Replace Kubernetes image tag           |
| Commit          | Push updated manifest with `[skip ci]` |

The image is tagged using the short Git commit SHA, providing traceability between a running container and the source-code revision.

---

# 🐳 Docker Image Strategy

The pipeline publishes:

```text
<dockerhub-username>/ai-bankapp-eks:latest
<dockerhub-username>/ai-bankapp-eks:<git-sha>
```

The Git SHA gives every deployment a unique, traceable version.

Example:

```text
Git Commit
   │
   └── 1c7cb0e
          │
          ▼
Docker Image
ai-bankapp-eks:1c7cb0e
```

---

# 🔄 Automatic Manifest Update

After building the image, GitHub Actions updates:

```text
k8s/bankapp-deployment.yml
```

The workflow replaces the existing image tag with the latest Git SHA and commits the change back to the repository.

The commit uses:

```text
[skip ci]
```

This prevents the manifest-update commit from triggering the CI pipeline again and creating an infinite loop.

---

# ☸️ ArgoCD Deployment

After the manifest changes in Git:

```text
GitHub Actions
      │
      ▼
Updated Kubernetes Manifest
      │
      ▼
ArgoCD detects commit
      │
      ▼
Desired State ≠ Live State
      │
      ▼
ArgoCD Sync
      │
      ▼
Rolling Update
      │
      ▼
New AI-BankApp Pods
```

ArgoCD performs the deployment automatically, without requiring a manual `kubectl apply`.

---

# 🔐 GitHub Secrets

The pipeline uses GitHub Actions secrets for DockerHub authentication:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
```

These should be configured under:

```text
Repository
 → Settings
 → Secrets and variables
 → Actions
```

The Docker repository is then configured in the workflow.

---

# 🧪 Full GitOps Cycle

A complete deployment follows:

```text
Code Change
    ↓
git push
    ↓
GitHub Actions
    ↓
Build + Test
    ↓
Docker Image
    ↓
DockerHub
    ↓
Update K8s Manifest
    ↓
Git Commit
    ↓
ArgoCD
    ↓
EKS
    ↓
Rolling Deployment
```

This provides an automated code-to-production workflow with no manual deployment step.

---

# 🛡️ Drift Detection & Self-Healing

I also explored what happens when someone manually changes the Kubernetes cluster.

### Scenario 1 — Scale Deployment

```bash
kubectl scale deployment bankapp -n bankapp --replicas=1
```

ArgoCD detects that the live state differs from Git and restores the desired replica count when self-healing is enabled.

### Scenario 2 — Change Image

```bash
kubectl set image deployment/bankapp bankapp=nginx:latest -n bankapp
```

ArgoCD detects the unauthorized image change and restores the image defined in Git.

### Scenario 3 — Delete Service

```bash
kubectl delete service bankapp-service -n bankapp
```

ArgoCD recreates the resource from the Git-defined desired state.

---

# 🔁 Rollback Strategy

Two approaches are available:

### ArgoCD Rollback

Useful for quickly restoring a previous live revision.

### Git Revert

The preferred GitOps approach because the desired state in Git is also reverted.

```text
git revert
     ↓
Git Repository
     ↓
ArgoCD detects change
     ↓
Cluster reconciled
```

This maintains a clear Git-based audit trail.

---

# 🌐 Complete DevOps Journey

This project connects multiple concepts learned throughout the challenge:

```text
Git & GitHub
     ↓
GitHub Actions
     ↓
Docker
     ↓
DockerHub
     ↓
Kubernetes
     ↓
Helm
     ↓
Amazon EKS
     ↓
ArgoCD / GitOps
     ↓
Prometheus + Grafana
     ↓
Production Application
```

Each block builds on the previous one, creating a complete modern DevOps workflow.

---

# 📚 Key Learnings

* CI builds and validates application changes.
* Docker packages the application into a portable image.
* Git stores the desired Kubernetes state.
* ArgoCD continuously reconciles Kubernetes with Git.
* Git SHA image tags provide deployment traceability.
* `[skip ci]` prevents CI loops.
* Self-healing protects against manual configuration drift.
* Git provides an auditable deployment history.
* Kubernetes rolling updates enable zero-downtime deployments.

---

# 🧹 Teardown

After completing the lab, all resources were cleaned up.

ArgoCD applications should be deleted with cascade enabled so their managed Kubernetes resources are also removed. The EKS infrastructure can then be destroyed using Terraform.

```bash
argocd app delete bankapp --cascade -y

cd AI-BankApp-DevOps/terraform

terraform destroy
```

---

# 🔗 GitHub Repository

https://github.com/Apurvbajpai2531/90daysofdevOps

---

## 🎯 Final Takeaway

**GitOps = Git as Source of Truth + CI Automation + ArgoCD Reconciliation + Kubernetes**

The complete pipeline now looks like:

```text
Developer
   ↓
GitHub
   ↓
GitHub Actions
   ↓
DockerHub
   ↓
Git Manifest
   ↓
ArgoCD
   ↓
Amazon EKS
   ↓
AI-BankApp
```

**Zero manual deployments. Full audit trail. Automated reconciliation. Self-healing infrastructure.**
