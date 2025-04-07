# Estados y acciones
states = ['A', 'B', 'C']
actions = ['left', 'right']

# Modelo de transición T(s, a) = (siguiente_estado, recompensa)
T = {
    'A': {'left': ('A', 0), 'right': ('B', 5)},
    'B': {'left': ('A', 0), 'right': ('C', 10)},
    'C': {'left': ('B', 0), 'right': ('C', 0)},
}

gamma = 0.9  # factor de descuento
V = {s: 0 for s in states}  # valores iniciales

for i in range(10):  # 10 iteraciones
    new_V = {}
    for s in states:
        valores_accion = []
        for a in actions:
            s_next, reward = T[s][a]
            valores_accion.append(reward + gamma * V[s_next])
        new_V[s] = max(valores_accion)
    V = new_V

# Derivar política óptima
policy = {}
for s in states:
    mejor_accion = max(actions, key=lambda a: T[s][a][1] + gamma * V[T[s][a][0]])
    policy[s] = mejor_accion

print("Valores finales:", V)
print("Política óptima:", policy)
