# Field Force Management System

A backend-focused Field Force Management System built using Django REST Framework with JWT authentication, role-based access control, visit tracking, mocked AI integration, activity logs, and reporting APIs.

## Features

- JWT Authentication
- Role-Based Access Control (RBAC)
- Task Management
- Visit Tracking
- Mock AI Summary & Risk Flags
- Activity Logs
- Dashboard APIs
- Reporting APIs
- Simple Frontend using Django Templates

## Tech Stack

- Django
- Django REST Framework
- Simple JWT
- SQLite

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Frontend

```txt
http://127.0.0.1:8000/
```

## Admin Panel

```txt
http://127.0.0.1:8000/admin/
```

## Main APIs

### Authentication

```http
POST /api/token/
```

### Tasks

```http
GET /api/tasks/
POST /api/tasks/
```

### Visits

```http
POST /api/visits/
```

### Logs

```http
GET /api/logs/
```

### Dashboard

```http
GET /api/dashboard/
```

### Reports

```http
GET /api/reports/pending-tasks/
GET /api/reports/recent-visits/
GET /api/reports/task-status/
```

## Mock AI

A mocked AI service analyzes visit notes and generates:
- AI summaries
- Risk flags

The AI layer is modular and can later be replaced with real LLM integrations.
