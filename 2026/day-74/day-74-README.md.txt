# 🚀 Day 74 – Node Exporter, cAdvisor & Grafana Dashboards

## 📖 Overview

On Day 74 of my **#90DaysOfDevOps** journey, I expanded my observability stack by integrating **Node Exporter**, **cAdvisor**, and **Grafana** with Prometheus.

This setup enables monitoring of both **host-level metrics** (CPU, memory, disk, network) and **container-level metrics**, while Grafana transforms raw Prometheus metrics into interactive dashboards for real-time infrastructure visibility.

---

## 🎯 Objectives

* Monitor Host Metrics using Node Exporter
* Monitor Docker Containers using cAdvisor
* Integrate Grafana with Prometheus
* Build Custom Dashboards
* Import Community Dashboards
* Automate Datasource Provisioning

---

## 🛠️ Tech Stack

* Prometheus
* Grafana
* Node Exporter
* cAdvisor
* Docker
* Docker Compose
* PromQL
* Linux

---

## 📂 Project Structure

```text
observability-stack/
├── docker-compose.yml
├── prometheus.yml
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       │   └── datasources.yml
│       └── dashboards/
├── screenshots/
│   ├── prometheus-targets.png
│   ├── grafana-dashboard.png
│   ├── node-exporter-dashboard.png
│   └── cadvisor-metrics.png
└── day-74-exporters-grafana.md
```

---

## 🚀 Components Added

### ✅ Node Exporter

Collected Linux host metrics:

* CPU Usage
* Memory Usage
* Disk Usage
* Filesystem Metrics
* Network Statistics

### ✅ cAdvisor

Collected Docker container metrics:

* Container CPU Usage
* Container Memory Usage
* Network Traffic
* Filesystem Usage
* Running Containers

### ✅ Grafana

* Connected Prometheus as a datasource
* Created custom dashboards
* Imported **Node Exporter Full (Dashboard ID: 1860)**
* Imported Docker monitoring dashboards
* Provisioned datasources automatically using YAML

---

## 📊 Architecture

```text
Application
        │
        ▼
 Prometheus
   ▲      ▲
   │      │
Node Exporter   cAdvisor
   │             │
Host Metrics   Container Metrics
        │
        ▼
     Grafana
 Interactive Dashboards
```

---

## 🔍 PromQL Queries Used

```promql
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100

(1 - node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100

rate(container_cpu_usage_seconds_total{name!=""}[5m])

container_memory_usage_bytes{name!=""}
```

---

## 🎯 Key Learnings

* Node Exporter monitors the Linux host.
* cAdvisor monitors Docker containers.
* Grafana converts metrics into meaningful dashboards.
* Datasource provisioning makes deployments repeatable.
* PromQL powers advanced metric analysis and visualization.

---
## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ If you find this repository useful, feel free to give it a Star.

Happy Learning! 🚀
