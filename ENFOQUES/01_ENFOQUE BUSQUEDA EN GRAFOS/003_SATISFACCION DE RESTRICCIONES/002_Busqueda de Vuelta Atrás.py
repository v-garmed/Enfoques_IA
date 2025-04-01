def es_seguro(tablero, fila, col, N):
    """ Verifica si es seguro colocar una reina en la posición (fila, col) """
    # Verificar la columna hacia arriba
    for i in range(fila):
        if tablero[i] == col:
            return False

    # Verificar la diagonal izquierda
    for i, j in zip(range(fila - 1, -1, -1), range(col - 1, -1, -1)):
        if tablero[i] == j:
            return False

    # Verificar la diagonal derecha
    for i, j in zip(range(fila - 1, -1, -1), range(col + 1, N)):
        if tablero[i] == j:
            return False

    return True

def resolver_n_reinas(tablero, fila, N):
    """ Resuelve el problema de las N reinas usando Backtracking """
    if fila == N:  # Se han colocado todas las reinas
        soluciones.append(tablero[:])  # Guardar la solución encontrada
        return

    for col in range(N):
        if es_seguro(tablero, fila, col, N):
            tablero[fila] = col  # Colocar la reina en esta columna
            resolver_n_reinas(tablero, fila + 1, N)  # Llamada recursiva
            tablero[fila] = -1  # Retroceso (backtrack)

def imprimir_soluciones(soluciones, N):
    """ Muestra todas las soluciones encontradas """
    for sol in soluciones:
        for i in range(N):
            fila = ["."] * N
            fila[sol[i]] = "Q"
            print(" ".join(fila))
        print("\n" + "-" * (2 * N))

# Definir tamaño del tablero
N = 8  # Cambiar para diferentes tamaños de tablero

# Lista para almacenar soluciones
soluciones = []
tablero = [-1] * N  # Inicializar el tablero con -1

# Ejecutar el algoritmo
resolver_n_reinas(tablero, 0, N)

# Imprimir las soluciones encontradas
print(f"Se encontraron {len(soluciones)} soluciones para {N}-reinas:")
imprimir_soluciones(soluciones, N)
