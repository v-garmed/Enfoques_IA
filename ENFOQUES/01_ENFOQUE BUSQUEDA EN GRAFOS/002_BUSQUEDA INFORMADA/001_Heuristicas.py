import heapq

# Definimos el grafo con costos
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'F': 3},
    'E': {'B': 5, 'C': 1, 'F': 2},
    'F': {'D': 3, 'E': 2}
}

# Heurística estimada (valores ficticios)
heuristica = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 0
}

def a_estrella(grafo, heuristica, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica[inicio], 0, inicio, []))  # (f(n), g(n), nodo, camino)
    visitados = set()

    while cola_prioridad:
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == objetivo:
            print(f"Camino encontrado: {camino} con costo {g}")
            return camino

        for vecino, costo in grafo[nodo].items():
            if vecino not in visitados:
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica[vecino]
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino))

    print("No se encontró un camino")
    return None

# Ejecutar la búsqueda A*
print("\nBúsqueda A* desde A hasta F:")
a_estrella(grafo, heuristica, 'A', 'F')
