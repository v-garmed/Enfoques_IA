# Representación simplificada de un grafo de planificación
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguientes = []

# Construcción del grafo
inicio = Nodo("inicio")
accion1 = Nodo("accion1")
accion2 = Nodo("accion2")
objetivo = Nodo("objetivo")

inicio.siguientes = [accion1, accion2]
accion1.siguientes = [objetivo]
accion2.siguientes = [objetivo]

# Búsqueda en el grafo
def buscar_camino(nodo, objetivo, camino):
    camino.append(nodo.nombre)
    if nodo.nombre == objetivo:
        return camino
    for siguiente in nodo.siguientes:
        resultado = buscar_camino(siguiente, objetivo, camino.copy())
        if resultado:
            return resultado
    return None

# Ejecución de la búsqueda
camino = buscar_camino(inicio, "objetivo", [])
print("Camino encontrado en el grafo:", camino)
