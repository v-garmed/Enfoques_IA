# Definición del espacio de estados para un problema simple
estado_inicial = 0
estado_objetivo = 5

# Define las acciones posibles desde un estado dado
# En este caso, se puede avanzar al siguiente estado sumando 1 o 2
def acciones_posibles(estado):
    return [estado + 1, estado + 2]

# Función recursiva para buscar una solución desde el estado actual al estado objetivo
# estado_actual: el estado en el que estamos actualmente
# estado_objetivo: el estado que queremos alcanzar
# camino: la lista de estados visitados hasta ahora
def buscar_solucion(estado_actual, estado_objetivo, camino):
    # Si el estado actual es el estado objetivo, se retorna el camino encontrado
    if estado_actual == estado_objetivo:
        return camino
    # Explora las acciones posibles desde el estado actual
    for siguiente_estado in acciones_posibles(estado_actual):
        # Llama recursivamente para buscar una solución desde el siguiente estado
        resultado = buscar_solucion(siguiente_estado, estado_objetivo, camino + [siguiente_estado])
        # Si se encuentra una solución, se retorna
        if resultado:
            return resultado
    # Si no se encuentra solución, retorna None
    return None

# Búsqueda de la solución desde el estado inicial al estado objetivo
# Se inicia el camino con el estado inicial
camino = buscar_solucion(estado_inicial, estado_objetivo, [estado_inicial])
print("Camino encontrado:", camino)
