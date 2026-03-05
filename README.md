# Event Management Platform

A **cloud-native event management system** built using **Flask, SQLAlchemy, MongoDB, Docker, and GitHub Actions CI/CD**.

The system allows administrators to manage **participants, trainers, and events**, while logging user activity in **MongoDB**.

---

# Features

* Create and manage participants
* Create trainers and assign them to events
* Create and manage events
* Register participants for events
* Store activity logs in MongoDB
* Containerized using Docker
* Automated testing with Pytest
* Continuous Integration using GitHub Actions

---

# Tech Stack

| Component        | Technology                          |
| ---------------- | ----------------------------------- |
| Backend          | Flask (Python)                      |
| SQL Database     | SQLite / MySQL using SQLAlchemy ORM |
| NoSQL Database   | MongoDB                             |
| Containerization | Docker                              |
| Testing          | Pytest                              |
| CI/CD            | GitHub Actions                      |

---

# Project Structure

```
event-management-platform
│
├── app/                 # Flask application
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── templates/
│
├── tests/               # Pytest test cases
│
├── instance/            # Database instance
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pytest.ini
│
└── .github/workflows/   # GitHub Actions CI pipeline
```

---

# System Architecture

The application follows a **cloud-native microservice style architecture**:

Flask API → SQL Database (events, participants)
Flask API → MongoDB (activity logs)

Docker is used to run services in containers and manage dependencies.

---

# Setup Instructions

## 1 Clone the repository

```bash
git clone https://github.com/pranayvpvns/event-management-platform.git
cd event-management-platform
```

---

## 2 Run using Docker

```bash
docker-compose up --build
```

This will start:

* Flask backend
* MongoDB container

---

## 3 Access the Application

Open browser:

```
http://localhost:5000
```

---

# API Documentation

## Create Participant

**Endpoint**

```
POST /participants/add
```

**Request Body**

| Field | Type   |
| ----- | ------ |
| name  | string |
| email | string |

Example

```
name = John
email = john@gmail.com
```

---

## Create Event

**Endpoint**

```
POST /events/add
```

**Request Body**

| Field    | Type    |
| -------- | ------- |
| title    | string  |
| capacity | integer |

---

## Register Participant for Event

**Endpoint**

```
POST /register
```

**Request Body**

| Field          | Type    |
| -------------- | ------- |
| participant_id | integer |
| event_id       | integer |

---

# Database Design

## SQL Database Entities

* Participant
* Trainer
* Event
* Registration

Relationships

* A **Trainer conducts many Events**
* A **Participant can register for multiple Events**

---

# ER Diagram

(Add diagram image here)

```
Participant ----< Registration >---- Event
                     |
                     |
                   Trainer
```

---

# MongoDB Activity Logs

MongoDB is used to store **application activity logs**.

Collection:

```
user_activity
```

Example log document

```
{
  action: "Participant Created",
  name: "John",
  email: "john@gmail.com"
}
```

These logs track important system events such as:

* Participant creation
* Event creation
* Event registration

---

# Testing

Testing is implemented using **Pytest**.

Test types included:

* Unit tests
* API endpoint tests
* Database interaction tests

Run tests locally:

```
pytest
```

Coverage reports are also generated during testing.

---

# Docker Containerization

The application is containerized using Docker.

Containers:

| Container   | Purpose          |
| ----------- | ---------------- |
| event_app   | Flask backend    |
| event_mongo | MongoDB database |

Docker Compose manages container networking and startup order.

---

# CI/CD Pipeline

Continuous Integration is implemented using **GitHub Actions**.

Workflow file:

```
.github/workflows/python-app.yml
```

Pipeline automatically runs when code is pushed.

Steps executed:

1. Install project dependencies
2. Run Pytest tests
3. Validate application build
4. Ensure project passes all checks

This ensures **code quality and automated testing**.

---

# System Integration Workflow

Complete workflow of the system:

1. Admin creates a participant
2. Admin creates an event
3. Admin registers participant to event
4. Activity logs are stored in MongoDB
5. Data is stored in SQL database
6. CI/CD pipeline validates code on every push

