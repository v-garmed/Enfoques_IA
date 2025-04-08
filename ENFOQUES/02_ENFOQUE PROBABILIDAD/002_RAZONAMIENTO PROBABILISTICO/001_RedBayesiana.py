# Definimos las probabilidades previas (P(G))
P_G = {
    "Sí": 0.1,   # 10% de tener gripe
    "No": 0.9    # 90% de no tener gripe
}

# P(Fiebre | Gripe)
P_F_given_G = {
    "Sí": {"Sí": 0.8, "No": 0.2},
    "No": {"Sí": 0.3, "No": 0.7}
}

# P(Tos | Gripe)
P_T_given_G = {
    "Sí": {"Sí": 0.9, "No": 0.1},
    "No": {"Sí": 0.2, "No": 0.8}
}

# Queremos calcular P(G=Sí | F=Sí, T=Sí)

# Paso 1: Calcular numerador de la regla de Bayes
numerador_si = (
    P_G["Sí"] * 
    P_F_given_G["Sí"]["Sí"] * 
    P_T_given_G["Sí"]["Sí"]
)

# Paso 2: Calcular numerador para G=No
numerador_no = (
    P_G["No"] * 
    P_F_given_G["No"]["Sí"] * 
    P_T_given_G["No"]["Sí"]
)

# Paso 3: Calcular denominador (normalización)
denominador = numerador_si + numerador_no

# Paso 4: Probabilidades posteriores normalizadas
P_G_si_dado_FT = numerador_si / denominador
P_G_no_dado_FT = numerador_no / denominador

# Resultado
print(f"Probabilidad de tener gripe dado fiebre y tos: {P_G_si_dado_FT:.4f} ({P_G_si_dado_FT*100:.2f}%)")
print(f"Probabilidad de NO tener gripe dado fiebre y tos: {P_G_no_dado_FT:.4f} ({P_G_no_dado_FT*100:.2f}%)")
