import heapq

def busqueda_anchura_uniforme(grafo, inicio, objetivo):
    """
    Algoritmo de Búsqueda en Anchura Uniforme (Uniform Cost Search - UCS)
    Encuentra el camino más corto desde el nodo 'inicio' hasta el nodo 'objetivo' en un grafo ponderado.
    
    :param grafo: Diccionario donde las claves son nodos y los valores son listas de tuplas (vecino, costo).
    :param inicio: Nodo de inicio.
    :param objetivo: Nodo de destino.
    :return: Ruta más corta y su costo.
    """
    # Cola de prioridad (heap) para almacenar (costo, nodo, camino)
    cola_prioridad = [(0, inicio, [])]
    
    # Conjunto para rastrear los nodos visitados
    visitados = set()
    
    while cola_prioridad:
        # Extraemos el nodo con el menor costo acumulado
        costo_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)
        
        # Si ya hemos visitado el nodo, continuamos con otro
        if nodo_actual in visitados:
            continue
        
        # Registramos el nodo como visitado
        visitados.add(nodo_actual)
        
        # Agregamos el nodo al camino
        camino = camino + [nodo_actual]
        
        # Si llegamos al objetivo, devolvemos el camino y el costo
        if nodo_actual == objetivo:
            return camino, costo_actual
        
        # Expandimos los vecinos del nodo actual
        for vecino, costo in grafo[nodo_actual]:
            if vecino not in visitados:
                heapq.heappush(cola_prioridad, (costo_actual + costo, vecino, camino))
    
    return None, float("inf")  # Retorna infinito si no hay camino

# Definir el grafo como un diccionario
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2), ('E', 1)],
    'E': [('B', 5), ('D', 1), ('F', 2)],
    'F': [('C', 3), ('E', 2)]
}

# Ejecutar el algoritmo UCS
inicio = 'A'
objetivo = 'F'
camino, costo = busqueda_anchura_uniforme(grafo, inicio, objetivo)

# Mostrar el resultado
if camino:
    print(f"Camino más corto encontrado: {camino} con un costo total de {costo}")
else:
    print("No hay camino disponible.")
