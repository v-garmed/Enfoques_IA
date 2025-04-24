from itertools import product

# Definimos las probabilidades
P_C = {True: 0.6, False: 0.4}  # P(C)
P_S_dado_C = {
    True: {True: 0.9, False: 0.1},   # P(S | C=True)
    False: {True: 0.5, False: 0.5}   # P(S | C=False)
}

# Inference: P(C | S=True)
def enumeracion_inferencia():
    resultado = {}

    # Para cada valor posible de C
    for c_valor in [True, False]:
        # Probabilidad conjunta: P(C=c) * P(S=True | C=c)
        prob_c = P_C[c_valor]
        prob_s_dado_c = P_S_dado_C[c_valor][True]
        resultado[c_valor] = prob_c * prob_s_dado_c

    # Normalizamos
    total = sum(resultado.values())
    for clave in resultado:
        resultado[clave] /= total
    
    return resultado

# Ejecutamos
resultado_final = enumeracion_inferencia()
print("P(C | S=True):", resultado_final)
