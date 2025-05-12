from collections import deque

# Definimos el grafo como un diccionario
# Cada nodo tiene una lista de nodos vecinos a los que está conectado
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Búsqueda en Profundidad (DFS)
# Función recursiva para buscar un camino desde el nodo de inicio hasta el nodo objetivo
def dfs(grafo, inicio, objetivo, visitado=None, camino=None):
    # Inicializamos el conjunto de nodos visitados si no se proporciona
    if visitado is None:
        visitado = set()
    # Inicializamos el camino si no se proporciona
    if camino is None:
        camino = []
    
    # Marcamos el nodo actual como visitado y lo añadimos al camino
    visitado.add(inicio)
    camino.append(inicio)
    
    # Si el nodo actual es el objetivo, devolvemos el camino encontrado
    if inicio == objetivo:
        return camino
    
    # Recorremos los vecinos del nodo actual
    for vecino in grafo[inicio]:
        # Si el vecino no ha sido visitado, realizamos una llamada recursiva
        if vecino not in visitado:
            resultado = dfs(grafo, vecino, objetivo, visitado, camino.copy())
            # Si encontramos un camino, lo devolvemos
            if resultado is not None:
                return resultado
    # Si no se encuentra un camino, devolvemos None
    return None

# Búsqueda en Anchura (BFS)
# Función iterativa para buscar un camino desde el nodo de inicio hasta el nodo objetivo
def bfs(grafo, inicio, objetivo):
    # Usamos una cola para gestionar los caminos a explorar
    cola = deque([[inicio]])
    # Conjunto para registrar los nodos visitados
    visitado = set()
    
    # Mientras haya caminos en la cola
    while cola:
        # Extraemos el primer camino de la cola
        camino = cola.popleft()
        # Obtenemos el último nodo del camino
        nodo = camino[-1]
        
        # Si el nodo actual es el objetivo, devolvemos el camino encontrado
        if nodo == objetivo:
            return camino
        
        # Si el nodo no ha sido visitado
        if nodo not in visitado:
            # Lo marcamos como visitado
            visitado.add(nodo)
            # Añadimos los caminos extendidos con los vecinos del nodo actual
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    # Si no se encuentra un camino, devolvemos None
    return None

# Ejemplo de uso
# Imprimimos el resultado de la búsqueda en profundidad (DFS) desde 'A' hasta 'F'
print("DFS:", dfs(grafo, 'A', 'F'))
# Imprimimos el resultado de la búsqueda en anchura (BFS) desde 'A' hasta 'F'
print("BFS:", bfs(grafo, 'A', 'F'))