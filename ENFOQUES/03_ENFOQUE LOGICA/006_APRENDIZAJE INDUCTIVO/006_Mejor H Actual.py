# Importamos el modelo de Árbol de Decisión para clasificación
from sklearn.tree import DecisionTreeClassifier

# Importamos el modelo Naive Bayes para clasificación
from sklearn.naive_bayes import GaussianNB

# Importamos la métrica para calcular la exactitud del modelo
from sklearn.metrics import accuracy_score

# Importamos herramientas para dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split

# Importamos el conjunto de datos Iris para usarlo como ejemplo
from sklearn.datasets import load_iris

# Cargamos los datos del conjunto Iris y los dividimos en características (X) y etiquetas (y)
X, y = load_iris(return_X_y=True)

# Dividimos los datos en conjuntos de entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Definimos los modelos candidatos para la clasificación
modelos = {
    "Arbol de Decisión": DecisionTreeClassifier(),  # Modelo de Árbol de Decisión
    "Naive Bayes": GaussianNB()                     # Modelo Naive Bayes
}

# Inicializamos variables para almacenar el mejor modelo y su exactitud
mejor_modelo = None
mejor_accuracy = 0

# Iteramos sobre los modelos candidatos
for nombre, modelo in modelos.items():
    # Entrenamos el modelo con los datos de entrenamiento
    modelo.fit(X_train, y_train)
    
    # Realizamos predicciones con los datos de prueba
    pred = modelo.predict(X_test)
    
    # Calculamos la exactitud del modelo
    acc = accuracy_score(y_test, pred)
    print(f"{nombre} tiene exactitud: {acc}")
    
    # Actualizamos el mejor modelo si la exactitud actual es mayor que la mejor registrada
    if acc > mejor_accuracy:
        mejor_modelo = modelo
        mejor_accuracy = acc

# Imprimimos el nombre del mejor modelo encontrado
print("\nMejor modelo:", type(mejor_modelo).__name__)
