import heapq

# Grafo con conexiones y costos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Heurística estimada (valores ficticios)
heuristica = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 0
}

def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica[inicio], inicio, []))  # (h(n), nodo, camino)
    visitados = set()

    while cola_prioridad:
        h, nodo, camino = heapq.heappop(cola_prioridad)
        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == objetivo:
            print(f"Camino encontrado: {camino}")
            return camino

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (heuristica[vecino], vecino, camino))

    print("No se encontró un camino")
    return None

# Ejecutar búsqueda voraz
print("\nBúsqueda Voraz desde A hasta F:")
busqueda_voraz(grafo, heuristica, 'A', 'F')
