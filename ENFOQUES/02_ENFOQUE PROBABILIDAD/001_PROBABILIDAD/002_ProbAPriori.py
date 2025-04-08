# Probabilidad a priori de tener la enfermedad (hipótesis)
P_enfermo = 0.01  # Solo el 1% de la población está enferma

# Probabilidad de NO estar enfermo
P_no_enfermo = 1 - P_enfermo

# Verosimilitudes:
# Probabilidad de dar positivo si está enfermo
P_positivo_dado_enfermo = 0.95

# Probabilidad de dar positivo si NO está enfermo (falsos positivos)
P_positivo_dado_no_enfermo = 0.1

# Evidencia total: P(Positivo)
# Usamos la ley de la probabilidad total
P_positivo = (
    P_enfermo * P_positivo_dado_enfermo +
    P_no_enfermo * P_positivo_dado_no_enfermo
)

# Aplicamos la Regla de Bayes para obtener la probabilidad posterior
P_enfermo_dado_positivo = (
    P_enfermo * P_positivo_dado_enfermo
) / P_positivo

# Mostrar el resultado
print("Probabilidad a priori de estar enfermo:", P_enfermo)
print("Probabilidad de estar enfermo dado un test positivo (posterior):")
print(f"P(Enfermo | Positivo) = {P_enfermo_dado_positivo:.4f}")
