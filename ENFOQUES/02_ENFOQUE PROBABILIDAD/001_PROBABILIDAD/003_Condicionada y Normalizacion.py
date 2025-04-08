# Caso 1: Probabilidad condicionada con la regla de Bayes

# Probabilidad a priori de enfermedad
P_enfermo = 0.01
P_no_enfermo = 1 - P_enfermo

# Verosimilitud del test
P_positivo_dado_enfermo = 0.95
P_positivo_dado_no_enfermo = 0.1

# Evidencia total (probabilidad de obtener un resultado positivo)
P_positivo = (
    P_enfermo * P_positivo_dado_enfermo +
    P_no_enfermo * P_positivo_dado_no_enfermo
)

# Probabilidad condicionada: P(Enfermo | Positivo)
P_enfermo_dado_positivo = (
    P_enfermo * P_positivo_dado_enfermo
) / P_positivo

print(f"Probabilidad condicionada (enfermo | positivo): {P_enfermo_dado_positivo:.4f}")

# ---------------------------------------------------
# Caso 2: Normalización de hipótesis

# Supongamos que tenemos 3 hipótesis y sus valores proporcionales
valores_proporcionales = {
    "Hipotesis_A": 0.2,
    "Hipotesis_B": 0.5,
    "Hipotesis_C": 0.3
}

# Calculamos el total para normalizar
suma_total = sum(valores_proporcionales.values())

# Creamos un nuevo diccionario con probabilidades normalizadas
probabilidades_normalizadas = {
    k: v / suma_total for k, v in valores_proporcionales.items()
}

# Mostrar resultados
print("\nProbabilidades normalizadas:")
for h, p in probabilidades_normalizadas.items():
    print(f"{h}: {p:.2f}")
