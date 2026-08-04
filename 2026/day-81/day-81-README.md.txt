# 🚀 Day 81 – Introduction to Amazon EKS with Terraform

## 📖 Overview

Day 81 marks the beginning of my **Amazon EKS (Elastic Kubernetes Service)** journey in the **#90DaysOfDevOps** challenge.

After building Kubernetes clusters locally with Kind, I explored how to provision a **production-grade Kubernetes cluster on AWS** using **Terraform**. I studied the AI-BankApp Terraform configuration, provisioned an Amazon EKS cluster, connected with `kubectl`, and manually deployed the AI-BankApp before introducing GitOps.

---

# 🎯 Objectives

* Understand Amazon EKS architecture
* Study the AI-BankApp Terraform configuration
* Provision an EKS cluster using Terraform
* Connect to the cluster using kubectl
* Deploy AI-BankApp manually on EKS
* Understand EKS pricing and cleanup strategies

---

# 🛠️ Technologies Used

* Amazon EKS
* Terraform
* Kubernetes
* AWS CLI
* kubectl
* Helm
* ArgoCD
* Amazon VPC
* IAM
* EBS CSI Driver

---

# 🏗️ EKS Architecture

```text
Terraform
     │
     ▼
Amazon VPC
     │
 ┌───────────────┐
 │ Public Subnets│
 │ Private Subnets│
 │ Intra Subnets │
 └───────────────┘
     │
     ▼
Amazon EKS Cluster
     │
Managed Node Group
     │
Pods
 ├── AI-BankApp
 ├── MySQL
 └── Ollama AI
```

---

# 📂 Terraform Configuration

The project Terraform configuration consists of:

* `provider.tf` → AWS & Helm providers
* `variables.tf` → Input variables
* `terraform.tfvars` → Default configuration values
* `vpc.tf` → Creates VPC and networking resources
* `eks.tf` → Deploys EKS cluster, node groups, IAM roles, and add-ons
* `argocd.tf` → Installs ArgoCD using Helm
* `outputs.tf` → Helper outputs for kubeconfig and ArgoCD

---

# ⚙️ EKS Components

The cluster includes:

* Amazon EKS Control Plane
* Managed Node Group
* Amazon VPC
* Public, Private & Intra Subnets
* NAT Gateway
* Internet Gateway
* IAM Roles
* ArgoCD

---

# 📦 Installed EKS Add-ons

* CoreDNS
* kube-proxy
* AWS VPC CNI
* EBS CSI Driver
* Metrics Server
* EKS Pod Identity Agent

---

# 🚀 Deployment Workflow

```text
Terraform Init
      │
Terraform Plan
      │
Terraform Apply
      │
Amazon EKS Cluster
      │
aws eks update-kubeconfig
      │
kubectl
      │
Deploy AI-BankApp
```

---

# 📋 Commands Practiced

```bash
terraform init
terraform plan
terraform apply
aws eks update-kubeconfig
kubectl get nodes
kubectl get pods -A
kubectl top nodes
terraform destroy
```

---

# 💰 EKS Cost Awareness

Major cost components include:

* EKS Control Plane
* EC2 Managed Node Group
* NAT Gateway
* Elastic Load Balancer
* Amazon EBS Volumes

One important learning was that the **NAT Gateway can become one of the most expensive resources** if left running continuously, making proper cleanup essential.

---

# 📚 Key Learnings

* Amazon EKS provides a fully managed Kubernetes control plane.
* Terraform makes cluster provisioning reproducible and consistent.
* Managed Node Groups simplify node lifecycle management.
* Kubernetes add-ons extend cluster functionality with minimal effort.
* ArgoCD can be installed during cluster provisioning using Terraform.
* Always destroy unused cloud resources to avoid unnecessary costs.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Follow the repository to track my complete DevOps learning journey.
