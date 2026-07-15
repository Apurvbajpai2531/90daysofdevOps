# 🚀 TerraWeek Challenge – Day 61 | Introduction to Terraform & First AWS Infrastructure

## 📖 Overview

Day 61 marks the beginning of my **Infrastructure as Code (IaC)** journey with **Terraform**. Instead of manually provisioning resources through the AWS Console, I learned how to define and manage cloud infrastructure using code.

In this hands-on lab, I configured Terraform with AWS, created an Amazon S3 bucket and an EC2 instance, explored Terraform state management, modified infrastructure, and finally destroyed all resources using Terraform.

---

## 🎯 Objectives

* Understand Infrastructure as Code (IaC)
* Install and configure Terraform
* Configure AWS CLI
* Create an Amazon S3 Bucket using Terraform
* Launch an EC2 instance using Terraform
* Explore Terraform State
* Modify existing infrastructure
* Destroy infrastructure safely

---

## 🛠️ Technologies Used

* Terraform
* AWS CLI
* Amazon EC2
* Amazon S3
* Infrastructure as Code (IaC)
* Git & GitHub

---

## 📂 Project Structure

```text
day-61/
├── main.tf
├── day-61-terraform-intro.md
├── .gitignore
└── images/
    ├── terraform-apply.png
    ├── s3-bucket.png
    └── ec2-instance.png
```

---

## 🚀 Terraform Workflow

Initialize Terraform

```bash
terraform init
```

Validate configuration

```bash
terraform validate
```

Format Terraform files

```bash
terraform fmt
```

Preview execution plan

```bash
terraform plan
```

Create infrastructure

```bash
terraform apply
```

View current infrastructure

```bash
terraform show
```

List managed resources

```bash
terraform state list
```

Destroy infrastructure

```bash
terraform destroy
```

---

## 📚 Key Learnings

* Learned the fundamentals of Infrastructure as Code (IaC)
* Understood why Terraform is declarative and cloud-agnostic
* Configured Terraform with AWS CLI
* Created AWS infrastructure using code
* Explored the Terraform State file
* Learned how Terraform tracks infrastructure changes
* Modified infrastructure without recreating resources
* Destroyed AWS resources safely using Terraform

---

## 📸 Screenshots

* Terraform Apply Output
* Amazon S3 Bucket
* Amazon EC2 Instance

(Add your screenshots inside the `images/` folder.)

---

## 📖 Documentation

Detailed notes are available in:

* `day-61-terraform-intro.md`

---

## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/TerraWeekTWS

---

## 🙏 Acknowledgements

Thanks to **TrainWithShubham** for organizing the **TerraWeek Challenge** and providing a practical roadmap to learn Terraform and Infrastructure as Code.

---

### ⭐ If you found this repository helpful, don't forget to star it!
