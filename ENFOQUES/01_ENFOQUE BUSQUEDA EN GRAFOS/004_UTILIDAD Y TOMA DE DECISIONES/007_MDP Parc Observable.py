import random

states = ['A', 'B']
actions = ['move']
observations = ['sensor_A', 'sensor_B']

T = {
    'A': {'move': 'B'},
    'B': {'move': 'A'}
}

O = {
    'A': {'sensor_A': 0.8, 'sensor_B': 0.2},
    'B': {'sensor_A': 0.3, 'sensor_B': 0.7}
}

# Inicializamos una creencia uniforme
belief = {'A': 0.5, 'B': 0.5}

def update_belief(belief, action, observation):
    new_belief = {}
    for s in states:
        prev_state = T[s][action]
        prob_obs = O[s][observation]
        new_belief[s] = belief[prev_state] * prob_obs
    # Normalizamos
    total = sum(new_belief.values())
    for s in states:
        new_belief[s] /= total
    return new_belief

# Simulación
observation = 'sensor_A'
belief = update_belief(belief, 'move', observation)
print("Nueva creencia del estado:", belief)
