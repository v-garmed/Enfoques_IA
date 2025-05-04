# Ejemplo básico de razonamiento inductivo con clasificación supervisada usando sklearn

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Datos de ejemplo: [edad, temperatura corporal, dolor muscular]
X = [[25, 37.5, 0], [30, 38.2, 1], [45, 39.1, 1], [22, 36.8, 0]]
# Etiquetas: 1 = enfermo, 0 = sano
y = [0, 1, 1, 0]

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

# Clasificador de árbol de decisión
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predicción y reporte
pred = clf.predict(X_test)
print(classification_report(y_test, pred))
