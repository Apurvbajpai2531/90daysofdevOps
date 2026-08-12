# Day 89 — Production AI Agents: KubeHealer & AIOps

## 🚀 Overview

Today I built and explored **KubeHealer**, a production-oriented AI agent for Kubernetes operations.

The agent can:

* 🔍 Scan Kubernetes for unhealthy pods
* 🧠 Diagnose root causes using Claude
* 🛠️ Propose remediation actions
* 👤 Ask for human approval before applying fixes
* ⚡ Apply targeted Kubernetes fixes
* 🔄 Recover from worker crashes using Temporal
* 📜 Maintain a complete workflow audit trail

This demonstrates **AIOps — AI-powered operations**: a system that can observe, reason, and act instead of simply displaying alerts.

---

## 🧠 What is AIOps?

AIOps applies AI to IT operations such as:

* Monitoring
* Diagnosis
* Root-cause analysis
* Remediation
* Incident response

The goal is not to completely replace engineers. Instead, AI handles repetitive operational problems while humans remain responsible for complex and potentially destructive decisions.

---

## 🛡️ Production Guardrails

Production AI agents need strong safety controls.

| Guardrail              | Purpose                                         |
| ---------------------- | ----------------------------------------------- |
| Human Approval         | Prevents destructive changes without permission |
| Scope Limits           | Restricts the agent to allowed resources        |
| Audit Trail            | Records every decision and tool call            |
| Rollback Capability    | Keeps changes reversible                        |
| Timeout & Retry Limits | Prevents infinite loops                         |
| Escalation Path        | Hands complex issues back to humans             |

KubeHealer demonstrates these principles through approval-based remediation and Temporal workflow history.

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │       User          │
                    │   Approval / Input  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Temporal Workflow │
                    │   KubeHealer Agent  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                ▼              ▼              ▼
          Scan Pods       Diagnose        Propose Fix
                │              │              │
                └──────────────┼──────────────┘
                               ▼
                        ┌─────────────┐
                        │ Claude LLM  │
                        └──────┬──────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Human Approval      │
                    │     yes / no        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Kubernetes API      │
                    │ kubectl patch/fix   │
                    └─────────────────────┘
```

---

## ☸️ Kubernetes Failure Lab

Three intentionally broken applications were deployed.

### 1. Image Typo

```text
ngnix:latest
```

instead of:

```text
nginx:latest
```

Result:

```text
ImagePullBackOff
```

KubeHealer identifies the image typo and proposes the correct image.

### 2. OOM Crash

The application was given an extremely low memory limit:

```yaml
resources:
  limits:
    memory: "1Mi"
```

Result:

```text
OOMKilled
CrashLoopBackOff
```

The agent proposes increasing the memory limit.

### 3. Missing ConfigMap

The application references:

```text
app-config
```

but the ConfigMap does not exist.

Result:

```text
CreateContainerConfigError
```

The important part is that KubeHealer **does not blindly create arbitrary resources**. It identifies the problem and escalates it for human intervention.

---

## 🔄 KubeHealer Workflow

The healing process follows:

```text
1. Scan
   ↓
2. Find unhealthy pods
   ↓
3. Collect pod details/events
   ↓
4. Send information to Claude
   ↓
5. Diagnose root cause
   ↓
6. Generate remediation plan
   ↓
7. Request human approval
   ↓
8. Apply safe fixes
   ↓
9. Verify Kubernetes state
```

---

## ⚡ Temporal Crash Recovery

One of the most important concepts was **durable execution**.

A traditional Python script can lose its state if the process crashes during an operation.

Temporal records workflow progress.

```text
Scan
  ↓
Diagnose
  ↓
Worker crashes ❌
  ↓
Worker restarted
  ↓
Temporal replays completed activities
  ↓
Workflow resumes
  ↓
Apply remaining fix
```

This means the workflow does not simply start from the beginning after a worker failure.

---

## 🧪 Crash Recovery Experiment

I tested the workflow by:

1. Starting KubeHealer
2. Deploying broken applications
3. Starting the healing workflow
4. Killing the Temporal worker during diagnosis
5. Restarting the worker
6. Observing the workflow resume

Temporal maintains the workflow history and allows the agent to continue from the interrupted point.

---

## 🤖 AI Agents vs Traditional Automation

| AI Agents                    | Traditional Automation         |
| ---------------------------- | ------------------------------ |
| Unknown problems             | Known problems                 |
| Multiple possible causes     | Fixed cause                    |
| Requires reasoning           | Deterministic logic            |
| Root-cause analysis          | If/then workflows              |
| Natural-language interaction | Predefined commands            |
| Troubleshooting              | Scaling / restart / deployment |

### Simple rule

```text
Known problem → Automation

Unknown / ambiguous problem → AI Agent
```

---

## 🔗 Connection With Previous DevOps Topics

The project combines concepts from across the 90 Days of DevOps challenge:

```text
Docker
   ↓
GitHub Actions
   ↓
Kubernetes
   ↓
Observability
   ↓
ArgoCD
   ↓
AI Agents
   ↓
AIOps
   ↓
KubeHealer
```

The agent can potentially use the same operational knowledge and tools learned throughout the challenge.

---

## 🧰 Tech Stack

* Python 3.10+
* Kubernetes
* Kind
* Claude
* Temporal
* kubectl
* Docker
* AI Agents
* AIOps

---

## 🚀 Setup

Clone the project:

```bash
git clone https://github.com/TrainWithShubham/kubehealer.git
cd kubehealer
```

Create the Kubernetes cluster:

```bash
kind create cluster --name kubehealer-demo
```

Start Temporal:

```bash
temporal server start-dev
```

Create Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure the Anthropic API key:

```bash
export ANTHROPIC_API_KEY="your-api-key"
```

Start the worker:

```bash
python3 worker.py
```

Run the healing workflow:

```bash
python3 starter.py
```

---

## 📊 Key Learnings

1. AI agents need **guardrails** before operating infrastructure.
2. Human approval is important for potentially destructive actions.
3. Temporal provides **durable execution** for agent workflows.
4. Agents should have a limited and well-defined toolset.
5. Not every problem should be automatically fixed.
6. Good agents should know when to **escalate**.
7. AI is most valuable when problems require reasoning rather than simple deterministic automation.

---

## 🧹 Cleanup

```bash
kind delete cluster --name kubehealer-demo
```

Stop the Temporal server and deactivate the Python environment.

---

## 🔥 Final Takeaway

KubeHealer demonstrates the evolution from:

```text
LLM
 ↓
ReAct Agent
 ↓
Multi-Tool Agent
 ↓
AI-powered Kubernetes Diagnosis
 ↓
Production-grade Self-Healing Agent
 ↓
AIOps
```

The biggest lesson:

> **An AI agent that can act on infrastructure needs guardrails, durability, observability, and human control.**

#90DaysOfDevOps #DevOpsKaJosh #TrainWithShubham
