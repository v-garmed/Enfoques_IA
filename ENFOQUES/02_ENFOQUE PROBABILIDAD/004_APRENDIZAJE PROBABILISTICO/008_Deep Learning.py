# Importar librerías necesarias
import tensorflow as tf  # TensorFlow es una biblioteca de aprendizaje automático de código abierto.
from tensorflow.keras import layers, models  # Keras es una API de alto nivel para construir y entrenar modelos en TensorFlow.
from tensorflow.keras.datasets import cifar10  # Conjunto de datos CIFAR-10, que contiene imágenes de 10 clases diferentes.
from tensorflow.keras.utils import to_categorical  # Utilidad para convertir etiquetas en formato categórico (one-hot encoding).

# Cargar el conjunto de datos CIFAR-10
# CIFAR-10 contiene 60,000 imágenes de 32x32 píxeles divididas en 10 clases.
(X_train, y_train), (X_test, y_test) = cifar10.load_data()  # Carga los datos de entrenamiento y prueba.
y_train = to_categorical(y_train)  # Convierte las etiquetas de entrenamiento a formato one-hot.
y_test = to_categorical(y_test)  # Convierte las etiquetas de prueba a formato one-hot.

# Normalizar los datos
# Escala los valores de los píxeles a un rango entre 0 y 1 para mejorar el rendimiento del modelo.
X_train, X_test = X_train / 255.0, X_test / 255.0

# Diseñar la CNN (Red Neuronal Convolucional)
# La CNN se utiliza para procesar datos de imágenes y extraer características relevantes.
model = models.Sequential([  # Sequential permite construir el modelo capa por capa.
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),  # Capa convolucional con 32 filtros y activación ReLU.
    layers.MaxPooling2D((2, 2)),  # Capa de agrupamiento máximo para reducir la dimensionalidad.
    layers.Conv2D(64, (3, 3), activation='relu'),  # Segunda capa convolucional con 64 filtros.
    layers.MaxPooling2D((2, 2)),  # Segunda capa de agrupamiento máximo.
    layers.Conv2D(64, (3, 3), activation='relu'),  # Tercera capa convolucional con 64 filtros.
    layers.Flatten(),  # Aplana las características extraídas en un vector 1D.
    layers.Dense(64, activation='relu'),  # Capa densa completamente conectada con 64 neuronas y activación ReLU.
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas (una por clase) y activación softmax.
])

# Compilar el modelo
# Configura el modelo para el entrenamiento especificando el optimizador, la función de pérdida y las métricas.
model.compile(optimizer='adam',  # Optimizador Adam para ajustar los pesos del modelo.
              loss='categorical_crossentropy',  # Función de pérdida para clasificación multiclase.
              metrics=['accuracy'])  # Métrica para evaluar el rendimiento del modelo.

# Entrenar el modelo
# Ajusta los pesos del modelo utilizando los datos de entrenamiento.
model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))  # Entrena el modelo durante 10 épocas.

# Evaluar el modelo
# Evalúa el rendimiento del modelo en los datos de prueba.
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)  # Calcula la pérdida y precisión en el conjunto de prueba.
print(f"Test accuracy: {test_acc}")  # Imprime la precisión del modelo en los datos de prueba.
