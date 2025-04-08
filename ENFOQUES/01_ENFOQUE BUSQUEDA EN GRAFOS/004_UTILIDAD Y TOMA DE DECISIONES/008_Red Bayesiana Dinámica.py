# Estados posibles
weather_states = ["Soleado", "Lluvioso"]
umbrella_states = ["No", "Sí"]

# Probabilidad inicial P(Weather_0)
P_Weather_0 = {
    "Soleado": 0.7,
    "Lluvioso": 0.3
}

# Probabilidad condicional P(Umbrella_t | Weather_t)
P_Umbrella_given_Weather = {
    "Soleado": {"Sí": 0.1, "No": 0.9},
    "Lluvioso": {"Sí": 0.8, "No": 0.2}
}

# Probabilidad de transición P(Weather_t+1 | Weather_t)
P_Weather_next_given_current = {
    "Soleado": {"Soleado": 0.8, "Lluvioso": 0.2},
    "Lluvioso": {"Soleado": 0.3, "Lluvioso": 0.7}
}

# Evidencia observada: Umbrella_1 = "Sí"
evidence_umbrella_1 = "Sí"

# Calculamos P(Weather_1 | Umbrella_1 = "Sí") usando inferencia
def inference_weather_1(evidence):
    probs = {}
    for w1 in weather_states:
        total = 0
        for w0 in weather_states:
            # P(W0) * P(W1 | W0)
            pw0 = P_Weather_0[w0]
            pw1_given_w0 = P_Weather_next_given_current[w0][w1]
            total += pw0 * pw1_given_w0
        # P(U1 | W1) * total
        p_umbrella_given_w1 = P_Umbrella_given_Weather[w1][evidence]
        probs[w1] = p_umbrella_given_w1 * total

    # Normalizar para obtener una distribución de probabilidad
    total_prob = sum(probs.values())
    for k in probs:
        probs[k] /= total_prob

    return probs

# Ejecutar inferencia
resultado = inference_weather_1(evidence_umbrella_1)
print("P(Weather_1 | Umbrella_1 = 'Sí'):")
for estado, prob in resultado.items():
    print(f"{estado}: {prob:.4f}")
