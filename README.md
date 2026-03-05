A cloud-native Event Management Platform built using Flask, MongoDB, Docker, and CI/CD pipelines.

## Features

- Create and manage events
- Register participants
- Activity logging with MongoDB
- REST API endpoints
- Containerized with Docker
- Automated testing with Pytest
- CI using GitHub Actions

---

## Tech Stack

- Python (Flask)
- MongoDB
- Docker
- Pytest
- GitHub Actions

---

## Project Structure


event-management-platform
│
├── app
│ ├── main.py
│ └── database.py
│
├── tests
│ └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

### 1. Clone repository


git clone https://github.com/yourusername/event-management-platform.git

cd event-management-platform


### 2. Install dependencies


pip install -r requirements.txt


### 3. Run application


python -m app.main


---

## Run with Docker


docker-compose up --build


Application will run on:


http://localhost:5000


---

## Run Tests


pytest


---
