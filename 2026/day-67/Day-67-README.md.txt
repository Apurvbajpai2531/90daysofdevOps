# 🚀 TerraWeek Challenge – Day 67 | Multi-Environment Infrastructure with Terraform Workspaces & Modules

## 📖 Overview

Day 67 was the **TerraWeek Capstone Project**, where I combined everything learned throughout the week into a production-style Infrastructure as Code project.

Using **Terraform Workspaces**, **Custom Modules**, and **AWS Infrastructure**, I built a reusable codebase capable of deploying **three completely isolated environments (Development, Staging, and Production)** from the same Terraform project.

---

## 🎯 Objectives

* Build reusable Terraform Modules
* Deploy multiple isolated environments
* Use Terraform Workspaces
* Reuse one codebase across Dev, Staging & Production
* Follow Infrastructure as Code best practices
* Destroy all resources safely

---

## 🛠️ Technologies Used

* Terraform
* AWS EC2
* Amazon VPC
* Security Groups
* Internet Gateway
* Terraform Workspaces
* Terraform Modules
* AWS Provider

---

## 📂 Project Structure

```text
terraweek-capstone/
├── providers.tf
├── variables.tf
├── locals.tf
├── main.tf
├── outputs.tf
├── dev.tfvars
├── staging.tfvars
├── prod.tfvars
├── .gitignore
└── modules/
    ├── vpc/
    ├── security-group/
    └── ec2-instance/
```

---

## 🚀 Infrastructure Created

Each workspace deployed its own isolated infrastructure:

### Development

* VPC (10.0.0.0/16)
* Public Subnet
* Security Group
* EC2 (t2.micro)

### Staging

* VPC (10.1.0.0/16)
* Public Subnet
* Security Group
* EC2 (t2.small)

### Production

* VPC (10.2.0.0/16)
* Public Subnet
* Security Group
* EC2 (t3.small)

---

## 📚 Terraform Concepts Covered

* Terraform Workspaces
* Custom Modules
* Variables
* Outputs
* Locals
* Dynamic Security Groups
* Workspace-aware Infrastructure
* Environment Isolation
* Infrastructure as Code Best Practices

---

## 💻 Commands Used

```bash
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

terraform workspace select dev
terraform apply -var-file="dev.tfvars"

terraform workspace select staging
terraform apply -var-file="staging.tfvars"

terraform workspace select prod
terraform apply -var-file="prod.tfvars"

terraform destroy
```

---

## 🎯 Key Learnings

* One codebase can manage multiple environments.
* Workspaces isolate Terraform state.
* Modules eliminate duplicate code.
* Different environments can use different infrastructure sizes.
* Proper tagging and naming improve maintainability.
* Infrastructure becomes scalable, reusable, and production-ready.

## 📖 TerraWeek Recap

| Day    | Topic                                       |
| ------ | ------------------------------------------- |
| Day 61 | Terraform Basics                            |
| Day 62 | Providers & Resources                       |
| Day 63 | Variables, Outputs & Data Sources           |
| Day 64 | State Management                            |
| Day 65 | Terraform Modules                           |
| Day 66 | Amazon EKS with Terraform                   |
| Day 67 | Multi-Environment Infrastructure (Capstone) |

---

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/TerraWeekTWS

---

## 🙏 Acknowledgements

A huge thanks to **TrainWithShubham** and the **TerraWeek Challenge** for providing an incredible hands-on learning journey into Terraform and Infrastructure as Code.

⭐ If you found this project useful, consider giving the repository a **Star**.
