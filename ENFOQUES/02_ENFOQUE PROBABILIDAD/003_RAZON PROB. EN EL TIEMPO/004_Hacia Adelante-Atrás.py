import numpy as np

# Estados ocultos
estados = ['Soleado', 'Lluvioso']
# Observaciones
observaciones = ['Sin paraguas', 'Con paraguas']

# Probabilidad inicial
P_inicial = np.array([0.6, 0.4])

# Matriz de transición de estados
P_transicion = np.array([
    [0.7, 0.3],  # Soleado → [Soleado, Lluvioso]
    [0.4, 0.6]   # Lluvioso → [Soleado, Lluvioso]
])

# Matriz de emisión: P(observación | estado)
P_emision = np.array([
    [0.9, 0.1],  # Soleado → [Sin paraguas, Con paraguas]
    [0.2, 0.8]   # Lluvioso → [Sin paraguas, Con paraguas]
])

# Observaciones (0: sin paraguas, 1: con paraguas)
obs = [1, 1, 0]

def forward(obs, P_ini, P_trans, P_emis):
    T = len(obs)
    N = len(P_ini)
    alpha = np.zeros((T, N))
    
    # Inicialización
    alpha[0] = P_ini * P_emis[:, obs[0]]
    alpha[0] = alpha[0] / np.sum(alpha[0])
    
    # Iteración hacia adelante
    for t in range(1, T):
        for j in range(N):
            alpha[t, j] = np.sum(alpha[t-1] * P_trans[:, j]) * P_emis[j, obs[t]]
        alpha[t] = alpha[t] / np.sum(alpha[t])
    
    return alpha

def backward(obs, P_trans, P_emis):
    T = len(obs)
    N = P_trans.shape[0]
    beta = np.zeros((T, N))
    
    # Inicialización
    beta[T-1] = np.ones(N)
    
    # Iteración hacia atrás
    for t in range(T-2, -1, -1):
        for i in range(N):
            beta[t, i] = np.sum(P_trans[i, :] * P_emis[:, obs[t+1]] * beta[t+1])
        beta[t] = beta[t] / np.sum(beta[t])
    
    return beta

def suavizado(obs, P_ini, P_trans, P_emis):
    alpha = forward(obs, P_ini, P_trans, P_emis)
    beta = backward(obs, P_trans, P_emis)
    posterior = alpha * beta
    posterior = posterior / np.sum(posterior, axis=1, keepdims=True)
    return posterior

# Ejecutamos suavizado
posterior_probs = suavizado(obs, P_inicial, P_transicion, P_emision)

# Mostramos resultados
print("Distribuciones de probabilidad suavizadas (por día):")
for t, dist in enumerate(posterior_probs):
    print(f"Día {t+1}: " + ", ".join(f"{estados[i]}: {round(p, 3)}" for i, p in enumerate(dist)))
