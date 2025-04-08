import nashpy as nash
import numpy as np

# Matrices de pagos: jugador A y jugador B
A = np.array([[3, 0], [5, 1]])  # Jugador A
B = np.array([[3, 5], [0, 1]])  # Jugador B

# Crear el juego
game = nash.Game(A, B)

# Buscar equilibrios de Nash
equilibrios = list(game.support_enumeration())

for eq in equilibrios:
    print("Equilibrio de Nash:", eq)
