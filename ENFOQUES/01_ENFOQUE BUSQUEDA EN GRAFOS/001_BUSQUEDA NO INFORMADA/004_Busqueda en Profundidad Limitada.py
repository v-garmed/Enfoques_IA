# Implementación de Búsqueda en Profundidad Limitada (DLS)
def dfs_limitado(grafo, nodo, objetivo, limite, profundidad=0, visitados=None):
    if visitados is None:
        visitados = set()
    
    print(f"Visitando: {nodo}, Profundidad: {profundidad}")
    visitados.add(nodo)

    # Si encontramos el objetivo, devolvemos True
    if nodo == objetivo:
        print("¡Objetivo encontrado!")
        return True

    # Si alcanzamos el límite, detenemos la búsqueda
    if profundidad >= limite:
        return False

    # Explorar vecinos dentro del límite
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            if dfs_limitado(grafo, vecino, objetivo, limite, profundidad + 1, visitados):
                return True

    return False


# Definir el grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecutar Búsqueda en Profundidad Limitada desde 'A' con límite 2
print("\nBúsqueda en Profundidad Limitada con Límite = 2")
encontrado = dfs_limitado(grafo, 'A', 'F', 2)

if not encontrado:
    print("No se encontró la solución dentro del límite.")

##Nota, cada profundidad puede considerarse como un movimiento entre nodos. Ejemplo: A>B>D serán 2 movimientos y no encontrará la respuesta, pero A>C>F sí lo hará.
# En una misma cantidad.
