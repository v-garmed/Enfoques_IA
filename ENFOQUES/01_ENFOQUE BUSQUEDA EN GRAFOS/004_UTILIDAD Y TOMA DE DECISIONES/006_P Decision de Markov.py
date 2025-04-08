states = ['A', 'B', 'C']
actions = ['left', 'right']

# Función de transición y recompensas
T = {
    'A': {'left': {'A': 1.0}, 'right': {'B': 1.0}},
    'B': {'left': {'A': 1.0}, 'right': {'C': 1.0}},
    'C': {'left': {'B': 1.0}, 'right': {'C': 1.0}},
}

R = {
    'A': {'left': 0, 'right': 5},
    'B': {'left': 0, 'right': 10},
    'C': {'left': 0, 'right': 0}
}

# Mostrar posibles resultados de tomar acciones
for state in states:
    for action in actions:
        print(f"Desde estado {state}, acción '{action}':")
        for next_state, prob in T[state][action].items():
            reward = R[state][action]
            print(f" -> va a {next_state} con probabilidad {prob}, recompensa = {reward}")
        print()
# Mostrar la política óptima y los valores de los estados
print("Política óptima y valores de los estados:")
for state in states:
    best_action = max(actions, key=lambda a: R[state][a] + sum(T[state][a].get(next_state, 0) * R[next_state][a] for next_state in states))
    print(f"Estado {state}: Acción óptima = '{best_action}'")

