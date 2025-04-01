import random

# Representación del laberinto (0 = libre, 1 = obstáculo)
laberinto = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Movimientos posibles (arriba, abajo, izquierda, derecha)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función de búsqueda online
def busqueda_online(inicio, objetivo):
    x, y = inicio
    visitados = set()

    while (x, y) != objetivo:
        visitados.add((x, y))
        vecinos = []

        # Explorar movimientos válidos
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and (nx, ny) not in visitados:
                if laberinto[nx][ny] == 0:  # Si no es obstáculo
                    vecinos.append((nx, ny))

        if not vecinos:
            print("¡Sin salida!")
            return None

        # Elegir un vecino aleatorio (simulando exploración)
        x, y = random.choice(vecinos)
        print(f"Moviéndose a: ({x}, {y})")

    print("¡Objetivo encontrado!")

# Ejecutar búsqueda
inicio = (0, 0)
objetivo = (4, 4)
busqueda_online(inicio, objetivo)
