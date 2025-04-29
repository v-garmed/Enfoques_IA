# Importar librerías necesarias
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Datos de ejemplo
emails = [
    ("Win a free iPhone!", "spam"),
    ("Meeting at 10am", "not spam"),
    ("Cheap loans available", "spam"),
    ("Project deadline is tomorrow", "not spam"),
]

# Separar características y etiquetas
texts, labels = zip(*emails)

# Convertir textos en una matriz de características
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)

# Entrenar el modelo Naïve-Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
