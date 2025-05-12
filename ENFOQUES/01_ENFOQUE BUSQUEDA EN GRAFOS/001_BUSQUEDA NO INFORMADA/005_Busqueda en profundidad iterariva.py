# Implementación de Búsqueda en Profundidad Iterativa (IDDFS)

# Función auxiliar para realizar una búsqueda en profundidad limitada
def dfs_limitado(grafo, nodo, objetivo, limite, profundidad=0, visitados=None):
    if visitados is None:
        visitados = set()  # Inicializa el conjunto de nodos visitados si no se proporciona uno
    
    print(f"Visitando: {nodo}, Profundidad: {profundidad}")
    visitados.add(nodo)  # Marca el nodo actual como visitado

    # Verifica si el nodo actual es el objetivo
    if nodo == objetivo:
        print("¡Objetivo encontrado!")
        return True

    # Si se alcanza el límite de profundidad, detiene la búsqueda en este camino
    if profundidad >= limite:
        return False

    # Recorre los vecinos del nodo actual
    for vecino in grafo[nodo]:
        if vecino not in visitados:  # Solo visita nodos no visitados
            # Llama recursivamente a dfs_limitado para explorar más profundamente
            if dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1, visitados):
                return True

    return False  # Retorna False si no encuentra el objetivo en este camino

# Función principal para realizar la Búsqueda en Profundidad Iterativa
def iddfs(grafo, inicio, objetivo, max_profundidad):
    # Itera sobre diferentes límites de profundidad desde 0 hasta max_profundidad
    for limite in range(max_profundidad + 1):
        print(f"\n Explorando con límite de profundidad: {limite}")
        # Llama a dfs_limitado con el límite actual
        if dfs_limitado(grafo, inicio, objetivo, limite):
            return True  # Termina si encuentra el objetivo
    print("No se encontró el objetivo dentro del límite máximo.")

    return False  # Retorna False si no encuentra el objetivo en ningún límite

# Definir el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],  # Nodo 'A' tiene como vecinos a 'B' y 'C'
    'B': ['D', 'E'],  # Nodo 'B' tiene como vecinos a 'D' y 'E'
    'C': ['F'],       # Nodo 'C' tiene como vecino a 'F'
    'D': [],          # Nodo 'D' no tiene vecinos
    'E': ['F'],       # Nodo 'E' tiene como vecino a 'F'
    'F': [],          # Nodo 'F' no tiene vecinos
    'G': ['H'],       # Nodo 'G' tiene como vecino a 'H' (no conectado al resto del grafo)
}

# Ejecutar Búsqueda en Profundidad Iterativa desde 'A' buscando 'H' con profundidad máxima de 3
print("\nBúsqueda en Profundidad Iterativa (IDDFS)")
iddfs(grafo, 'A', 'H', 3)  # Busca el nodo 'H' desde 'A' con un límite de profundidad de 3


##La diferencia con la profundidad limitada es que este aumenta conforme no encuentre al nodo, así hasta
# que no quede nodo en el cual buscar