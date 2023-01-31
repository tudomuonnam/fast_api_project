from fastapi.testclient import TestClient

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app


client = TestClient(app)

def test_root():
    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}