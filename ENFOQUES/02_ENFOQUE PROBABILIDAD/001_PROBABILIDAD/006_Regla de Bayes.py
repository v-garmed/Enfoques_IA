# Probabilidad de tener la enfermedad (P(E))
P_E = 0.01  # 1% de la población

# Probabilidad de NO tener la enfermedad (P(~E))
P_not_E = 1 - P_E  # 99%

# Probabilidad de dar positivo si se tiene la enfermedad (P(+|E)) => sensibilidad
P_pos_given_E = 0.99

# Probabilidad de dar positivo si NO se tiene la enfermedad (P(+|~E)) => falso positivo
P_pos_given_not_E = 1 - 0.95  # 5% de falsos positivos

# Probabilidad total de dar positivo (P(+))
P_pos = (P_pos_given_E * P_E) + (P_pos_given_not_E * P_not_E)

# Aplicamos la Regla de Bayes: P(E|+)
P_E_given_pos = (P_pos_given_E * P_E) / P_pos

# Mostramos resultados
print(f"Probabilidad de tener la enfermedad dado un test positivo: {P_E_given_pos:.4f} ({P_E_given_pos*100:.2f}%)")
