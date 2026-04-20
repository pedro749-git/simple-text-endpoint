from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_text_normal():
    """Prueba un escenario normal con combinación de mayúsculas y minúsculas."""
    response = client.post("/text", json={"text": "Hello World"})
    assert response.status_code == 200
    assert response.json() == {
        "original": "Hello World",
        "uppercase": "HELLO WORLD",
        "char_count": 11
    }

def test_process_text_empty_string():
    """Prueba el caso de enviar un string vacío."""
    response = client.post("/text", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {
        "original": "",
        "uppercase": "",
        "char_count": 0
    }

def test_process_text_special_characters():
    """Prueba caracteres especiales y tildes para asegurar que .upper() y len() funcionan bien."""
    response = client.post("/text", json={"text": "café!"})
    assert response.status_code == 200
    assert response.json() == {
        "original": "café!",
        "uppercase": "CAFÉ!",
        "char_count": 5
    }

def test_process_text_invalid_payload():
    """Prueba el manejo de errores enviando un JSON sin el campo text."""
    response = client.post("/text", json={})
    assert response.status_code == 422