import random

# Función objetivo a optimizar
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabólica con máximo en x=3, y=9

# Algoritmo de Búsqueda de Haz Local
def busqueda_haz_local(k=3, iteraciones=50, delta=0.5):
    # Generar k soluciones iniciales aleatorias
    soluciones = [random.uniform(-10, 10) for _ in range(k)]
    
    for _ in range(iteraciones):
        # Generar todos los vecinos posibles
        vecinos = []
        for s in soluciones:
            vecinos.append(s + delta)
            vecinos.append(s - delta)

        # Seleccionar las k mejores soluciones
        soluciones = sorted(vecinos, key=funcion_objetivo, reverse=True)[:k]
    
    # Mejor solución encontrada
    mejor_x = soluciones[0]
    mejor_valor = funcion_objetivo(mejor_x)
    return mejor_x, mejor_valor

# Ejecutar
solucion, valor = busqueda_haz_local()

print(f"Máximo encontrado en x = {solucion:.2f}, f(x) = {valor:.2f}")
