# 🚀 Day 73 – Introduction to Observability & Prometheus

## 📖 Overview

Day 73 marks the beginning of the **Observability** journey in the **#90DaysOfDevOps** challenge.

After provisioning infrastructure with Terraform, configuring servers using Ansible, and deploying applications with Docker, the next step is understanding **how to monitor and troubleshoot running systems**.

In this project, I explored the fundamentals of **Observability**, learned the **three pillars (Metrics, Logs, and Traces)**, deployed **Prometheus** using Docker, configured scrape targets, and wrote my first **PromQL** queries.

---

## 🎯 Objectives

* Understand Observability
* Compare Monitoring vs Observability
* Learn the Three Pillars
* Deploy Prometheus using Docker
* Configure Scrape Targets
* Write PromQL Queries
* Monitor Applications

---

## 🛠️ Tech Stack

* Prometheus
* Docker
* Docker Compose
* PromQL
* Linux
* YAML

---

## 📂 Project Structure

```text
observability-stack/
├── docker-compose.yml
├── prometheus.yml
├── README.md
├── screenshots/
│   ├── targets.png
│   ├── graph.png
│   ├── promql.png
│   └── tsdb.png
└── day-73-observability-prometheus.md
```

---

## 📚 Topics Covered

### ✅ Observability

* Monitoring vs Observability
* Metrics
* Logs
* Traces

### ✅ Prometheus

* Pull-based Monitoring
* Scrape Targets
* Time Series Database (TSDB)
* Data Retention
* Labels
* Metric Types

### ✅ PromQL

Practiced queries including:

* `up`
* `rate()`
* `sum()`
* `topk()`
* `count()`
* Memory Usage
* HTTP Request Metrics

---

## 📊 Architecture

```text
Application
      │
      ▼
 Prometheus
      │
      ▼
 Metrics Storage (TSDB)
      │
      ▼
 PromQL Queries
      │
      ▼
 Dashboards (Grafana)
```

Future Stack:

```text
Application → Prometheus → Grafana
Application → Promtail → Loki → Grafana
Application → OTEL Collector → Grafana
Host → Node Exporter → Prometheus
Docker → cAdvisor → Prometheus
```

---

## 💻 Commands Used

```bash
docker compose up -d

docker ps

docker exec prometheus du -sh /prometheus

curl http://localhost:8000
```

---

## 🔍 PromQL Queries

* `up`
* `count({__name__=~".+"})`
* `process_resident_memory_bytes`
* `rate(prometheus_http_requests_total[5m])`
* `sum(rate(prometheus_http_requests_total[5m]))`

---

## 🎯 Key Learnings

* Observability explains **why** systems fail.
* Prometheus uses a **pull model**.
* Metrics are stored as **time series**.
* PromQL enables powerful metric analysis.
* Prometheus integrates seamlessly with Grafana.

---


## 🔗 GitHub Repository

**Repository:**
https://github.com/Apurvbajpai2531/90daysofdevOps

⭐ Feel free to explore the repository and share your feedback.

Happy Learning! 🚀
