# 🚀 Day 85 – ArgoCD Deep Dive: Sync Strategies, Rollbacks & Multi-App Management

## 📖 Overview

Day 85 of my **#90DaysOfDevOps** journey was a deep dive into **ArgoCD and advanced GitOps practices**.

After deploying AI-BankApp through ArgoCD on Day 84, today I explored how production teams manage multiple Kubernetes applications using **sync strategies, sync waves, rollbacks, App of Apps, notifications, Projects, and RBAC**.

This helped me understand that GitOps is much more than simply deploying applications from Git — it is a complete operational model for managing production Kubernetes environments.

---

## 🎯 What I Learned

* Automated vs manual ArgoCD synchronization
* Previewing changes before synchronization
* Sync waves for controlling resource deployment order
* ArgoCD rollback vs `git revert`
* App of Apps pattern
* ArgoCD notifications
* Projects and RBAC for multi-team environments
* Resource pruning and self-healing

---

## 🔄 Automated vs Manual Sync

### Automated Sync

```yaml
syncPolicy:
  automated:
    prune: true
    selfHeal: true
```

With automated synchronization, ArgoCD continuously monitors Git and applies changes automatically.

### Manual Sync

```yaml
syncPolicy: {}
```

With manual sync, ArgoCD detects differences but waits for an administrator to approve and execute the synchronization.

| Feature              | Automated   | Manual     |
| -------------------- | ----------- | ---------- |
| Automatic deployment | ✅           | ❌          |
| Drift detection      | ✅           | ✅          |
| Auto self-healing    | ✅           | ❌          |
| Human approval       | ❌           | ✅          |
| Suitable for         | Dev/Staging | Production |

---

## 🌊 Sync Waves

AI-BankApp has dependencies between infrastructure, configuration, databases, and application workloads.

I used ArgoCD sync waves to control deployment order:

| Wave | Resources               | Purpose        |
| ---: | ----------------------- | -------------- |
| `-2` | Namespace, StorageClass | Infrastructure |
| `-1` | PVCs, ConfigMap, Secret | Configuration  |
|  `0` | MySQL, Ollama, Services | Dependencies   |
|  `1` | BankApp Deployment      | Application    |
|  `2` | HPA                     | Scaling        |

```text
Wave -2
   ↓
Namespace + StorageClass
   ↓
Wave -1
   ↓
PVC + ConfigMap + Secret
   ↓
Wave 0
   ↓
MySQL + Ollama + Services
   ↓
Wave 1
   ↓
BankApp
   ↓
Wave 2
   ↓
HPA
```

Resources within the same wave can be synchronized in parallel.

---

## 🔙 ArgoCD Rollback

ArgoCD maintains synchronization history, allowing applications to be rolled back to previous revisions.

```bash
argocd app history bankapp
argocd app rollback bankapp 1
```

However, an ArgoCD rollback changes the live cluster but **does not change Git**.

For a GitOps-correct rollback:

```bash
git revert HEAD
git push
```

ArgoCD then detects the Git change and synchronizes the cluster.

### Key Difference

```text
ArgoCD Rollback
        ↓
Changes cluster only

git revert
        ↓
Changes Git
        ↓
ArgoCD reconciles cluster
```

---

# 🏗️ App of Apps Pattern

Managing dozens of applications individually becomes difficult.

The **App of Apps** pattern solves this by using one parent ArgoCD Application to manage multiple child Applications.

```text
                 Root App
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
     BankApp    Monitoring   Envoy Gateway
        │           │           │
     Kubernetes   Prometheus   Gateway
     Resources    + Grafana
```

The parent application watches the `argocd-apps/` directory.

Adding a new application can be as simple as adding another Application manifest to Git.

---

## 🔔 ArgoCD Notifications

I explored notification triggers for important application events:

* Sync succeeded
* Sync failed
* Application health degraded

Example:

```yaml
trigger.on-sync-succeeded:
  - when: app.status.operationState.phase in ['Succeeded']
    send: [app-sync-succeeded]

trigger.on-sync-failed:
  - when: app.status.operationState.phase in ['Error', 'Failed']
    send: [app-sync-failed]
```

Notifications can be integrated with services such as Slack or generic webhooks.

---

# 🔐 Projects & RBAC

For production environments, every team should not have unrestricted access to every application.

ArgoCD **Projects** can restrict:

* Allowed Git repositories
* Allowed Kubernetes namespaces
* Deployment destinations

RBAC can further control operations.

Example:

```text
bankapp-developers
        │
        ├── View applications ✅
        ├── Sync applications ✅
        └── Rollback ❌
```

This provides better multi-team isolation and reduces the risk of accidental changes.

---

# 🧠 Key Learnings

### 1. Sync Waves

Control the order in which dependent resources are deployed.

### 2. Manual Sync

Useful when production deployments require an approval gate.

### 3. Rollbacks

ArgoCD can quickly restore an older cluster state, while `git revert` provides the proper GitOps audit trail.

### 4. App of Apps

A scalable pattern for managing many ArgoCD applications.

### 5. Notifications

Provide visibility when deployments succeed, fail, or become unhealthy.

### 6. Projects & RBAC

Enable controlled access for multiple teams working on the same Kubernetes platform.

---

## 🛠️ Commands Practiced

```bash
argocd app set bankapp --sync-policy none

argocd app diff bankapp

argocd app sync bankapp --dry-run

argocd app sync bankapp

argocd app history bankapp

argocd app rollback bankapp 1

argocd app list

kubectl apply -f argocd-apps/root-app.yaml

argocd app get bankapp
```

---

## 📂 Project Structure

```text
day-85/
├── day-85-argocd-deep-dive.md
└── argocd-apps/
    ├── root-app.yaml
    ├── bankapp.yaml
    ├── monitoring.yaml
    └── envoy-gateway.yaml
```

---

## 🔗 GitHub Repository

https://github.com/Apurvbajpai2531/90daysofdevOps

---

## 🚀 Final Takeaway

Day 85 showed me that **GitOps is not just "deploy from Git."**

It provides a complete operational framework covering:

```text
Git
 ↓
ArgoCD
 ↓
Sync Strategies
 ↓
Ordered Deployments
 ↓
Self-Healing
 ↓
Rollback
 ↓
Multi-App Management
 ↓
Notifications
 ↓
RBAC
 ↓
Production Kubernetes
```

#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham #GitOps #ArgoCD #Kubernetes #AWS #EKS
