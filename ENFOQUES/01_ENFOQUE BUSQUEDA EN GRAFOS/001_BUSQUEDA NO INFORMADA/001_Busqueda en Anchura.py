#Ejemplo de Algoritmo de Busqueda en anchura


from collections import deque
from typing import List, Dict, Any, Tuple

# Definimos el grafo como un diccionario de listas de adyacencia
grafo: Dict[str, List[str]] = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos la funcion de busqueda en anchura

def busqueda_en_anchura(grafo: Dict[str, List[str]], inicio: str, objetivo: str) -> List[str]:
    visitados: List[str] = []  # Lista de nodos visitados
    cola: deque = deque([inicio])  # Cola para los nodos a visitar

    while cola:
        nodo_actual = cola.popleft()  # Extraemos el primer nodo de la cola
        if nodo_actual == objetivo:
            return visitados + [nodo_actual]  # Retornamos la ruta al objetivo
        if nodo_actual not in visitados:
            visitados.append(nodo_actual)  # Marcamos el nodo como visitado
            cola.extend(grafo[nodo_actual])  # Agregamos los nodos adyacentes a la cola

    return []  # Retornamos una lista vacía si no se encuentra el objetivo

# Ejemplo de uso
inicio = 'A'
objetivo = 'C'
ruta = busqueda_en_anchura(grafo, inicio, objetivo)
if ruta:
    print(f"Ruta encontrada: {' -> '.join(ruta)}")
else:
    print("No se encontró una ruta al objetivo.")
