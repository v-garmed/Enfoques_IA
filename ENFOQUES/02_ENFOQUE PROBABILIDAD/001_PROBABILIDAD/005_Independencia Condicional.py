# Variables posibles
valores = ["Sí", "No"]

# Probabilidades condicionales simples (ficticias para el ejemplo)
P_lluvia = {"Sí": 0.3, "No": 0.7}
P_nublado_dado_lluvia = {
    "Sí": {"Sí": 0.8, "No": 0.2},
    "No": {"Sí": 0.3, "No": 0.7}
}
P_paraguas_dado_lluvia = {
    "Sí": {"Sí": 0.9, "No": 0.1},
    "No": {"Sí": 0.2, "No": 0.8}
}

# Queremos saber: ¿es independiente C (paraguas) de A (nublado), dado B (lluvia)?

print("¿P(C | A, B) == P(C | B)?\n")
for lluvia in valores:
    for nublado in valores:
        for paraguas in valores:
            # Calculamos ambas formas
            P_C_dado_AB = P_paraguas_dado_lluvia[lluvia][paraguas]  # depende solo de B
            P_C_dado_B = P_paraguas_dado_lluvia[lluvia][paraguas]    # también depende solo de B
            
            print(f"P(Paraguas={paraguas} | Nublado={nublado}, Lluvia={lluvia}) = {P_C_dado_AB}")
            print(f"P(Paraguas={paraguas} | Lluvia={lluvia})           = {P_C_dado_B}")
            print("---")
