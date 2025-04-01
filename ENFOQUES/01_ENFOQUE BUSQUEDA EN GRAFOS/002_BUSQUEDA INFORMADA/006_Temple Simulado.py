import math
import random

# Función objetivo a optimizar
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabólica con máximo en x=3, y=9

# Algoritmo de Temple Simulado
def temple_simulado(inicio, temperatura=1000, enfriamiento=0.99, iteraciones=1000, delta=0.1):
    x_actual = inicio  # Estado inicial
    mejor_x = x_actual
    mejor_valor = funcion_objetivo(x_actual)

    for _ in range(iteraciones):
        # Generar vecino cercano
        vecino = x_actual + random.uniform(-delta, delta)
        diferencia = funcion_objetivo(vecino) - funcion_objetivo(x_actual)

        # Aceptar siempre si el vecino es mejor
        if diferencia > 0 or random.uniform(0, 1) < math.exp(diferencia / temperatura):
            x_actual = vecino

        # Actualizar mejor solución
        if funcion_objetivo(x_actual) > mejor_valor:
            mejor_x, mejor_valor = x_actual, funcion_objetivo(x_actual)

        # Reducir la temperatura
        temperatura *= enfriamiento

    return mejor_x, mejor_valor

# Ejecutar
inicio = random.uniform(-10, 10)  # Punto de inicio aleatorio
solucion, valor = temple_simulado(inicio)

print(f"Máximo encontrado en x = {solucion:.2f}, f(x) = {valor:.2f}")
