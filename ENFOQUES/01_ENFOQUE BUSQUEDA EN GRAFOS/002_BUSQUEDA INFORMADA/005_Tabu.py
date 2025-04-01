import random

# Función objetivo a optimizar
def funcion_objetivo(x):
    return -(x - 3) ** 2 + 9  # Parabólica con máximo en x=3, y=9

# Algoritmo de Búsqueda Tabú
def busqueda_tabu(inicio, iteraciones=100, delta=0.1, tamaño_tabu=5):
    x_actual = inicio  # Estado inicial
    mejor_x = x_actual
    mejor_valor = funcion_objetivo(x_actual)
    lista_tabu = []  # Lista Tabú

    for _ in range(iteraciones):
        # Generar vecinos
        vecinos = [x_actual + delta, x_actual - delta]
        vecinos = [x for x in vecinos if x not in lista_tabu]  # Evitar tabú

        if not vecinos:  # Si todos los vecinos son tabú, salir
            break

        # Escoger el mejor vecino
        x_actual = max(vecinos, key=funcion_objetivo)

        # Actualizar mejor solución
        if funcion_objetivo(x_actual) > mejor_valor:
            mejor_x, mejor_valor = x_actual, funcion_objetivo(x_actual)

        # Agregar a la lista tabú y mantener tamaño
        lista_tabu.append(x_actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)  # Eliminar el más antiguo

    return mejor_x, mejor_valor

# Ejecutar
inicio = random.uniform(-10, 10)  # Punto de inicio aleatorio
solucion, valor = busqueda_tabu(inicio)

print(f"Máximo encontrado en x = {solucion:.2f}, f(x) = {valor:.2f}")
