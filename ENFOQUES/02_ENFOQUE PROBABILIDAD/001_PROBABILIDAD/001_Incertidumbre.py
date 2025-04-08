# Probabilidades base
P_enfermo = 0.01                        # P(E)
P_no_enfermo = 1 - P_enfermo           # P(¬E)

# Sensibilidad y especificidad
P_positivo_dado_enfermo = 0.99         # P(Pos | E)
P_positivo_dado_no_enfermo = 0.05      # P(Pos | ¬E)

# Probabilidad total de positivo (teorema de la probabilidad total)
P_positivo = (
    P_enfermo * P_positivo_dado_enfermo +
    P_no_enfermo * P_positivo_dado_no_enfermo
)

# Regla de Bayes: P(E | Pos)
P_enfermo_dado_positivo = (
    P_enfermo * P_positivo_dado_enfermo
) / P_positivo

# Imprimir resultado
print("Probabilidad de estar enfermo dado un resultado positivo:")
print(f"P(E | Positivo) = {P_enfermo_dado_positivo:.4f}")
