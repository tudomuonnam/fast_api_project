
def test_create_user(client):
    data = {"email": "testuser1@example.com","password": "mypassword"}
    response = client.post("/users",json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "testuser1@example.com"
    assert response.json()["is_active"] == True