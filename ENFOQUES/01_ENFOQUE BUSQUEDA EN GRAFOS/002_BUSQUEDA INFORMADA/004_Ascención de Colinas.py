import random

# Función a optimizar (encontrar el máximo)
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabólica con máximo en x=3, y=9

# Algoritmo de Ascensión de Colinas
def hill_climbing(inicio, pasos=100, delta=0.1):
    x = inicio  # Estado inicial
    for _ in range(pasos):
        vecino = x + random.choice([-delta, delta])  # Elegir un vecino cercano
        if funcion_objetivo(vecino) > funcion_objetivo(x):  # Si mejora, moverse
            x = vecino
    return x, funcion_objetivo(x)

# Ejecutar
inicio = random.uniform(-10, 10)  # Punto de inicio aleatorio
solucion, valor = hill_climbing(inicio)

print(f"Máximo encontrado en x = {solucion:.2f}, f(x) = {valor:.2f}")
