from fastapi.testclient import TestClient
import json

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

client = TestClient()

def test_create_user():
    data = {"email": "testuser1@example.com","password": "mypassword"}
    response = client.post("/users",json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser1@example.com"
    assert response.json()["is_active"] == True