# Implementación de DFS en un grafo (búsqueda en profundidad)
def dfs_recursivo(grafo, nodo, visitados=None):
    # Inicializar el conjunto de nodos visitados si no se proporciona
    if visitados is None:
        visitados = set()
    
    # Imprimir el nodo actual (visitado)
    print(nodo, end=" ")
    # Marcar el nodo como visitado
    visitados.add(nodo)

    # Llamada recursiva para cada vecino no visitado del nodo actual
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_recursivo(grafo, vecino, visitados)


# Implementación iterativa de DFS usando una pila
def dfs_iterativo(grafo, inicio):
    # Conjunto para rastrear los nodos visitados
    visitados = set()
    # Pila para gestionar los nodos a explorar (LIFO)
    pila = [inicio]

    # Mientras haya nodos en la pila
    while pila:
        # Sacar el último nodo de la pila
        nodo = pila.pop()
        # Si el nodo no ha sido visitado
        if nodo not in visitados:
            # Imprimir el nodo actual (visitado)
            print(nodo, end=" ")
            # Marcar el nodo como visitado
            visitados.add(nodo)

            # Agregar los vecinos del nodo actual a la pila
            # Se invierte el orden para mantener la exploración en profundidad
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)


# Definir un grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],  # Nodo 'A' tiene como vecinos a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' tiene como vecinos a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' tiene como vecino a 'F'
    'D': [],          # Nodo 'D' no tiene vecinos
    'E': ['F'],       # Nodo 'E' tiene como vecino a 'F'
    'F': []           # Nodo 'F' no tiene vecinos
}

# Ejecutar DFS recursivo desde el nodo 'A'
print("DFS Recursivo:")
dfs_recursivo(grafo, 'A')

# Ejecutar DFS iterativo desde el nodo 'A'
print("\nDFS Iterativo:")
dfs_iterativo(grafo, 'A')
