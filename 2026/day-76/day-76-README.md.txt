# Day 76 – OpenTelemetry & Alerting | 90 Days of DevOps 🚀

## 📌 Overview

Today I completed one of the most important parts of the Observability journey by adding the **third pillar – Distributed Tracing** using **OpenTelemetry (OTEL)** and implementing **alerting** using both **Prometheus** and **Grafana**.

The observability stack now includes:

- ✅ Metrics (Prometheus)
- ✅ Logs (Loki + Promtail)
- ✅ Traces (OpenTelemetry)
- ✅ Alerting (Prometheus + Grafana)

This completes a modern cloud-native monitoring stack.

---

# 🎯 Objectives

- Learn OpenTelemetry architecture
- Configure OTEL Collector
- Send OTLP Metrics & Traces
- Export metrics to Prometheus
- Configure Prometheus Alert Rules
- Create Grafana Alert Rules
- Configure Notification Contact Points
- Understand the Three Pillars of Observability

---

# 🏗️ OpenTelemetry Architecture

OpenTelemetry is an open-source, vendor-neutral observability framework used to collect telemetry data.

It supports:

- Metrics
- Logs
- Traces

Unlike Prometheus or Loki, OpenTelemetry is **not a storage backend**. It only collects and exports telemetry.

---

# OTEL Collector Pipeline

```
Applications
      │
      ▼
Receivers
      │
      ▼
Processors
      │
      ▼
Exporters
      │
      ├────────► Prometheus
      ├────────► Jaeger
      ├────────► Tempo
      ├────────► Debug
      └────────► Datadog
```

---

# Components

## Receivers

Receive telemetry from applications.

Examples:

- OTLP
- Prometheus
- Jaeger
- Zipkin

---

## Processors

Modify telemetry before exporting.

Examples:

- Batch
- Filter
- Sampling

---

## Exporters

Send telemetry to external systems.

Examples:

- Prometheus
- Loki
- Tempo
- Jaeger
- Debug Console

---

# What is OTLP?

OTLP (OpenTelemetry Protocol) is the standard protocol for transferring telemetry.

Supported protocols:

- gRPC → Port **4317**
- HTTP → Port **4318**

---

# Distributed Tracing

A trace follows a request across multiple services.

Example:

```
Client
   │
   ▼
API Gateway
   │
   ▼
Authentication Service
   │
   ▼
Database
```

Each operation is represented by a **Span**.

Each span contains:

- Trace ID
- Span ID
- Parent Span ID
- Duration
- Timestamp
- Attributes

---

# OTEL Collector Configuration

Created:

```
otel-collector/
    otel-collector-config.yml
```

Configuration includes:

## Receivers

- OTLP gRPC
- OTLP HTTP

## Processor

- Batch Processor

## Exporters

- Prometheus Exporter
- Debug Exporter

---

# Docker Compose Integration

Added:

```
otel-collector:
    image: otel/opentelemetry-collector-contrib
```

Ports:

| Port | Purpose |
|------|----------|
|4317|OTLP gRPC|
|4318|OTLP HTTP|
|8889|Prometheus Metrics|

---

# Prometheus Integration

Added new scrape job:

```
job_name: otel-collector
```

Target:

```
otel-collector:8889
```

Now Prometheus automatically scrapes OTEL metrics.

---

# Sending Test Traces

Sent sample traces using:

```
curl
```

Verified through:

```
docker logs otel-collector
```

Observed:

- Trace ID
- Span ID
- Service Name
- HTTP Method
- Status Code

---

# Sending Metrics

Sent OTLP Metrics.

Verified in Prometheus:

```
test_requests_total
```

Pipeline:

```
Application
      │
      ▼
OTEL Collector
      │
      ▼
Prometheus Exporter
      │
      ▼
Prometheus
      │
      ▼
Grafana
```

---

# Prometheus Alert Rules

Configured alerts for:

✅ High CPU Usage

✅ High Memory Usage

✅ High Disk Usage

✅ Target Down

✅ Container Down

Each alert contains:

- Expression
- Duration
- Severity
- Summary
- Description

---

# Grafana Alerting

Configured:

- Contact Point
- Notification Policy
- Alert Rule

Example:

```
Container Memory >100 MB
```

Evaluation:

```
Every 1 minute
For 2 minutes
```

---

# Prometheus Alerts vs Grafana Alerts

| Prometheus | Grafana |
|------------|----------|
|Evaluates PromQL Rules|Can evaluate PromQL and other data sources|
|Requires Alertmanager for notifications|Built-in notifications|
|Simple and lightweight|Rich UI and integrations|
|Best for infrastructure alerts|Best for dashboards and visualization|

---

# Complete Observability Architecture

```
                METRICS
Node Exporter
        │
cAdvisor
        │
OTEL Collector
        │
        ▼
   Prometheus
        │
        ▼
    Grafana
        │
        ▼
     Alerts

------------------------------

                 LOGS

Containers
     │
Promtail
     │
Loki
     │
Grafana

------------------------------

                TRACES

Application
      │
OTLP
      │
OTEL Collector
      │
Debug Exporter
(Production → Tempo / Jaeger)
```

---

# Services Running

| Service | Port |
|----------|------|
|Grafana|3000|
|Prometheus|9090|
|Node Exporter|9100|
|cAdvisor|8080|
|Loki|3100|
|Promtail|9080|
|OTEL Collector|4317 / 4318 / 8889|
|Notes App|8000|

---

# Key Learnings

- OpenTelemetry standardizes telemetry collection.
- OTEL Collector acts as a telemetry pipeline.
- OTLP is the standard telemetry protocol.
- Distributed tracing helps debug microservices.
- Prometheus alerting detects infrastructure failures.
- Grafana alerting delivers notifications.
- Observability consists of Metrics, Logs, and Traces working together.

---

# Repository

🔗 **GitHub Repository**

https://github.com/Apurvbajpai2531/90daysofdevOps

---

# Screenshots

- OTEL Collector Running
- Prometheus Targets
- Trace Debug Logs
- Prometheus Alerts
- Grafana Alert Rules
- Full Architecture Diagram

---

## 🚀 Day 76 Complete

Successfully added OpenTelemetry and Alerting to build a complete cloud-native observability stack.