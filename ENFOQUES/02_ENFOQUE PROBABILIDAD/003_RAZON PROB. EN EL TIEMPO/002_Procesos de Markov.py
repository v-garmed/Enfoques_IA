import numpy as np

# Definimos los estados
estados = ["Soleado", "Nublado", "Lluvioso"]

# Matriz de transición: filas = estado actual, columnas = estado siguiente
# Ejemplo: desde Soleado → [0.6 a Soleado, 0.3 a Nublado, 0.1 a Lluvioso]
matriz_transicion = np.array([
    [0.6, 0.3, 0.1],  # Soleado
    [0.2, 0.5, 0.3],  # Nublado
    [0.1, 0.3, 0.6]   # Lluvioso
])

# Estado inicial
estado_actual = 0  # Comenzamos en "Soleado"
np.random.seed(42)

# Simulación de 10 días
secuencia = [estados[estado_actual]]

for _ in range(10):
    estado_actual = np.random.choice([0, 1, 2], p=matriz_transicion[estado_actual])
    secuencia.append(estados[estado_actual])

# Mostrar resultado
print("Secuencia de clima en 10 días:")
print(" → ".join(secuencia))
