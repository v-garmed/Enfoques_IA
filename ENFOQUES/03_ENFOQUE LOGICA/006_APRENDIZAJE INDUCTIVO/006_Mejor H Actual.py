from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Datos
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Modelos candidatos
modelos = {
    "Arbol de Decisión": DecisionTreeClassifier(),
    "Naive Bayes": GaussianNB()
}

mejor_modelo = None
mejor_accuracy = 0

for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    pred = modelo.predict(X_test)
    acc = accuracy_score(y_test, pred)
    print(f"{nombre} tiene exactitud: {acc}")
    
    if acc > mejor_accuracy:
        mejor_modelo = modelo
        mejor_accuracy = acc

print("\nMejor modelo:", type(mejor_modelo).__name__)
