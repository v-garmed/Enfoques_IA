from collections import deque

# Definimos el grafo como un diccionario
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Búsqueda en Profundidad (DFS)
def dfs(grafo, inicio, objetivo, visitado=None, camino=None):
    if visitado is None:
        visitado = set()
    if camino is None:
        camino = []
    
    visitado.add(inicio)
    camino.append(inicio)
    
    if inicio == objetivo:
        return camino
    
    for vecino in grafo[inicio]:
        if vecino not in visitado:
            resultado = dfs(grafo, vecino, objetivo, visitado, camino.copy())
            if resultado is not None:
                return resultado
    return None

# Búsqueda en Anchura (BFS)
def bfs(grafo, inicio, objetivo):
    cola = deque([[inicio]])
    visitado = set()
    
    while cola:
        camino = cola.popleft()
        nodo = camino[-1]
        
        if nodo == objetivo:
            return camino
        
        if nodo not in visitado:
            visitado.add(nodo)
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None

# Ejemplo de uso
print("DFS:", dfs(grafo, 'A', 'F'))
print("BFS:", bfs(grafo, 'A', 'F'))