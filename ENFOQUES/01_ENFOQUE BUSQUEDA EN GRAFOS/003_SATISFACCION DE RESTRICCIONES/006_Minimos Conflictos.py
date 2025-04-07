import random

def conflictos(tablero, fila, col):
    conflictos = 0
    for i in range(len(tablero)):
        if i == fila:
            continue
        # Mismo columna o misma diagonal
        if tablero[i] == col or abs(tablero[i] - col) == abs(i - fila):
            conflictos += 1
    return conflictos

def min_conflicts(n, max_intentos=5000):
    # Asignación inicial aleatoria (una reina por fila)
    tablero = [random.randint(0, n - 1) for _ in range(n)]

    for _ in range(max_intentos):
        conflictuadas = [fila for fila in range(n) if conflictos(tablero, fila, tablero[fila]) > 0]
        if not conflictuadas:
            return tablero  # Solución encontrada

        fila = random.choice(conflictuadas)
        min_col = tablero[fila]
        min_conf = n  # Peor caso

        for col in range(n):
            conf = conflictos(tablero, fila, col)
            if conf < min_conf:
                min_conf = conf
                min_col = col

        tablero[fila] = min_col  # Reasignar con menor conflicto

    return None  # No se encontró solución en los intentos dados

# Ejecutamos para 8 reinas
solucion = min_conflicts(8)
if solucion:
    print("Solución encontrada:", solucion)
else:
    print("No se encontró solución.")
