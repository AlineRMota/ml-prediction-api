
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.json() == {"status": "ok"}


def test_prever_flor():
    resposta = client.post(
        "/prever-flor",
        json={
            "comprimento_sepala": 5.1,
            "largura_sepala": 3.5,
            "comprimento_petala": 1.4,
            "largura_petala": 0.2,
        },
    )

    assert resposta.status_code == 200

    resultado = resposta.json()

    assert resultado["especie_prevista"] == "setosa"
    assert "probabilidades" in resultado
    assert set(resultado["probabilidades"].keys()) == {
        "setosa",
        "versicolor",
        "virginica",
    }


def test_prever_flor_rejeita_texto_em_medida():
    resposta = client.post(
        "/prever-flor",
        json={
            "comprimento_sepala": "flor",
            "largura_sepala": 3.5,
            "comprimento_petala": 1.4,
            "largura_petala": 0.2,
        },
    )

    assert resposta.status_code == 422

def test_prever_flor_rejeita_medida_negativa():
    resposta = client.post(
        "/prever-flor",
        json={
            "comprimento_sepala": -5.1,
            "largura_sepala": 3.5,
            "comprimento_petala": 1.4,
            "largura_petala": 0.2,
        },
    )

    assert resposta.status_code == 422
