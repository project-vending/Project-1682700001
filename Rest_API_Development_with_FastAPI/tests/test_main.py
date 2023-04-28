
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World, this is the root endpoint!"}

def test_read_item():
    response = client.get("/items/foo")
    assert response.status_code == 200
    assert response.json() == {"item_id": "foo", "item_name": "Fake Item"}
