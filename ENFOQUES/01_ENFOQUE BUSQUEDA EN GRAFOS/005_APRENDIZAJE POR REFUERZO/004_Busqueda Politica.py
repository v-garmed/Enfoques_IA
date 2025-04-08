import numpy as np

# Definimos el entorno: 1D con 5 estados y la meta en el estado 4
num_states = 5
goal_state = 4

# Dos acciones: 0 = izquierda, 1 = derecha
num_actions = 2

# Inicializamos parámetros aleatorios para la política (matriz estados x acciones)
policy_params = np.random.rand(num_states, num_actions)

# Función softmax para convertir parámetros en probabilidades
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

# Definimos la política estocástica usando softmax
def get_action_probs(state):
    return softmax(policy_params[state])

# Simula un episodio en el entorno, devuelve el historial
def simulate_episode():
    state = 0
    trajectory = []
    while state != goal_state:
        probs = get_action_probs(state)
        action = np.random.choice(num_actions, p=probs)
        next_state = state + 1 if action == 1 else max(0, state - 1)
        reward = 1 if next_state == goal_state else 0
        trajectory.append((state, action, reward))
        state = next_state
    return trajectory

# Entrenamiento de la política usando REINFORCE
learning_rate = 0.1
for episode in range(500):
    trajectory = simulate_episode()
    for state, action, reward in trajectory:
        probs = get_action_probs(state)
        grad = -probs
        grad[action] += 1
        # Ajustamos los parámetros hacia la acción que llevó al objetivo
        policy_params[state] += learning_rate * reward * grad

# Evaluamos la política entrenada
print("\nPolítica aprendida (probabilidades de moverse a la derecha):")
for s in range(num_states):
    print(f"Estado {s}: {get_action_probs(s)[1]:.2f}")
