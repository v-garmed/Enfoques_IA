import random

# Parámetros del algoritmo genético
TAM_POBLACION = 10
GENERACIONES = 50
MUTACION_PROB = 0.2

# Función objetivo
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabólica con máximo en x=3

# Generar población inicial aleatoria
def generar_poblacion():
    return [random.uniform(-10, 10) for _ in range(TAM_POBLACION)]

# Selección por torneo
def seleccion(poblacion):
    return max(random.sample(poblacion, 2), key=funcion_objetivo)

# Cruce (promedio entre padres)
def cruce(padre1, padre2):
    return (padre1 + padre2) / 2

# Mutación (pequeña alteración)
def mutacion(individuo):
    if random.random() < MUTACION_PROB:
        return individuo + random.uniform(-0.5, 0.5)
    return individuo

# Algoritmo Genético
def algoritmo_genetico():
    poblacion = generar_poblacion()
    
    for _ in range(GENERACIONES):
        nueva_poblacion = []
        for _ in range(TAM_POBLACION):
            padre1, padre2 = seleccion(poblacion), seleccion(poblacion)
            hijo = cruce(padre1, padre2)
            hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)
        poblacion = nueva_poblacion
    
    mejor_solucion = max(poblacion, key=funcion_objetivo)
    return mejor_solucion, funcion_objetivo(mejor_solucion)

# Ejecutar algoritmo
solucion, valor = algoritmo_genetico()
print(f"Mejor solución encontrada: x = {solucion:.2f}, f(x) = {valor:.2f}")
