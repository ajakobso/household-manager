from fastapi.testclient import TestClient
from app.main import app
from pytest import fixture

@fixture
def client():
    return TestClient(app)