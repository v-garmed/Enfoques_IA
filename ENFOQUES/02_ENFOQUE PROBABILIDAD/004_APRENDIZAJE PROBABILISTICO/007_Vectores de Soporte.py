# Importar librerías necesarias
# sklearn.datasets: para cargar conjuntos de datos predefinidos como MNIST.
# sklearn.model_selection: para dividir los datos en conjuntos de entrenamiento y prueba.
# sklearn.svm: para implementar máquinas de soporte vectorial (SVM).
# sklearn.metrics: para calcular métricas de evaluación como la precisión.
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos MNIST
# digits contiene imágenes de dígitos escritos a mano (0-9) y sus etiquetas correspondientes.
digits = datasets.load_digits()
X, y = digits.data, digits.target  # X son las características (imágenes) y y son las etiquetas (dígitos).

# Dividir los datos en conjuntos de entrenamiento y prueba
# Se utiliza un 75% de los datos para entrenamiento y un 25% para prueba.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Entrenar SVM con diferentes núcleos
# Se prueban tres tipos de núcleos: lineal, polinómico y radial (RBF).
kernels = ['linear', 'poly', 'rbf']
for kernel in kernels:
    # Crear un modelo SVM con el núcleo especificado.
    svm = SVC(kernel=kernel)
    
    # Entrenar el modelo con los datos de entrenamiento.
    svm.fit(X_train, y_train)
    
    # Predecir las etiquetas para los datos de prueba.
    y_pred = svm.predict(X_test)
    
    # Calcular la precisión del modelo comparando las predicciones con las etiquetas reales.
    accuracy = accuracy_score(y_test, y_pred)
    
    # Imprimir la precisión del modelo para el núcleo actual.
    print(f"SVM ({kernel} kernel) Accuracy: {accuracy}")
