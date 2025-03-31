# Implementación de DFS en un grafo
def dfs_recursivo(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()
    
    print(nodo, end=" ")  # Imprimir el nodo visitado
    visitados.add(nodo)

    # Llamada recursiva para cada vecino no visitado
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_recursivo(grafo, vecino, visitados)


# Implementación iterativa usando una pila
def dfs_iterativo(grafo, inicio):
    visitados = set()
    pila = [inicio]

    while pila:
        nodo = pila.pop()  # Sacamos el último nodo (LIFO)
        if nodo not in visitados:
            print(nodo, end=" ")  # Imprimir el nodo visitado
            visitados.add(nodo)

            # Agregar vecinos a la pila (en orden inverso para mantener la exploración en profundidad)
            for vecino in reversed(grafo[nodo]):
                if vecino not in visitados:
                    pila.append(vecino)


# Definir un grafo como diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar DFS desde el nodo 'A'
print("DFS Recursivo:")
dfs_recursivo(grafo, 'A')

print("\nDFS Iterativo:")
dfs_iterativo(grafo, 'A')
