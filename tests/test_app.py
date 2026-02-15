import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Signup
    email = "testuser@mergington.edu"
    activity = "Chess Club"
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_resp.status_code == 200
    assert email in signup_resp.json()["message"]
    # Duplicate signup
    dup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert dup_resp.status_code == 400
    # Unregister
    unreg_resp = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unreg_resp.status_code == 200
    assert email in unreg_resp.json()["message"]
    # Unregister non-existent
    unreg_resp2 = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unreg_resp2.status_code == 404
