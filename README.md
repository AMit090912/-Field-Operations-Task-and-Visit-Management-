# Field Force Management System

A backend-focused Field Force Management System built using Django REST Framework.  
The project demonstrates role-based access control, task management, visit tracking, mocked AI integration, activity logging, and reporting APIs.

---

# Features

## Authentication
- JWT Authentication using Simple JWT
- Protected APIs

## Role-Based Access Control (RBAC)
Supported roles:
- Admin
- Regional Manager
- Team Lead
- Field Agent
- Auditor

Scoped visibility implemented using queryset filtering.

---

# Core Modules

## Task Management
- Create tasks
- Assign tasks
- Update task status
- List tasks based on user role

## Visit Tracking
- Create visits
- Add visit notes
- Track visit status

## Mock AI Integration
A mocked AI service analyzes visit notes and:
- generates AI summaries
- assigns risk flags

Example:
- Notes containing keywords like `delay` or `angry`
  generate HIGH risk flags.

## Activity Logs
Tracks:
- Task creation
- Visit creation

## Dashboard APIs
Provides summary statistics:
- total tasks
- completed tasks
- total visits

## Reporting APIs
Implemented reporting endpoints:
- Pending tasks by region
- Visits completed in last 7 days
- Task status distribution

---

# Tech Stack

- Django
- Django REST Framework
- Simple JWT
- SQLite
- HTML/CSS/JavaScript frontend

---

# Project Structure

```txt
backend/
│
├── ai_service/
├── core/
├── logs/
├── tasks/
├── users/
├── visits/
├── templates/
│
├── manage.py
├── requirements.txt
└── README.md
