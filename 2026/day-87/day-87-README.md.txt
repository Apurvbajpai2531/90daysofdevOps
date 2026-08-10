# 🚀 Day 87 – Introduction to Agentic AI for DevOps

## 📖 Overview

Day 87 of my **#90DaysOfDevOps** journey marks the beginning of the **Agentic AI for DevOps** block.

After working with Linux, Docker, CI/CD, Kubernetes, Terraform, Ansible, Observability, Helm, EKS, and GitOps, I started exploring how AI agents can interact with DevOps tools and help troubleshoot infrastructure.

Unlike a traditional chatbot, an AI agent can use tools, execute commands, inspect systems, and reason over the results to reach a solution.

---

## 🎯 Today's Objectives

* Understand Agentic AI for DevOps
* Set up Ollama locally
* Run the Gemma 4 model
* Create a Python environment with LangChain
* Build a Docker Error Explainer
* Build a Docker Troubleshooter Agent
* Understand the ReAct pattern
* Create tools that wrap Docker CLI commands
* Experiment with autonomous troubleshooting

---

# 🤖 What is an AI Agent?

An AI agent is an **LLM that can use tools to interact with the real world**.

A chatbot primarily generates text, while an agent can:

* Run commands
* Read files
* Call APIs
* Inspect infrastructure
* Choose which tool to use
* Reason over tool output
* Perform multiple actions before responding

### Agent Architecture

```text
User Question
      │
      ▼
┌───────────────┐
│      LLM      │
│  Gemma 4      │
└───────┬───────┘
        │
        ▼
   Tool Selection
        │
   ┌────┼───────────────┐
   ▼    ▼               ▼
docker ps  docker logs  docker inspect
   │    │               │
   └────┼───────────────┘
        ▼
   Tool Results
        │
        ▼
       LLM
        │
        ▼
   Final Diagnosis
```

---

# 🔄 ReAct Pattern

The agent uses the **Reason + Act** approach.

```text
User:
"Why is broken-app crashing?"
        │
        ▼
     THINK
"I should check containers"
        │
        ▼
      ACT
list_containers()
        │
        ▼
    OBSERVE
"broken-app is Restarting"
        │
        ▼
     THINK
"I should check its logs"
        │
        ▼
      ACT
get_logs("broken-app")
        │
        ▼
    OBSERVE
"app starting... → exit code 1"
        │
        ▼
     THINK
"Container exits immediately"
        │
        ▼
     ANSWER
Explain root cause + fix
```

The important part is that **the LLM decides which tools to call and in what order** based on the problem.

---

# 🧠 Key Components

| Component       | Role                         |
| --------------- | ---------------------------- |
| LLM             | Brain                        |
| Tools           | Hands                        |
| Agent Framework | Reasoning/orchestration      |
| MCP             | Standard way to expose tools |

The task uses **Ollama/Gemma 4**, Python tools, LangChain's `create_react_agent`, and introduces MCP as the next step.

---

# 🦙 Environment Setup

I explored a local AI setup using **Ollama + Gemma 4**.

```bash
ollama serve &
ollama pull gemma4
ollama list
```

Then created a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

The environment includes:

* `ollama`
* `langchain`
* `langchain-ollama`
* `langgraph`
* `fastmcp`
* `langchain-mcp-adapters`

---

# 🐳 Docker Error Explainer

The first project was a simple LLM application without tools or an agent loop.

It takes a Docker error and converts it into a human-readable explanation.

The system prompt asks the model to explain:

1. What went wrong
2. The most likely cause
3. How to fix it

The model runs with a low temperature of `0.3` for more deterministic technical responses.

Example:

```text
Docker:
Bind for 0.0.0.0:8080 failed:
port is already allocated.
```

The LLM can explain that another process/container is already using port `8080` and suggest commands to identify and resolve the conflict.

---

# 🛠️ Docker Troubleshooter Agent

The second project is where Agentic AI becomes interesting.

I created a deliberately broken container:

```bash
docker run -d \
  --name broken-app \
  nginx:alpine \
  sh -c "echo 'app starting...' && sleep 2 && exit 1"
```

The container starts, prints a message, waits, exits with code `1`, and repeatedly restarts.

---

## 🔧 Agent Tools

The agent has three Docker tools:

### `list_containers()`

Runs:

```bash
docker ps -a
```

### `get_logs()`

Runs:

```bash
docker logs --tail 50 <container>
```

### `inspect_container()`

Runs:

```bash
docker inspect <container>
```

These functions are exposed to the LLM using LangChain's `@tool` decorator.

---

# 🔍 Autonomous Troubleshooting

When asked:

```text
Why is broken-app crashing?
```

The agent performs approximately this workflow:

```text
1. list_containers()
        ↓
2. Detect "Restarting"
        ↓
3. get_logs("broken-app")
        ↓
4. Find application exit
        ↓
5. inspect_container("broken-app")
        ↓
6. Confirm exit code 1
        ↓
7. Explain root cause
```

The key learning was that **I didn't explicitly tell the agent to check logs or inspect the container**. The LLM selected the tools based on their descriptions and the problem.

---

# 🧩 Tool Pattern

A DevOps CLI command can be wrapped as an agent tool:

```python
@tool
def my_tool(argument: str) -> str:
    """Description the LLM reads to decide when to use the tool."""
    result = subprocess.run(
        ["some-cli", "command", argument],
        capture_output=True,
        text=True
    )
    return result.stdout or result.stderr
```

This pattern can be extended to:

```text
Docker
   ↓
Kubernetes
   ↓
Terraform
   ↓
AWS CLI
   ↓
Ansible
   ↓
GitHub CLI
```

The underlying agent architecture remains the same.

---

# 🧪 Experiment: Add More Tools

I also explored extending the agent with additional tools such as:

```python
list_images()
```

to inspect Docker images and their sizes.

Another possible tool is:

```python
restart_container(container_name)
```

which allows the agent to restart a container.

This introduces an important production consideration: **agents that can modify infrastructure need guardrails** such as confirmation, permissions, and allowed-resource lists.

---

# 🏗️ DevOps + Agentic AI

The overall architecture can evolve from:

```text
                ┌───────────────┐
                │   AI Agent    │
                │   Gemma 4     │
                └───────┬───────┘
                        │
                ┌───────▼───────┐
                │     Tools     │
                └───────┬───────┘
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
     Docker          Kubernetes       Terraform
```

Tomorrow the same approach can be extended with Kubernetes tools, followed by automated remediation and guardrails.

---

# 📚 Key Learnings

### 1. AI Agent ≠ Chatbot

An agent can reason, select tools, execute actions, and inspect results.

### 2. ReAct

The agent follows:

**Reason → Act → Observe → Repeat → Answer**

### 3. Tools

Python functions can turn existing DevOps CLI commands into capabilities available to an LLM.

### 4. Local AI

Ollama allows models to run locally without API keys or external model APIs.

### 5. Guardrails

Giving an AI agent the ability to modify infrastructure introduces safety concerns and requires appropriate controls.

---

# 🔮 What's Next?

The Agentic AI journey continues with:

```text
Day 87
Agentic AI + Docker
       ↓
Day 88
MCP + Kubernetes Tools
       ↓
Day 89
Production DevOps Agent
       ↓
Automated Troubleshooting
```

---

# 🔗 GitHub

[My 90DaysOfDevOps Repository](https://github.com/Apurvbajpai2531/90daysofdevOps?utm_source=chatgpt.com)

---

## 🎯 Final Takeaway

**AI doesn't replace DevOps tools — it can reason over them.**

The same Docker, Kubernetes, Terraform, AWS, and Ansible commands that DevOps engineers already use can become tools for an AI agent.

That opens the door to intelligent troubleshooting, automated diagnosis, and eventually safe automated remediation.
