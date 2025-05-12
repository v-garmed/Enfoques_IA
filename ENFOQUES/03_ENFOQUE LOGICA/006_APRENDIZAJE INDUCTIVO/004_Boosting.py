# Importar el modelo de boosting (AdaBoost) de la biblioteca scikit-learn
from sklearn.ensemble import AdaBoostClassifier

# Importar el clasificador base (árbol de decisión) de scikit-learn
from sklearn.tree import DecisionTreeClassifier

# Importar la función para generar conjuntos de datos artificiales
from sklearn.datasets import make_classification

# Generar un conjunto de datos artificiales con características y etiquetas
X, y = make_classification(n_samples=100, n_features=5, random_state=42)

# Crear un clasificador base (árbol de decisión con profundidad máxima de 1)
base_clf = DecisionTreeClassifier(max_depth=1)

# Crear un modelo de boosting (AdaBoost) utilizando el clasificador base
boost_clf = AdaBoostClassifier(base_estimator=base_clf, n_estimators=50)

# Entrenar el modelo de boosting con los datos generados
boost_clf.fit(X, y)

# Imprimir la precisión del modelo en los datos de entrenamiento
print("Precisión del modelo:", boost_clf.score(X, y))
