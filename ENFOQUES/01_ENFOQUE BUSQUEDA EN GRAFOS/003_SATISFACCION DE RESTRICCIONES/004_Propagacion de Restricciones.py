from collections import deque

def es_consistente(variable, valor, asignacion, restricciones):
    """ Verifica si asignar 'valor' a 'variable' cumple con las restricciones. """
    for vecino in restricciones[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Conflicto con vecino
    return True

def ac3(restricciones, dominios):
    """ Aplica el algoritmo AC-3 para propagar restricciones. """
    cola = deque([(x, y) for x in restricciones for y in restricciones[x]])  

    while cola:
        xi, xj = cola.popleft()
        if reducir_dominio(xi, xj, dominios):
            if not dominios[xi]:  
                return False  # No hay valores válidos, inconsistencia encontrada
            for vecino in restricciones[xi]:
                if vecino != xj:
                    cola.append((vecino, xi))
    return True  

def reducir_dominio(xi, xj, dominios):
    """ Elimina valores de xi que no cumplen la restricción con xj """
    reducido = False
    for valor in list(dominios[xi]):
        if all(valor == v for v in dominios[xj]):  
            dominios[xi].remove(valor)
            reducido = True
    return reducido

def coloreo_grafos(nodos, restricciones, colores):
    """ Intenta asignar colores a un grafo usando AC-3 y backtracking. """
    dominios = {nodo: set(colores) for nodo in nodos}
    if not ac3(restricciones, dominios):
        return None  

    asignacion = {}  
    return backtracking_coloreo(asignacion, nodos, dominios, restricciones)

def backtracking_coloreo(asignacion, nodos, dominios, restricciones):
    """ Algoritmo de backtracking con propagación de restricciones. """
    if len(asignacion) == len(nodos):
        return asignacion  

    nodo = min((n for n in nodos if n not in asignacion), key=lambda x: len(dominios[x]))  

    for color in dominios[nodo]:
        if es_consistente(nodo, color, asignacion, restricciones):
            asignacion[nodo] = color
            resultado = backtracking_coloreo(asignacion, nodos, dominios, restricciones)
            if resultado:
                return resultado
            del asignacion[nodo]  

    return None  

# Definimos el grafo
nodos = ['A', 'B', 'C', 'D']
restricciones = {
    'A': {'B', 'C'},
    'B': {'A', 'C', 'D'},
    'C': {'A', 'B', 'D'},
    'D': {'B', 'C'}
}
colores = ['Rojo', 'Verde', 'Azul']

# Ejecutamos la propagación de restricciones con AC-3 y backtracking
solucion = coloreo_grafos(nodos, restricciones, colores)

if solucion:
    print("Coloreo del grafo encontrado:")
    for nodo, color in solucion.items():
        print(f"Nodo {nodo}: {color}")
else:
    print("No se encontró una solución válida.")
