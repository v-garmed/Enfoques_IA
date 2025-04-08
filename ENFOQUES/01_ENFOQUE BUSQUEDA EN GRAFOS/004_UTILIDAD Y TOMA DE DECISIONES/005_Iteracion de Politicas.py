states = ['A', 'B', 'C']
actions = ['left', 'right']

# Modelo de transición y recompensa
T = {
    'A': {'left': ('A', 0), 'right': ('B', 5)},
    'B': {'left': ('A', 0), 'right': ('C', 10)},
    'C': {'left': ('B', 0), 'right': ('C', 0)},
}

gamma = 0.9

# Inicializar política arbitraria
policy = {s: 'left' for s in states}
V = {s: 0 for s in states}

def evaluar_politica(policy, V, iteraciones=10):
    for _ in range(iteraciones):
        for s in states:
            a = policy[s]
            s_next, r = T[s][a]
            V[s] = r + gamma * V[s_next]
    return V

def mejorar_politica(V, policy):
    estable = True
    for s in states:
        mejores_valores = {}
        for a in actions:
            s_next, r = T[s][a]
            mejores_valores[a] = r + gamma * V[s_next]
        mejor_accion = max(mejores_valores, key=mejores_valores.get)
        if mejor_accion != policy[s]:
            policy[s] = mejor_accion
            estable = False
    return policy, estable

# Iteración de políticas
estable = False
while not estable:
    V = evaluar_politica(policy, V)
    policy, estable = mejorar_politica(V, policy)

print("Valores finales:", V)
print("Política óptima:", policy)
