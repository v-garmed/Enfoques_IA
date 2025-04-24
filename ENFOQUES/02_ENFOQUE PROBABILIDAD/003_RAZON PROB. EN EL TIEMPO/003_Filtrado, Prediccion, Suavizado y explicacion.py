import numpy as np

# Estados ocultos (el clima): Soleado (0), Lluvioso (1)
# Observaciones: No lleva paraguas (0), Lleva paraguas (1)
estados = ['Soleado', 'Lluvioso']
observaciones = ['Sin paraguas', 'Con paraguas']

# Probabilidades iniciales
P_inicial = np.array([0.6, 0.4])

# Transición: P(estado_t | estado_t-1)
P_transicion = np.array([
    [0.7, 0.3],  # Soleado → [Soleado, Lluvioso]
    [0.4, 0.6]   # Lluvioso → [Soleado, Lluvioso]
])

# Emisión: P(obs | estado)
P_emision = np.array([
    [0.9, 0.1],  # Soleado → [Sin paraguas, Con paraguas]
    [0.2, 0.8]   # Lluvioso → [Sin paraguas, Con paraguas]
])

# Observaciones (solo vemos si lleva paraguas)
observed = [1, 1, 0]  # 3 días: Con, Con, Sin

# Algoritmo de filtrado (Forward)
def filtro_hmm(observaciones, P_inicial, P_trans, P_emis):
    belief = P_inicial
    for o in observaciones:
        # Predicción: nuevo belief sin observar
        pred = np.dot(belief, P_trans)
        # Actualización con observación
        belief = pred * P_emis[:, o]
        # Normalización
        belief = belief / np.sum(belief)
    return belief

resultado = filtro_hmm(observed, P_inicial, P_transicion, P_emision)
print("Distribución del estado oculto actual (filtrado):")
print({estados[i]: round(p, 3) for i, p in enumerate(resultado)})
