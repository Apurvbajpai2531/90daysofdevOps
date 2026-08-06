# 🚀 Day 83 – Production Deployment of AI-BankApp on Amazon EKS

## 📖 Overview

Day 83 concludes my Amazon EKS learning block in the **#90DaysOfDevOps** challenge.

Today I deployed the complete **AI-BankApp** on **Amazon EKS**, bringing together everything learned over the past three days—from Terraform-based infrastructure provisioning to Gateway API networking, persistent storage, autoscaling, and observability.

The final deployment includes a **Spring Boot application**, **MySQL database**, **Ollama AI chatbot**, **Gateway API**, **Amazon EBS persistent storage**, **Horizontal Pod Autoscaler**, and **Prometheus + Grafana monitoring**.

---

# 🎯 Objectives

* Deploy the complete AI-BankApp stack on Amazon EKS
* Configure persistent storage using Amazon EBS
* Expose the application using Gateway API
* Enable Horizontal Pod Autoscaling (HPA)
* Monitor the application with Prometheus and Grafana
* Validate the production deployment
* Cleanly destroy all AWS resources

---

# 🛠️ Technologies Used

* Amazon EKS
* Terraform
* Kubernetes
* Gateway API
* Envoy Gateway
* Spring Boot
* MySQL
* Ollama AI
* Amazon EBS
* Prometheus
* Grafana
* Helm
* AWS CLI

---

# 🏗️ Architecture

```text
Internet
     │
AWS Network Load Balancer
     │
Gateway API (Envoy)
     │
BankApp Service
     │
Amazon EKS Cluster
     │
Managed Node Group
     │
──────────────────────────────────
│ Spring Boot AI-BankApp Pods    │
│ MySQL Database (EBS Storage)   │
│ Ollama AI (EBS Storage)        │
──────────────────────────────────
     │
Prometheus + Grafana Monitoring
```

---

# 🚀 Deployment Workflow

```text
Terraform Apply
      │
Amazon EKS Cluster
      │
Deploy MySQL
      │
Deploy Ollama
      │
Deploy AI-BankApp
      │
Configure Gateway API
      │
Enable HPA
      │
Deploy Monitoring Stack
      │
Validate Application
      │
Terraform Destroy
```

---

# 📦 Application Components

* Spring Boot AI-BankApp
* MySQL Database
* Ollama AI Chatbot
* Gateway API
* Amazon EBS Persistent Volumes
* Horizontal Pod Autoscaler
* Prometheus
* Grafana

---

# 📊 Validation Performed

* Verified all BankApp pods were healthy
* Confirmed MySQL persistent storage
* Verified Ollama model availability
* Tested Gateway API routing
* Checked HPA status
* Monitored JVM and HTTP metrics in Prometheus
* Viewed dashboards in Grafana
* Completed full application testing

---

# 📚 Key Learnings

* Amazon EKS simplifies production Kubernetes management.
* Gateway API provides modern and flexible traffic routing.
* Amazon EBS ensures persistent storage for stateful workloads.
* Horizontal Pod Autoscaler improves scalability automatically.
* Prometheus and Grafana provide complete observability.
* Infrastructure can be provisioned and removed consistently using Terraform.

---

# 💰 Cost Awareness

One of the biggest takeaways from this project was understanding the importance of resource cleanup. After validation, the entire infrastructure was removed using Terraform to avoid unnecessary AWS costs.

---

# 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Follow the repository to explore my complete DevOps learning journey.
