# Day 77 – Observability Project: Full Stack with Docker Compose 🚀

## 📌 Overview

Today marked the completion of the 5-day Observability learning block in the **#90DaysOfDevOps** challenge.

I deployed a complete production-style observability stack using Docker Compose, integrating **Prometheus, Grafana, Loki, Promtail, OpenTelemetry Collector, Node Exporter, cAdvisor, and a sample Notes application** into a single monitoring platform.

The project demonstrates how metrics, logs, traces, and alerting work together to provide complete visibility into modern applications.

---

# 🎯 Objectives

- Deploy the complete observability stack
- Validate Metrics, Logs, and Traces
- Configure Prometheus monitoring
- Explore logs using Loki
- Validate OpenTelemetry traces
- Build a unified Grafana dashboard
- Compare custom configurations with the reference repository
- Document a production-ready observability architecture

---

# 🏗️ Project Architecture

```
                     METRICS
Node Exporter ─┐
               │
cAdvisor ──────┼────────► Prometheus ─────► Grafana Dashboards
               │                │
OTEL Collector ┘                ▼
                          Alert Rules

------------------------------------------------------

                      LOGS

Docker Containers
        │
        ▼
    Promtail
        │
        ▼
      Loki
        │
        ▼
     Grafana Explore

------------------------------------------------------

                    TRACES

Application
      │
 OTLP (4317 / 4318)
      │
      ▼
OTEL Collector
      │
      ▼
Debug Exporter
(Future → Grafana Tempo / Jaeger)
```

---

# 🛠️ Technology Stack

- Docker Compose
- Prometheus
- Grafana
- Node Exporter
- cAdvisor
- Loki
- Promtail
- OpenTelemetry Collector
- OTLP
- PromQL
- LogQL

---

# 🚀 Services Running

| Service | Port | Purpose |
|----------|------|----------|
| Prometheus | 9090 | Metrics Storage |
| Grafana | 3000 | Dashboards & Alerting |
| Node Exporter | 9100 | Host Metrics |
| cAdvisor | 8080 | Container Metrics |
| Loki | 3100 | Log Storage |
| Promtail | 9080 | Log Collection |
| OTEL Collector | 4317 / 4318 / 8889 | Telemetry Collection |
| Notes App | 8000 | Sample Application |

---

# 📊 Metrics Validation

Validated Prometheus targets:

- ✅ Prometheus
- ✅ Node Exporter
- ✅ cAdvisor
- ✅ OTEL Collector

Key PromQL Queries:

- CPU Usage
- Memory Usage
- Container CPU
- Top Memory Consumers
- Healthy Targets

---

# 📜 Logs Validation

Using Loki + Promtail:

- Container Logs
- Notes App Logs
- Error Logs
- HTTP GET Requests
- Log Rate per Container

LogQL was used to filter and analyze application logs directly inside Grafana Explore.

---

# 🔍 Trace Validation

Validated OpenTelemetry pipeline by sending OTLP traces.

Verified:

- Trace ID
- Span ID
- Parent Span
- HTTP Route
- Database Span
- Status Code

---

# 🚨 Alerting

Configured:

### Prometheus Alerts

- High CPU Usage
- High Memory Usage
- High Disk Usage
- Container Down
- Target Down

### Grafana Alerts

- Contact Points
- Notification Policies
- Container Memory Alert

---

# 📈 Production Overview Dashboard

Created a unified Grafana dashboard including:

### System Health

- CPU Usage
- Memory Usage
- Disk Usage
- Targets Up

### Container Metrics

- CPU Usage
- Memory Usage
- Running Containers

### Application Logs

- Notes App Logs
- Error Rate
- Log Volume

### Service Overview

- Prometheus Scrape Duration
- OTEL Metrics

---

# 📚 Comparison with Previous Days

| Day | Learning |
|-----|----------|
| Day 73 | Prometheus & Metrics |
| Day 74 | Grafana, Node Exporter & cAdvisor |
| Day 75 | Loki, Promtail & LogQL |
| Day 76 | OpenTelemetry & Alerting |
| Day 77 | Full Stack Observability |

---

# 🚀 Production Improvements

Future enhancements include:

- Alertmanager Integration
- Grafana Tempo for Trace Storage
- HTTPS/TLS
- Authentication
- High Availability
- Long-Term Storage
- Log Retention Policies

---

# 💡 Key Learnings

- Built a complete cloud-native observability platform.
- Integrated Metrics, Logs, and Traces into a unified monitoring solution.
- Learned end-to-end telemetry collection with OpenTelemetry.
- Created production-style dashboards and alerting workflows.
- Understood how modern DevOps teams monitor infrastructure and applications.

---

# 📂 Repository

**GitHub Repository**

https://github.com/Apurvbajpai2531/90daysofdevOps

---

## ✅ Day 77 Complete

Successfully deployed and validated a production-style observability stack using Docker Compose, integrating Metrics, Logs, Traces, Dashboards, and Alerting into one unified platform.