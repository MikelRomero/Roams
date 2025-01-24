import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import create_db_and_tables, get_session, engine
from sqlmodel import SQLModel, Session

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():

    create_db_and_tables()
    yield

    SQLModel.metadata.drop_all(engine)

@pytest.fixture(scope="module")
def session():
    with Session(engine) as session:
        yield session

def test_create_cliente(test_db):
    response = client.post("/clientes/", json={
        "nombre": "John Doe",
        "dni": "12345678Z",
        "email": "john.doe@example.com",
        "capital_solicitado": 100000.0
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "John Doe"
    assert response.json()["dni"] == "12345678Z"

def test_get_cliente(test_db):
    response = client.get("/clientes/dni/12345678Z")
    assert response.status_code == 200
    assert response.json()["nombre"] == "John Doe"
    assert response.json()["dni"] == "12345678Z"

def test_update_cliente(test_db):
    response = client.put("/clientes/dni/12345678Z", json={
        "nombre": "John Doe Updated",
        "dni": "12345678Z",
        "email": "john.doe.updated@example.com",
        "capital_solicitado": 150000.0
    })
    assert response.status_code == 200
    assert response.json()["nombre"] == "John Doe Updated"
    assert response.json()["email"] == "john.doe.updated@example.com"

def test_delete_cliente(test_db):
    response = client.delete("/clientes/dni/12345678Z")
    assert response.status_code == 200
    assert response.json()["message"] == "Cliente eliminado"

    response = client.get("/clientes/dni/12345678Z")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente no encontrado"

def test_simulate_hipoteca(test_db):

    response = client.post("/clientes/", json={
        "nombre": "Jane Doe",
        "dni": "87654321X",
        "email": "jane.doe@example.com",
        "capital_solicitado": 200000.0
    })
    assert response.status_code == 200
    cliente_id = response.json()["id"]

    response = client.post("/hipotecas/", json={
        "cliente_id": 1,
        "tae": 3.5,
        "plazo_amortizacion": 30
    })
    assert response.status_code == 200
    assert "cuota_mensual" in response.json()