import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200

def test_participants_page(client):
    response = client.get("/participants")
    assert response.status_code == 200

def test_create_participant(client):
    response = client.post(
        "/participants/add",
        data={
            "name": "Test User",
            "email": "test@test.com",
            "phone": "1234567890"
        },
        follow_redirects=True
    )
    assert response.status_code == 200

def test_events_page(client):

    response = client.get("/events")

    assert response.status_code == 200

def test_create_event(client):
    response = client.post(
        "/events/add",
        data={
            "title": "Test Event",
            "capacity": 50,
            "trainer_id": 1
        },
        follow_redirects=True
    )
    assert response.status_code == 200