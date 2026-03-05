# Event Management Platform

A cloud-native event management system built with **Flask, MongoDB, Docker, and GitHub Actions CI/CD**.

## Features

* Create participants
* Create trainers
* Create events
* Register participants to events
* Activity logging using MongoDB
* Docker containerization
* Automated testing using Pytest
* CI/CD pipeline using GitHub Actions

---

# Tech Stack

* Backend: Flask (Python)
* Database: MongoDB
* Containerization: Docker
* Testing: Pytest
* CI/CD: GitHub Actions

---

# Project Structure

app/ → Flask application
tests/ → Unit tests using pytest
Dockerfile → Docker image configuration
docker-compose.yml → Service orchestration
.github/workflows → CI/CD pipeline

---

# Setup Instructions

## 1 Clone the repository

git clone https://github.com/pranayvpvns/event-management-platform.git

cd event-management-platform

## 2 Run using Docker

docker-compose up --build

Application will run at:

http://localhost:5000

---

# API Documentation

## Create Participant

POST /participants/add

Request Body:

name
email

Example:

name = John
email = [john@gmail.com](mailto:john@gmail.com)

---

## Create Event

POST /events/add

Request Body:

title
capacity

---

## Register Participant to Event

POST /register

Request Body:

participant_id
event_id

---

# Database Design (ER Diagram)

Entities:

Participant
Trainer
Event
Registration
User Activity Logs

Relationships:

Trainer → conducts → Event
Participant → registers → Event

---

# CI/CD Pipeline

The project uses **GitHub Actions** for continuous integration.

Pipeline Steps:

1. Install dependencies
2. Run pytest tests
3. Build Docker image

Workflow file:

.github/workflows/python-app.yml

Whenever code is pushed to GitHub:

Tests automatically run
Docker build is verified

---

# Activity Logging

All user actions are logged in MongoDB collection:

user_activity

Example log document:

{
action: "Participant Created",
name: "John",
email: "[john@gmail.com](mailto:john@gmail.com)"
}

---

# Author

Pranay
