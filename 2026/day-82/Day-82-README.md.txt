# 🚀 Day 82 – EKS Networking with Gateway API & Persistent Storage

## 📖 Overview

On **Day 82** of my **#90DaysOfDevOps** journey, I explored production-grade networking and storage on **Amazon EKS**.

I learned how the **Gateway API** and **Envoy Gateway** modernize Kubernetes traffic management, how **cert-manager** automates HTTPS certificates, and how **Amazon EBS** provides persistent storage for stateful workloads like MySQL and Ollama. I also understood why session persistence is critical for Spring Security applications running across multiple replicas.

---

# 🎯 Objectives

* Install and configure Envoy Gateway
* Understand Gateway API architecture
* Deploy GatewayClass, Gateway, HTTPRoute, and BackendTrafficPolicy
* Explore TLS automation using cert-manager
* Verify Amazon EBS persistent storage
* Understand session persistence and Horizontal Pod Autoscaling

---

# 🛠️ Technologies Used

* Amazon EKS
* Kubernetes Gateway API
* Envoy Gateway
* cert-manager
* Amazon EBS CSI Driver
* Helm
* Terraform
* Spring Boot
* MySQL
* Ollama AI

---

# 🏗️ Gateway API Architecture

```text
Internet
    │
AWS Network Load Balancer
    │
Gateway
    │
HTTPRoute
    │
BankApp Service
    │
Spring Boot Pods
```

---

# 🔀 Gateway API Resources

### GatewayClass

Defines which controller manages Gateway resources.

### Gateway

Creates the external load balancer and exposes HTTP/HTTPS listeners.

### HTTPRoute

Routes incoming traffic to backend services.

### BackendTrafficPolicy

Provides cookie-based session affinity so authenticated users consistently reach the same application pod.

---

# 🔐 TLS with cert-manager

Implemented:

* cert-manager installation
* Let's Encrypt ClusterIssuer
* HTTP-01 validation
* Automatic certificate renewal
* TLS termination at the Gateway

This removes the need for manually creating and renewing SSL certificates.

---

# 💾 Persistent Storage with Amazon EBS

Storage flow:

```text
StorageClass
      │
PersistentVolumeClaim
      │
PersistentVolume
      │
Amazon EBS Volume
      │
MySQL / Ollama Pod
```

Key observations:

* Dynamic volume provisioning
* gp3 StorageClass
* WaitForFirstConsumer scheduling
* ReadWriteOnce access mode
* Data persists even after pod recreation

---

# 📊 Resource Overview

| Component            | Purpose                              |
| -------------------- | ------------------------------------ |
| Gateway API          | Modern Kubernetes traffic management |
| Envoy Gateway        | Gateway controller                   |
| cert-manager         | Automatic TLS certificates           |
| EBS CSI Driver       | Persistent storage                   |
| BackendTrafficPolicy | Session persistence                  |
| HPA                  | Automatic pod scaling                |

---

# 📚 Key Learnings

* Gateway API provides a more flexible replacement for traditional Kubernetes Ingress.
* Envoy Gateway automatically provisions an AWS Network Load Balancer.
* Cookie-based session affinity keeps authenticated Spring Security sessions consistent.
* Amazon EBS volumes remain intact even if pods restart.
* cert-manager automates HTTPS certificate issuance and renewal.
* Persistent storage is essential for stateful workloads such as MySQL and Ollama.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Follow the repository to track my complete DevOps learning journey.
