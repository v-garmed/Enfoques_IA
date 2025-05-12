import heapq

# Definimos el grafo con costos
# Representa un grafo donde las claves son nodos y los valores son diccionarios
# que contienen los nodos vecinos y el costo de moverse hacia ellos.
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'F': 3},
    'E': {'B': 5, 'C': 1, 'F': 2},
    'F': {'D': 3, 'E': 2}
}

# Heurística estimada (valores ficticios)
# Representa una estimación del costo desde cada nodo hasta el objetivo.
heuristica = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 0
}

# Función que implementa el algoritmo A* para encontrar el camino más corto
# entre un nodo inicial y un nodo objetivo.
def a_estrella(grafo, heuristica, inicio, objetivo):
    # Cola de prioridad para almacenar los nodos a explorar.
    # Cada elemento es una tupla (f(n), g(n), nodo, camino).
    cola_prioridad = []
    # Insertamos el nodo inicial en la cola con f(n) = g(n) + h(n).
    heapq.heappush(cola_prioridad, (0 + heuristica[inicio], 0, inicio, []))
    # Conjunto para rastrear los nodos visitados.
    visitados = set()

    # Mientras haya nodos en la cola de prioridad.
    while cola_prioridad:
        # Extraemos el nodo con el menor valor de f(n).
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        # Si el nodo ya fue visitado, lo ignoramos.
        if nodo in visitados:
            continue

        # Actualizamos el camino actual y marcamos el nodo como visitado.
        camino = camino + [nodo]
        visitados.add(nodo)

        # Si llegamos al nodo objetivo, imprimimos el camino y su costo.
        if nodo == objetivo:
            print(f"Camino encontrado: {camino} con costo {g}")
            return camino

        # Exploramos los vecinos del nodo actual.
        for vecino, costo in grafo[nodo].items():
            # Si el vecino no ha sido visitado, calculamos sus valores g(n) y f(n).
            if vecino not in visitados:
                nuevo_g = g + costo  # Costo acumulado hasta el vecino.
                nuevo_f = nuevo_g + heuristica[vecino]  # Costo total estimado.
                # Añadimos el vecino a la cola de prioridad.
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino))

    # Si no encontramos un camino al objetivo, lo indicamos.
    print("No se encontró un camino")
    return None

# Ejecutar la búsqueda A* desde el nodo 'A' hasta el nodo 'F'.
print("\nBúsqueda A* desde A hasta F:")
a_estrella(grafo, heuristica, 'A', 'F')
