import heapq

# Implementación de A*
def a_estrella(grafo, heuristica, inicio, objetivo):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica[inicio], 0, inicio, []))
    visitados = set()

    while cola_prioridad:
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        if nodo in visitados:
            continue

        camino = camino + [nodo]
        visitados.add(nodo)

        if nodo == objetivo:
            print(f"Camino encontrado con A*: {camino} con costo {g}")
            return camino

        for vecino, costo in grafo[nodo].items():
            if vecino not in visitados:
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica[vecino]
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino))

    print("No se encontró un camino con A*")
    return None

# Implementación de AO*
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sucesores = []
        self.costo = float('inf')
        self.marca = False

    def agregar_sucesor(self, nodos, costo):
        self.sucesores.append((nodos, costo))

def ao_estrella(raiz):
    if not raiz.sucesores:
        raiz.costo = 0
        raiz.marca = True
        return

    for hijos, costo in raiz.sucesores:
        for hijo in hijos:
            ao_estrella(hijo)
        
        costo_total = costo + sum(hijo.costo for hijo in hijos)
        if costo_total < raiz.costo:
            raiz.costo = costo_total
            raiz.marca = all(hijo.marca for hijo in hijos)

# Datos de entrada para A*
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'F': 3},
    'E': {'B': 5, 'C': 1, 'F': 2},
    'F': {'D': 3, 'E': 2}
}

heuristica = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 0}

# Datos de entrada para AO*
A, B, C, D, E, F = Nodo('A'), Nodo('B'), Nodo('C'), Nodo('D'), Nodo('E'), Nodo('F')
A.agregar_sucesor([B, C], 5)
B.agregar_sucesor([D], 2)
C.agregar_sucesor([E, F], 3)
D.agregar_sucesor([], 0)
E.agregar_sucesor([], 0)
F.agregar_sucesor([], 0)

# Ejecutar A*
print("\nEjecutando A*")
a_estrella(grafo, heuristica, 'A', 'F')

# Ejecutar AO*
print("\nEjecutando AO*")
ao_estrella(A)
print(f"Costo mínimo desde A con AO*: {A.costo}")
