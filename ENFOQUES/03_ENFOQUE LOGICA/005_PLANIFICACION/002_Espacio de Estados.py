# Definición del espacio de estados para un problema simple
estado_inicial = 0
estado_objetivo = 5

def acciones_posibles(estado):
    return [estado + 1, estado + 2]

def buscar_solucion(estado_actual, estado_objetivo, camino):
    if estado_actual == estado_objetivo:
        return camino
    for siguiente_estado in acciones_posibles(estado_actual):
        resultado = buscar_solucion(siguiente_estado, estado_objetivo, camino + [siguiente_estado])
        if resultado:
            return resultado
    return None

# Búsqueda de la solución
camino = buscar_solucion(estado_inicial, estado_objetivo, [estado_inicial])
print("Camino encontrado:", camino)
