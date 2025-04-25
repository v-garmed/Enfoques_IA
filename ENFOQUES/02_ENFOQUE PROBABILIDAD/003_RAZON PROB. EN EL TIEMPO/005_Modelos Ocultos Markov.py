import numpy as np

# Definimos los estados ocultos y observaciones
estados = ['Soleado', 'Lluvioso']
observaciones = ['Sin paraguas', 'Con paraguas']

# Probabilidad inicial
P_inicial = np.array([0.6, 0.4])  # P(Soleado), P(Lluvioso)

# Matriz de transición entre estados ocultos
P_transicion = np.array([
    [0.7, 0.3],  # Soleado → [Soleado, Lluvioso]
    [0.4, 0.6]   # Lluvioso → [Soleado, Lluvioso]
])

# Matriz de emisión (probabilidad de observación dado el estado)
P_emision = np.array([
    [0.9, 0.1],  # Soleado → [Sin paraguas, Con paraguas]
    [0.2, 0.8]   # Lluvioso → [Sin paraguas, Con paraguas]
])

# Observaciones reales registradas (0 = sin paraguas, 1 = con paraguas)
obs = [1, 1, 0]

# Algoritmo hacia adelante
def forward(obs, P_ini, P_trans, P_emis):
    T = len(obs)
    N = len(P_ini)
    alpha = np.zeros((T, N))
    
    # Inicialización
    alpha[0] = P_ini * P_emis[:, obs[0]]
    alpha[0] /= np.sum(alpha[0])
    
    # Iteración
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = np.sum(alpha[t-1] * P_trans[:, j]) * P_emis[j, obs[t]]
        alpha[t] /= np.sum(alpha[t])
    
    return alpha

# Ejecutamos el algoritmo hacia adelante
resultados = forward(obs, P_inicial, P_transicion, P_emision)

# Mostrar resultados
print("Probabilidades estimadas del clima (por día):")
for t, dist in enumerate(resultados):
    print(f"Día {t+1}: " + ", ".join(f"{estados[i]}: {round(p, 3)}" for i, p in enumerate(dist)))
