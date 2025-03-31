from collections import deque

def bidirectional_search(grafo, inicio, objetivo):
    # Inicializar las dos fronteras
    frontera_inicio = deque([inicio])
    frontera_objetivo = deque([objetivo])
    
    # Conjuntos para los nodos visitados desde cada dirección
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}
    
    while frontera_inicio and frontera_objetivo:
        # Expande desde el inicio
        if frontera_inicio:
            nodo = frontera_inicio.popleft()
            print(f"Desde inicio visitando: {nodo}")
            if nodo in visitados_objetivo:
                print(f"¡Camino encontrado en {nodo}!")
                return True
            for vecino in grafo[nodo]:
                if vecino not in visitados_inicio:
                    visitados_inicio.add(vecino)
                    frontera_inicio.append(vecino)
        
        # Expande desde el objetivo
        if frontera_objetivo:
            nodo = frontera_objetivo.popleft()
            print(f"Desde objetivo visitando: {nodo}")
            if nodo in visitados_inicio:
                print(f"¡Camino encontrado en {nodo}!")
                return True
            for vecino in grafo[nodo]:
                if vecino not in visitados_objetivo:
                    visitados_objetivo.add(vecino)
                    frontera_objetivo.append(vecino)
    
    print("No se encontró un camino entre los nodos.")
    return False

# Definir el grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

# Ejecutar la búsqueda bidireccional desde 'A' a 'E'
print("\nBúsqueda Bidireccional")
bidirectional_search(grafo, 'A', 'E')
