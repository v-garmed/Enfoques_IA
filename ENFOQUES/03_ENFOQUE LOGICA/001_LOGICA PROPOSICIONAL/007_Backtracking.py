# Definimos un grafo como un diccionario, donde las claves son los nodos y los valores son listas de nodos vecinos.
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Lista de colores disponibles para asignar a los nodos.
colores = ['Rojo', 'Verde']

# Función que verifica si asignar un color a un nodo es válido.
# Un color es válido si ningún vecino del nodo tiene el mismo color.
def es_valido(nodo, color, asignacion):
    return all(asignacion.get(vecino) != color for vecino in grafo[nodo])

# Función de backtracking para asignar colores a los nodos del grafo.
# Recibe la asignación actual de colores y la lista de nodos pendientes por procesar.
def backtracking(asignacion, nodos):
    # Caso base: si no quedan nodos por procesar, devolvemos la asignación actual.
    if not nodos:
        return asignacion
    
    # Tomamos el primer nodo de la lista de nodos pendientes.
    nodo = nodos[0]
    
    # Intentamos asignar cada color disponible al nodo actual.
    for color in colores:
        # Verificamos si el color es válido para el nodo actual.
        if es_valido(nodo, color, asignacion):
            # Asignamos el color al nodo.
            asignacion[nodo] = color
            
            # Llamamos recursivamente al backtracking con el resto de los nodos.
            resultado = backtracking(asignacion.copy(), nodos[1:])
            
            # Si encontramos una solución válida, la devolvemos.
            if resultado:
                return resultado
    
    # Si no se puede asignar un color válido, devolvemos None.
    return None

# Llamamos a la función de backtracking con una asignación inicial vacía y todos los nodos del grafo.
sol = backtracking({}, list(grafo.keys()))

# Imprimimos la asignación de colores encontrada.
print("Colores asignados:", sol)
