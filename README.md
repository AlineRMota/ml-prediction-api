# ML Prediction API

API de Machine Learning desenvolvida com Python e FastAPI para disponibilizar previsões de um modelo de classificação treinado com o conjunto de dados Iris.

## Objetivo

Este projeto demonstra um fluxo básico de Machine Learning Engineering, desde o treinamento e a serialização de um modelo até sua disponibilização por meio de uma API REST, com validação de entradas e testes automatizados.

## Tecnologias utilizadas

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Pytest

## Funcionalidades

- Endpoint de verificação de saúde da API.
- Endpoint de exemplo para previsão numérica.
- Classificação de flores Iris com Random Forest.
- Retorno da espécie prevista e das probabilidades por classe.
- Validação dos dados de entrada.
- Testes automatizados dos endpoints e de entradas inválidas.

## Estrutura do projeto

```text
ml-prediction-api/
├── app/
│   └── main.py
├── tests/
│   └── test_api.py
├── treinar_modelo/
│   ├── modelo_iris.joblib
│   └── treinar_modelo.py
├── .gitignore
└── README.md
```

## Como executar

### 1. Instalar as dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias:

```bash
pip install fastapi uvicorn scikit-learn joblib pytest httpx
```

### 2. Iniciar a API

Na pasta raiz do projeto, execute:

```bash
python -m uvicorn app.main:app --reload
```

### 3. Acessar a documentação interativa

Abra no navegador:

http://127.0.0.1:8000/docs

A documentação permite consultar os endpoints e enviar dados para testar as previsões.

## Testes automatizados

Com o terminal na pasta raiz do projeto, execute:

```bash
python -m pytest -v
```

## Modelo de Machine Learning

O projeto utiliza um classificador Random Forest treinado com o conjunto de dados Iris, que contém medidas de sépalas e pétalas para três espécies de flores.

O endpoint `/prever-flor` recebe as quatro medidas e retorna a espécie prevista e as probabilidades estimadas para cada classe.

## Próximas melhorias

- Adicionar configuração de dependências em um arquivo `requirements.txt`.
- Melhorar o tratamento de erros e a documentação da API.
- Implementar integração contínua para executar os testes automaticamente.
- Criar testes adicionais para validar o comportamento do modelo.
