import heapq

# Implementación de A* (Algoritmo de búsqueda informada)
def a_estrella(grafo, heuristica, inicio, objetivo):
    # Cola de prioridad para almacenar los nodos a explorar, ordenados por su costo estimado (f = g + h)
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0 + heuristica[inicio], 0, inicio, []))  # (f, g, nodo, camino)
    visitados = set()  # Conjunto para rastrear nodos ya visitados

    while cola_prioridad:
        # Extraer el nodo con el menor costo estimado (f)
        f, g, nodo, camino = heapq.heappop(cola_prioridad)
        if nodo in visitados:
            continue  # Si ya fue visitado, lo ignoramos

        # Actualizar el camino actual
        camino = camino + [nodo]
        visitados.add(nodo)  # Marcar el nodo como visitado

        # Si llegamos al objetivo, devolvemos el camino y el costo
        if nodo == objetivo:
            print(f"Camino encontrado con A*: {camino} con costo {g}")
            return camino

        # Explorar los vecinos del nodo actual
        for vecino, costo in grafo[nodo].items():
            if vecino not in visitados:
                # Calcular los nuevos costos g y f
                nuevo_g = g + costo
                nuevo_f = nuevo_g + heuristica[vecino]
                # Agregar el vecino a la cola de prioridad
                heapq.heappush(cola_prioridad, (nuevo_f, nuevo_g, vecino, camino))

    # Si no se encuentra un camino, se informa
    print("No se encontró un camino con A*")
    return None

# Clase Nodo para representar nodos en el algoritmo AO*
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del nodo
        self.sucesores = []  # Lista de sucesores (hijos) del nodo
        self.costo = float('inf')  # Costo inicial (infinito)
        self.marca = False  # Marca para indicar si el nodo está resuelto

    # Método para agregar sucesores al nodo
    def agregar_sucesor(self, nodos, costo):
        self.sucesores.append((nodos, costo))  # (lista de nodos hijos, costo de transición)

# Implementación de AO* (Algoritmo de optimización en grafos AND-OR)
def ao_estrella(raiz):
    # Si el nodo no tiene sucesores, es un nodo hoja
    if not raiz.sucesores:
        raiz.costo = 0  # El costo de un nodo hoja es 0
        raiz.marca = True  # Se marca como resuelto
        return

    # Recorrer cada conjunto de sucesores del nodo
    for hijos, costo in raiz.sucesores:
        # Resolver recursivamente los nodos hijos
        for hijo in hijos:
            ao_estrella(hijo)
        
        # Calcular el costo total para este conjunto de sucesores
        costo_total = costo + sum(hijo.costo for hijo in hijos)
        # Actualizar el costo del nodo si encontramos un costo menor
        if costo_total < raiz.costo:
            raiz.costo = costo_total
            # El nodo se marca si todos sus hijos están marcados
            raiz.marca = all(hijo.marca for hijo in hijos)

# Datos de entrada para A* (grafo y heurística)
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'E': 1},
    'D': {'B': 2, 'F': 3},
    'E': {'B': 5, 'C': 1, 'F': 2},
    'F': {'D': 3, 'E': 2}
}

heuristica = {'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 2, 'F': 0}

# Datos de entrada para AO* (nodos y relaciones)
A, B, C, D, E, F = Nodo('A'), Nodo('B'), Nodo('C'), Nodo('D'), Nodo('E'), Nodo('F')
A.agregar_sucesor([B, C], 5)  # Nodo A tiene como sucesores a B y C con un costo de 5
B.agregar_sucesor([D], 2)     # Nodo B tiene como sucesor a D con un costo de 2
C.agregar_sucesor([E, F], 3)  # Nodo C tiene como sucesores a E y F con un costo de 3
D.agregar_sucesor([], 0)      # Nodo D es una hoja
E.agregar_sucesor([], 0)      # Nodo E es una hoja
F.agregar_sucesor([], 0)      # Nodo F es una hoja

# Ejecutar A*
print("\nEjecutando A*")
a_estrella(grafo, heuristica, 'A', 'F')  # Buscar el camino desde A hasta F usando A*

# Ejecutar AO*
print("\nEjecutando AO*")
ao_estrella(A)  # Resolver el grafo AND-OR comenzando desde el nodo A
print(f"Costo mínimo desde A con AO*: {A.costo}")  # Imprimir el costo mínimo desde A
