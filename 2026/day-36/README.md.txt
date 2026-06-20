# Dockerized Python Backend Application

A production-style Python Flask application containerized with Docker and orchestrated using Docker Compose. The project demonstrates how multiple services can work together in a containerized environment using PostgreSQL for data storage and Redis for caching.

## Tech Stack

* Python
* Flask
* PostgreSQL 16
* Redis 7
* Docker
* Docker Compose
* Celery

## Project Structure

```text
.
├── Dockerfile
├── docker-compose.yml
├── .env
├── README.md
└── app
    ├── app.py
    ├── task.py
    └── requirements.txt
```

## Features

* Containerized Flask application
* PostgreSQL database integration
* Redis caching service
* Environment variable management
* Persistent database storage with Docker Volumes
* Health checks for service readiness
* Multi-container deployment using Docker Compose

## Environment Variables

Create a `.env` file in the project root:

```env
DB_HOST=db
DB_NAME=appdb
DB_USER=admin
DB_PASS=admin
```

## Run Locally

Build and start all services:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up -d --build
```

## Access the Application

Open:

```text
http://localhost:5009
```

Example response:

```text
🚀 Dockerized Python Backend | Visits: 1
```

## Services

| Service    | Purpose                  |
| ---------- | ------------------------ |
| Backend    | Flask application        |
| PostgreSQL | Database storage         |
| Redis      | Cache and message broker |

## Learning Outcomes

* Docker image creation
* Multi-container applications
* Docker Compose orchestration
* Volume management
* Environment configuration
* Service health checks

## Author

Apurv Bajpai

GitHub: https://github.com/Apurvbajpai2531
