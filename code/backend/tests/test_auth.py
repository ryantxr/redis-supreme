import os
import sys
from pathlib import Path
import pytest
from fastapi.testclient import TestClient

# Use a separate SQLite file for tests inside the database directory
os.environ["DATABASE_URL"] = "sqlite:///./code/backend/database/test_temp.db"

# Ensure the backend package is on the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import app, get_db
from database import Base, engine, SessionLocal

# Ensure a clean database for each test
@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    # Remove the temporary database file
    Path("code/backend/database/test_temp.db").unlink(missing_ok=True)

# Override the dependency to use the same testing session
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_register_success():
    response = client.post("/register", json={"username": "alice", "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert "id" in data


def test_register_existing_user():
    client.post("/register", json={"username": "bob", "password": "pass"})
    response = client.post("/register", json={"username": "bob", "password": "pass"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Username already registered"


def test_login_success():
    client.post("/register", json={"username": "carol", "password": "carolpass"})
    response = client.post("/login", json={"username": "carol", "password": "carolpass"})
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}


def test_login_invalid_credentials():
    client.post("/register", json={"username": "dan", "password": "password"})
    response = client.post("/login", json={"username": "dan", "password": "wrong"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid credentials"
