# 🚀 Day 88 – Multi-Tool Agents, MCP & CI/CD Failure Analyzer

## 📖 Overview

Day 88 takes my Agentic AI for DevOps journey to the next level.

Yesterday I built a Docker troubleshooting agent. Today I extended it into a **multi-tool DevOps agent** capable of troubleshooting both **Docker and Kubernetes**.

I also explored **Model Context Protocol (MCP)** and built an MCP server that exposes Kubernetes tools to compatible AI clients. Finally, I built a **CI/CD Failure Analyzer** that uses the GitHub CLI to investigate failed GitHub Actions workflows.

---

## 🏗️ What I Built

### 1. Multi-Tool DevOps Agent

The agent now has **6 tools across two domains**:

**Docker**

* `list_containers()`
* `get_logs()`
* `inspect_container()`

**Kubernetes**

* `list_pods()`
* `describe_pod()`
* `get_events()`

The agent decides which tools to use based on the user's question.

```text
                 ┌─────────────────────┐
                 │      User Query     │
                 └──────────┬──────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   LLM Agent   │
                    │   ReAct       │
                    └───────┬───────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        Docker Tools    K8s Tools      Both
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                       Tool Output
                            │
                            ▼
                       Final Answer
```

---

# ☸️ Kubernetes Troubleshooting

I created a deliberately broken Kubernetes pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: broken-pod
spec:
  containers:
    - name: app
      image: nginx:alpine
      command:
        - sh
        - -c
        - "echo 'app starting...' && sleep 2 && exit 1"
```

The pod crashes after starting, allowing the agent to investigate the issue.

The Kubernetes tools allow the agent to:

```text
list_pods()
     ↓
describe_pod()
     ↓
get_events()
```

This enables the agent to inspect pod state, detailed configuration, conditions, and Kubernetes events.

---

# 🧠 ReAct Multi-Tool Reasoning

The agent follows the same ReAct pattern:

```text
Reason
   ↓
Select Tool
   ↓
Execute Tool
   ↓
Observe Result
   ↓
Reason Again
   ↓
Select Another Tool
   ↓
Final Diagnosis
```

For example:

```text
User:
"Why is broken-pod crashing?"

Agent:
→ list_pods()
→ sees CrashLoop/restarting state
→ describe_pod()
→ checks container state
→ get_events()
→ analyzes events
→ explains root cause
```

One agent can now reason across multiple infrastructure domains.

---

# 🔌 Model Context Protocol (MCP)

One of the major concepts I learned today was **Model Context Protocol**.

MCP provides a standard way for AI models to connect to external tools and data sources.

Instead of embedding tools directly inside a specific Python agent, tools can be exposed through an MCP server and discovered by compatible clients.

### Without MCP

```text
AI Agent
   ↓
Hardcoded Tools
   ↓
Specific Framework
```

### With MCP

```text
                 ┌───────────────┐
                 │   MCP Server  │
                 └───────┬───────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Claude Desktop   VS Code       Python Agent
     Copilot          Cursor        MCP Client
```

Write the tool once and make it available to multiple MCP-compatible clients.

---

# 🛠️ Kubernetes MCP Server

I created an MCP server using **FastMCP**.

```python
from fastmcp import FastMCP

mcp = FastMCP("Kubernetes Tools")
```

Tools are registered using:

```python
@mcp.tool
```

The server exposes:

* `list_pods()`
* `describe_pod()`
* `get_events()`

The MCP server runs using:

```python
mcp.run()
```

Any compatible MCP client can discover and call these tools.

---

# 🔄 MCP Client

Instead of defining Kubernetes tools directly inside the agent, the client dynamically discovers them from the MCP server.

```python
client = MultiServerMCPClient({
    "docker-mcp": {
        "transport": "stdio",
        "command": "python",
        "args": ["mcp_server.py"]
    }
})

tools = await client.get_tools()
```

The agent then receives the tools dynamically.

```text
MCP Server
     ↓
Tool Discovery
     ↓
LangChain MCP Adapter
     ↓
ReAct Agent
     ↓
LLM
```

This separates the **tool implementation** from the **AI agent**.

---

# 🚨 CI/CD Failure Analyzer

The same agent pattern can be applied to CI/CD.

I built a **GitHub Actions Failure Analyzer** using the `gh` CLI.

It has three tools:

### `list_workflow_runs()`

Find recent workflow failures.

### `get_failed_logs()`

Retrieve logs from failed workflow runs.

### `get_workflow_file()`

Read a GitHub Actions workflow YAML file.

---

## 🔍 CI/CD Diagnosis Flow

```text
GitHub Actions
      │
      ▼
Failed Workflow
      │
      ▼
CI/CD AI Agent
      │
      ├── list_workflow_runs()
      │
      ├── get_failed_logs()
      │
      └── get_workflow_file()
              │
              ▼
        Root Cause Analysis
              │
              ▼
        Recommended Fix
```

The agent can answer questions such as:

```text
"What failed in my last CI run?"

"Show me the recent workflow runs"

"Read the gitops-ci.yml workflow and explain it"

"Why did broken-ci fail?"
```

---

# ✂️ Log Truncation

A useful production consideration is **LLM context limits**.

CI logs can become extremely large, so the analyzer limits failed logs to approximately **5000 characters**.

```python
if len(output) > 5000:
    output = output[:5000] + "\n\n[...truncated]"
```

This keeps the most relevant failure information while avoiding unnecessarily large prompts.

---

# 🧰 Custom DevOps Tools

The tool pattern is domain-agnostic.

Any CLI command can potentially become an AI tool.

Examples explored:

### Terraform

```text
terraform_plan()
```

### AWS

```text
list_ec2_instances()
```

### Kubernetes

```text
search_logs()
```

The core pattern remains:

```text
CLI Command
     ↓
Python Function
     ↓
Tool Description
     ↓
LLM
     ↓
Agent Decision
```

---

# 📊 What I Built Today

| Component        |   Tools | Technology              |
| ---------------- | ------: | ----------------------- |
| Multi-tool Agent |       6 | LangChain + ReAct       |
| MCP Server       |       3 | FastMCP                 |
| MCP Client Agent | Dynamic | LangChain + MCP Adapter |
| CI/CD Analyzer   |       3 | GitHub CLI + ReAct      |

---

# 🔑 Key Learnings

* One AI agent can use multiple DevOps toolsets.
* ReAct allows the agent to select tools dynamically.
* MCP separates tools from a specific AI framework.
* MCP tools can be reused by multiple compatible clients.
* CI/CD logs can be analyzed automatically by an AI agent.
* Tool descriptions/docstrings are important because they guide tool selection.
* Large logs should be truncated before sending them to an LLM.
* Any CLI command can potentially become an agent tool.

---

# 🏆 Day 88 Takeaway

The most important pattern I learned today:

```text
Define Tool
    ↓
Expose Tool
    ↓
LLM Discovers Tool
    ↓
Agent Reasons
    ↓
Tool Executes
    ↓
Agent Observes
    ↓
Root Cause / Action
```

This opens up possibilities for AI-powered:

**Docker troubleshooting → Kubernetes troubleshooting → Terraform analysis → AWS investigation → CI/CD debugging → Automated DevOps operations**

---

# 🔗 Repository

[90DaysOfDevOps – GitHub](https://github.com/Apurvbajpai2531/90daysofdevOps

---

## 🚀 Next Step

The goal is to continue combining **DevOps automation with Agentic AI** while keeping tool access controlled, observable, and safe.
