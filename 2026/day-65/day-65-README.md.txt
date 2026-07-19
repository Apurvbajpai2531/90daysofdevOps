# 🚀 TerraWeek Challenge – Day 65 | Terraform Modules: Build Reusable Infrastructure

## 📖 Overview

On Day 65, I learned one of the most powerful Terraform concepts—**Modules**.

Instead of writing all infrastructure inside a single `main.tf`, I created reusable Terraform modules that can be shared across multiple projects and environments. I also used the official AWS VPC module from the Terraform Registry to understand how production-ready infrastructure is built.

---

## 🎯 Objectives

* Understand Root & Child Modules
* Build a reusable EC2 Module
* Build a reusable Security Group Module
* Deploy multiple EC2 instances using the same module
* Use the official AWS VPC Registry Module
* Learn Module Versioning & Best Practices

---

## 🛠️ Technologies Used

* Terraform
* AWS Provider
* Amazon EC2
* Amazon VPC
* Security Groups
* Terraform Registry
* Terraform Modules

---

## 📂 Project Structure

```text
terraform-modules/
├── providers.tf
├── variables.tf
├── outputs.tf
├── main.tf
└── modules/
    ├── ec2-instance/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    │
    └── security-group/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

---

## 📚 What I Learned

### ✅ Root Module

The entry point of the Terraform project that calls child modules.

### ✅ Child Modules

Reusable Terraform components that can be invoked multiple times.

### ✅ Custom Modules Created

* EC2 Instance Module
* Security Group Module

### ✅ Terraform Registry Module

Used the official:

```text
terraform-aws-modules/vpc/aws
```

to provision a production-ready VPC.

### ✅ Module Outputs

Created outputs for:

* EC2 Instance ID
* Public IP
* Private IP
* Security Group ID

### ✅ Module Versioning

Learned different version constraints:

* `= 5.1.0`
* `~> 5.0`
* `>= 5.0, < 6.0`

---

## 🚀 Terraform Commands

```bash
terraform init
terraform init -upgrade
terraform plan
terraform apply
terraform state list
terraform destroy
```

---

## 🎯 Key Learnings

* Modules make Infrastructure as Code reusable.
* Child modules reduce duplication.
* Registry modules simplify complex infrastructure.
* Module outputs enable communication between modules.
* Version pinning ensures consistent deployments.
* Well-designed modules improve maintainability and scalability.

---

## ⭐ Module Best Practices

* Pin module versions.
* Keep modules focused on one responsibility.
* Avoid hardcoded values.
* Always expose outputs.
* Include documentation (README.md) in every module.

---

Thanks to **TrainWithShubham** for another practical Terraform learning challenge.
