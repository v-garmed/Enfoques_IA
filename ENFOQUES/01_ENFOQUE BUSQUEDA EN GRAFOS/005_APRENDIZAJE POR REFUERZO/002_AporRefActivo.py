import numpy as np
import random

# Definimos entorno
estados = [(0,0), (0,1), (0,2),
           (1,0), (1,1), (1,2),
           (2,0), (2,1), (2,2)]
acciones = [(0,1), (1,0), (0,-1), (-1,0)]  # Derecha, abajo, izquierda, arriba
recompensas = {(0,2): 1, (1,2): -1}
terminales = [(0,2), (1,2)]

# Parámetros Q-learning
Q = {s: {a: 0 for a in acciones} for s in estados}
alpha = 0.5
gamma = 0.9
epsilon = 0.1

# Función para obtener siguiente estado válido
def mover(s, a):
    x, y = s[0] + a[0], s[1] + a[1]
    if (x, y) in estados:
        return (x, y)
    return s

# Entrenamiento
for episodio in range(5000):
    s = (0, 0)
    while s not in terminales:
        if random.random() < epsilon:
            a = random.choice(acciones)
        else:
            a = max(Q[s], key=Q[s].get)
        s_next = mover(s, a)
        r = recompensas.get(s_next, 0)
        best_next = max(Q[s_next].values())
        Q[s][a] += alpha * (r + gamma * best_next - Q[s][a])
        s = s_next

# Mostrar política aprendida
print("Política óptima aprendida (mejor acción por estado):")
for s in estados:
    if s in terminales:
        print(f"{s}: TERMINAL")
    else:
        mejor_accion = max(Q[s], key=Q[s].get)
        print(f"{s}: {mejor_accion}")
