grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}
colores = ['Rojo', 'Verde']

def es_valido(nodo, color, asignacion):
    return all(asignacion.get(vecino) != color for vecino in grafo[nodo])

def backtracking(asignacion, nodos):
    if not nodos:
        return asignacion
    nodo = nodos[0]
    for color in colores:
        if es_valido(nodo, color, asignacion):
            asignacion[nodo] = color
            resultado = backtracking(asignacion.copy(), nodos[1:])
            if resultado:
                return resultado
    return None

sol = backtracking({}, list(grafo.keys()))
print("Colores asignados:", sol)
