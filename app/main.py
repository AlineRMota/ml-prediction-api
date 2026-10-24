import joblib
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris

app = FastAPI(
    title="ML Prediction API",
    description="Minha primeira API de Machine Learning",
    version="0.1.0",
)

CAMINHO_MODELO = Path(__file__).resolve().parent.parent / "treinar_modelo" / "modelo_iris.joblib"

modelo = joblib.load(CAMINHO_MODELO)

iris = load_iris()

class DadosFlor(BaseModel):
    comprimento_sepala: float = Field(gt=0)
    largura_sepala: float = Field(gt=0)
    comprimento_petala: float = Field(gt=0)
    largura_petala: float = Field(gt=0)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/prever/{numero}")
def prever(numero: int):
    dobro = numero * 2
    return {"numero_recebido": numero, "dobro": dobro}

@app.post("/prever-flor")
def prever_flor(dados: DadosFlor):
    entrada = [[
        dados.comprimento_sepala,
        dados.largura_sepala,
        dados.comprimento_petala,
        dados.largura_petala,
    ]]

    previsao = modelo.predict(entrada)[0]
    probabilidades = modelo.predict_proba(entrada)[0]

    especie = iris.target_names[previsao]

    resultado_probabilidades = {
        nome: round(float(probabilidade), 4)
        for nome, probabilidade in zip(
            iris.target_names, probabilidades
        )
    }

    return {
        "especie_prevista": especie,
        "probabilidades": resultado_probabilidades,
    }


