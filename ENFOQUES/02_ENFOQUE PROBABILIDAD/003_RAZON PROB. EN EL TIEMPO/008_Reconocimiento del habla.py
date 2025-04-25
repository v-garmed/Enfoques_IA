import math

# Función log con verificación de cero
def safe_log(x):
    return math.log(x) if x > 0 else float('-inf')

# Modelo HMM simple: transiciones y emisiones
class SimpleHMM:
    def __init__(self, states, observations, start_prob, trans_prob, emit_prob):
        self.states = states
        self.observations = observations
        self.start_prob = start_prob
        self.trans_prob = trans_prob
        self.emit_prob = emit_prob

    def evaluate(self, obs_seq):
        # Algoritmo de Forward (con log-probabilidades)
        alpha = [{}]

        # Inicialización
        for state in self.states:
            alpha[0][state] = safe_log(self.start_prob[state]) + safe_log(self.emit_prob[state].get(obs_seq[0], 0))

        # Recursión
        for t in range(1, len(obs_seq)):
            alpha.append({})
            for curr in self.states:
                max_prob = float('-inf')
                for prev in self.states:
                    prob = alpha[t-1][prev] + safe_log(self.trans_prob[prev][curr])
                    if prob > max_prob:
                        max_prob = prob
                alpha[t][curr] = max_prob + safe_log(self.emit_prob[curr].get(obs_seq[t], 0))

        # Terminación
        final_probs = [alpha[-1][s] for s in self.states]
        return max(final_probs)  # log-probabilidad

# Definimos los modelos para "hola" y "adios"
states = ['S1', 'S2', 'S3', 'S4']

# Observaciones para cada palabra
obs_hola = [0, 1, 2, 3]   # h o l a
obs_adios = [4, 5, 6, 7, 8] # a d i o s

# Probabilidades para "hola"
start_hola = {'S1': 1.0, 'S2': 0, 'S3': 0, 'S4': 0}
trans_hola = {
    'S1': {'S2': 1.0, 'S1': 0, 'S3': 0, 'S4': 0},
    'S2': {'S3': 1.0, 'S1': 0, 'S2': 0, 'S4': 0},
    'S3': {'S4': 1.0, 'S1': 0, 'S2': 0, 'S3': 0},
    'S4': {'S4': 1.0, 'S1': 0, 'S2': 0, 'S3': 0},
}
emit_hola = {
    'S1': {0: 1.0},  # h
    'S2': {1: 1.0},  # o
    'S3': {2: 1.0},  # l
    'S4': {3: 1.0},  # a
}

# Probabilidades para "adios"
start_adios = {'S1': 1.0, 'S2': 0, 'S3': 0, 'S4': 0}
trans_adios = {
    'S1': {'S2': 1.0, 'S1': 0, 'S3': 0, 'S4': 0},
    'S2': {'S3': 1.0, 'S1': 0, 'S2': 0, 'S4': 0},
    'S3': {'S4': 1.0, 'S1': 0, 'S2': 0, 'S3': 0},
    'S4': {'S4': 1.0, 'S1': 0, 'S2': 0, 'S3': 0},
}
emit_adios = {
    'S1': {4: 1.0},  # a
    'S2': {5: 1.0},  # d
    'S3': {6: 1.0},  # i
    'S4': {7: 0.5, 8: 0.5},  # o y s
}

# Creamos ambos modelos
hmm_hola = SimpleHMM(states, obs_hola, start_hola, trans_hola, emit_hola)
hmm_adios = SimpleHMM(states, obs_adios, start_adios, trans_adios, emit_adios)

# Evaluamos una secuencia observada
test_sequence = [0, 1, 2, 3]  # h o l a

prob_hola = hmm_hola.evaluate(test_sequence)
prob_adios = hmm_adios.evaluate(test_sequence)

print("Log-probabilidad HMM 'hola':", prob_hola)
print("Log-probabilidad HMM 'adios':", prob_adios)

if prob_hola > prob_adios:
    print("Resultado: ¡Probablemente dijo 'hola'!")
else:
    print("Resultado: ¡Probablemente dijo 'adios'!")
