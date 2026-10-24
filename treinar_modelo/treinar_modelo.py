
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Carregar os dados das flores
iris = load_iris()
X = iris.data
y = iris.target

# Separar dados para treino e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Treinar o modelo
modelo = RandomForestClassifier(random_state=42)
modelo.fit(X_treino, y_treino)

# Avaliar o modelo
previsoes = modelo.predict(X_teste)
acuracia = accuracy_score(y_teste, previsoes)

print(f"Acurácia: {acuracia:.2%}")

# Salvar o modelo treinado
joblib.dump(modelo, "modelo_iris.joblib")
print("Modelo salvo com sucesso!")