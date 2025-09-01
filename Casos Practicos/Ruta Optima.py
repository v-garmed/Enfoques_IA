import random
import math

# Coordenadas de las casas (x, y)
casas = {
    "A": (2, 3),
    "B": (5, 8),
    "C": (1, 9),
    "D": (7, 4),
    "E": (6, 1)
}

# Distancia euclidiana entre dos casas
def distancia(a, b):
    return math.dist(casas[a], casas[b])

# Función objetivo: longitud total de la ruta
def longitud_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(ruta[i], ruta[i+1])
    return total

# Algoritmo de Búsqueda Tabú para optimizar rutas
def busqueda_tabu_rutas(ruta_inicial, iteraciones=100, tamaño_tabu=10):
    ruta_actual = ruta_inicial[:]
    mejor_ruta = ruta_inicial[:]
    mejor_distancia = longitud_ruta(mejor_ruta)
    lista_tabu = []

    for _ in range(iteraciones):
        # Generar vecinos intercambiando dos ciudades
        vecinos = []
        for i in range(len(ruta_actual)):
            for j in range(i+1, len(ruta_actual)):
                vecino = ruta_actual[:]
                vecino[i], vecino[j] = vecino[j], vecino[i]
                if vecino not in lista_tabu:
                    vecinos.append(vecino)

        if not vecinos:
            break

        # Escoger el vecino con menor distancia
        ruta_actual = min(vecinos, key=longitud_ruta)

        # Actualizar mejor solución
        if longitud_ruta(ruta_actual) < mejor_distancia:
            mejor_ruta, mejor_distancia = ruta_actual[:], longitud_ruta(ruta_actual)

        # Actualizar lista tabú
        lista_tabu.append(ruta_actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

    return mejor_ruta, mejor_distancia

# Ruta inicial aleatoria
casas_lista = list(casas.keys())
ruta_inicial = random.sample(casas_lista, len(casas_lista))

# Ejecutar búsqueda tabú
mejor_ruta, mejor_distancia = busqueda_tabu_rutas(ruta_inicial)

print("🚚 Ruta óptima encontrada:", " -> ".join(mejor_ruta))
print(f"📏 Distancia total: {mejor_distancia:.2f}")
