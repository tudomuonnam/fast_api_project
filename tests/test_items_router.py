import datetime

def test_create_item(client):
    data = {"title": "product3","description": "description3"}
    response = client.post("/item",json=data)
    assert response.status_code == 200
    assert response.json()["title"] == "product3"
    assert response.json()["description"] == "description3"
  #  assert response.json()["date_posted"] == datetime.now().date().strftime("%Y-%m-%d")


    