# 🚀 Day 75 – Log Management with Loki & Promtail

## 📖 Overview

On Day 75 of my **#90DaysOfDevOps** journey, I completed the **second pillar of Observability — Logs** by integrating **Grafana Loki** and **Promtail** into my monitoring stack.

After setting up metrics monitoring with Prometheus, Node Exporter, cAdvisor, and Grafana, I extended the observability pipeline to collect, store, and visualize Docker container logs. I also learned how to use **LogQL** to search, filter, and analyze logs directly from Grafana.

---

## 🎯 Objectives

* Understand the Logging Pipeline
* Deploy Grafana Loki
* Configure Promtail
* Collect Docker Container Logs
* Add Loki as a Grafana Datasource
* Query Logs using LogQL
* Correlate Metrics and Logs

---

## 🛠️ Tech Stack

* Grafana Loki
* Promtail
* Grafana
* Prometheus
* Docker
* Docker Compose
* LogQL
* Linux

---

## 📂 Project Structure

```text
observability-stack/
├── docker-compose.yml
├── prometheus.yml
├── loki/
│   └── loki-config.yml
├── promtail/
│   └── promtail-config.yml
├── grafana/
│   └── provisioning/
│       └── datasources/
│           └── datasources.yml
├── screenshots/
│   ├── loki-ready.png
│   ├── promtail-targets.png
│   ├── grafana-explore.png
│   ├── metrics-logs-correlation.png
│   └── docker-services.png
└── day-75-loki-promtail.md
```

---

## 🚀 Components Added

### ✅ Grafana Loki

* Log Aggregation
* Label-based Indexing
* Time-Series Log Storage
* Lightweight Architecture
* Cost-efficient Logging

### ✅ Promtail

* Docker Log Collection
* Container Discovery
* Metadata Enrichment
* Log Shipping
* Position Tracking

### ✅ Grafana

* Added Loki Datasource
* Explore Mode
* Logs Visualization
* Metrics + Logs Correlation
* Unified Observability Dashboard

---

## 📊 Logging Architecture

```text
Docker Containers
        │
        ▼
    Promtail
        │
        ▼
       Loki
        │
        ▼
     Grafana
        │
        ▼
 Metrics + Logs Correlation
```

---

## 🔍 LogQL Queries Practiced

```logql
{job="docker"}

{container_name="notes-app"}

{job="docker"} |= "error"

count_over_time({job="docker"}[5m])

topk(5, sum by(container_name) (rate({job="docker"}[5m])))
```

---

## 📚 Key Learnings

* Metrics tell **what** is happening.
* Logs explain **why** it happened.
* Loki indexes labels instead of complete log content.
* Promtail automatically discovers and ships Docker logs.
* LogQL enables fast log searching and filtering.
* Grafana combines metrics and logs into a single troubleshooting interface.

---

## ⚖️ Loki vs ELK Stack

| Loki                                  | ELK                          |
| ------------------------------------- | ---------------------------- |
| Indexes only labels                   | Indexes complete log text    |
| Lightweight                           | Resource intensive           |
| Lower storage cost                    | Higher storage cost          |
| Optimized for Kubernetes & Prometheus | Powerful full-text search    |
| Easy Grafana integration              | Separate visualization stack |

---


## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ If you found this project helpful, feel free to Star the repository.

Happy Learning! 🚀
