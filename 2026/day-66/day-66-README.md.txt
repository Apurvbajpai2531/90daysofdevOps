# 🚀 TerraWeek Challenge – Day 66 | Provision an AWS EKS Cluster with Terraform Modules

## 📖 Overview

On Day 66 of the TerraWeek Challenge, I provisioned a fully managed **Amazon EKS (Elastic Kubernetes Service)** cluster using **Terraform Registry Modules**.

Instead of manually creating networking, IAM roles, node groups, and Kubernetes resources, everything was provisioned as Infrastructure as Code. After creating the cluster, I connected `kubectl`, deployed an Nginx application, verified the workload, and finally destroyed all resources to avoid unnecessary AWS costs.

---

## 🎯 Objectives

* Provision an AWS EKS Cluster using Terraform
* Build networking using the AWS VPC Module
* Create an EKS Managed Node Group
* Connect `kubectl` to the cluster
* Deploy an Nginx application
* Destroy all infrastructure cleanly

---

## 🛠️ Technologies Used

* Terraform
* AWS EKS
* Amazon VPC
* AWS IAM
* Amazon EC2
* kubectl
* Kubernetes
* Nginx
* Terraform Registry Modules

---

## 📂 Project Structure

```text
terraform-eks/
├── providers.tf
├── variables.tf
├── terraform.tfvars
├── vpc.tf
├── eks.tf
├── outputs.tf
├── k8s/
│   └── nginx-deployment.yaml
├── day-66-eks-terraform.md
└── images/
    ├── terraform-apply.png
    ├── kubectl-nodes.png
    ├── nginx-running.png
    └── eks-console.png
```

---

## 🚀 What I Built

* AWS VPC using the Terraform AWS VPC Module
* Public & Private Subnets
* NAT Gateway
* Amazon EKS Cluster
* Managed Node Group
* IAM Roles
* Security Groups
* Nginx Deployment
* Kubernetes LoadBalancer Service

---

## 📚 What I Learned

* Provisioning production-ready Kubernetes infrastructure with Terraform
* Using official Terraform Registry Modules
* Connecting `kubectl` to an EKS cluster
* Deploying Kubernetes workloads
* Managing AWS infrastructure as code
* Cleaning up cloud resources safely using `terraform destroy`

---

## 🔧 Commands Used

```bash
terraform init
terraform plan
terraform apply
aws eks update-kubeconfig
kubectl get nodes
kubectl get pods -A
kubectl apply -f k8s/nginx-deployment.yaml
kubectl get svc
terraform destroy
```

---



## 🎯 Key Takeaways

* Terraform modules simplify complex AWS infrastructure.
* EKS can be deployed with a single Terraform workflow.
* kubectl integrates seamlessly after kubeconfig is updated.
* Infrastructure becomes repeatable, scalable, and version-controlled.
* Always destroy cloud resources after practice to avoid unnecessary costs.

---

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofDevops

---

⭐ Thanks to **TrainWithShubham** for another hands-on DevOps learning experience.
