# Probabilidades dadas
P_A = 0.6                         # P(A)
P_B_given_A = 0.7                 # P(B | A)
P_C_given_AB = 0.9                # P(C | A, B)

# Aplicación de la regla de la cadena
# P(A, B, C) = P(A) * P(B|A) * P(C|A,B)
P_ABC = P_A * P_B_given_A * P_C_given_AB

# Mostrar resultado
print("Probabilidad conjunta P(A, B, C):", P_ABC)
print("Probabilidad de A:", P_A)
print("Probabilidad de B dado A:", P_B_given_A)
print("Probabilidad de C dado A y B:", P_C_given_AB)
print("Probabilidad de A y B y C:", P_ABC)
print("Probabilidad de A y B:", P_A * P_B_given_A)

# La regla de la cadena nos permite calcular la probabilidad conjunta de múltiples eventos