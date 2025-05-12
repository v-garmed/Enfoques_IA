import heapq  # Importa la biblioteca heapq para manejar colas de prioridad

# Grafo con conexiones y costos
grafo = {
    'A': ['B', 'C'],  # Nodo A conectado a B y C
    'B': ['A', 'D', 'E'],  # Nodo B conectado a A, D y E
    'C': ['A', 'F'],  # Nodo C conectado a A y F
    'D': ['B'],  # Nodo D conectado a B
    'E': ['B', 'F'],  # Nodo E conectado a B y F
    'F': ['C', 'E']  # Nodo F conectado a C y E
}

# Heurística estimada (valores ficticios)
heuristica = {
    'A': 6,  # Estimación de costo desde A al objetivo
    'B': 4,  # Estimación de costo desde B al objetivo
    'C': 4,  # Estimación de costo desde C al objetivo
    'D': 2,  # Estimación de costo desde D al objetivo
    'E': 2,  # Estimación de costo desde E al objetivo
    'F': 0   # Estimación de costo desde F al objetivo (objetivo alcanzado)
}

def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    # Inicializa una cola de prioridad para explorar nodos según la heurística
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (heuristica[inicio], inicio, []))  # (h(n), nodo, camino)
    visitados = set()  # Conjunto para rastrear nodos visitados

    while cola_prioridad:
        # Extrae el nodo con el menor valor heurístico
        h, nodo, camino = heapq.heappop(cola_prioridad)
        if nodo in visitados:  # Si el nodo ya fue visitado, lo ignora
            continue

        # Actualiza el camino y marca el nodo como visitado
        camino = camino + [nodo]
        visitados.add(nodo)

        # Si se alcanza el objetivo, imprime y retorna el camino
        if nodo == objetivo:
            print(f"Camino encontrado: {camino}")
            return camino

        # Explora los vecinos del nodo actual
        for vecino in grafo[nodo]:
            if vecino not in visitados:  # Solo agrega vecinos no visitados
                heapq.heappush(cola_prioridad, (heuristica[vecino], vecino, camino))

    # Si no se encuentra un camino al objetivo, informa al usuario
    print("No se encontró un camino")
    return None

# Ejecutar búsqueda voraz
print("\nBúsqueda Voraz desde A hasta F:")
busqueda_voraz(grafo, heuristica, 'A', 'F')
