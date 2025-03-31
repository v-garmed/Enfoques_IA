# Implementación de Búsqueda en Profundidad Iterativa (IDDFS)
# Implementación de Búsqueda en Profundidad Iterativa (IDDFS)
def dfs_limitado(grafo, nodo, objetivo, limite, profundidad=0, visitados=None):
    if visitados is None:
        visitados = set()
    
    print(f"Visitando: {nodo}, Profundidad: {profundidad}")
    visitados.add(nodo)

    if nodo == objetivo:
        print("¡Objetivo encontrado!")
        return True

    if profundidad >= limite:
        return False

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            if dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1, visitados):
                return True

    return False


def iddfs(grafo, inicio, objetivo, max_profundidad):
    for limite in range(max_profundidad + 1):
        print(f"\n Explorando con límite de profundidad: {limite}")
        if dfs_limitado(grafo, inicio, objetivo, limite):
            return True  # Termina si encuentra el objetivo
    print("No se encontró el objetivo dentro del límite máximo.")

    return False


# Definir el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': ['H'],
}

# Ejecutar Búsqueda en Profundidad Iterativa desde 'A' buscando 'F' con profundidad máxima de 3
print("\nBúsqueda en Profundidad Iterativa (IDDFS)")
iddfs(grafo, 'A', 'H', 3)


##La diferencia con la profundidad limitada es que este aumenta conforme no encuentre al nodo, así hasta
# que no quede nodo en el cual buscar