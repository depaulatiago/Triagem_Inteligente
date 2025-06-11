from sklearn.tree import DecisionTreeClassifier
import joblib

# Exemplo de dados fictícios para treino
X = [
    [38.5, 1, 0],
    [36.0, 0, 0],
    [39.5, 1, 1],
    [37.2, 0, 1]
]
y = ['moderado', 'leve', 'grave', 'moderado']

modelo = DecisionTreeClassifier()
modelo.fit(X, y)

joblib.dump(modelo, 'modelo.pkl')
