# Tablas de probabilidad condicional (simplificadas)
# Probabilidad marginal de que llueva
P_Rain = {True: 0.2, False: 0.8}

# Probabilidad condicional de que el aspersor esté encendido dado que llueve o no
P_Sprinkler_given_Rain = {
    True: {True: 0.01, False: 0.99},  # Si llueve
    False: {True: 0.4, False: 0.6}    # Si no llueve
}

# Probabilidad condicional de que el césped esté mojado dado el estado del aspersor y la lluvia
P_WetGrass_given_Sprinkler_Rain = {
    (True, True): {True: 0.99, False: 0.01},   # Aspersor encendido y llueve
    (True, False): {True: 0.9, False: 0.1},    # Aspersor encendido y no llueve
    (False, True): {True: 0.9, False: 0.1},    # Aspersor apagado y llueve
    (False, False): {True: 0.0, False: 1.0}    # Aspersor apagado y no llueve
}

# Función para realizar la eliminación de variables y calcular P(Rain | WetGrass=True)
def eliminar_variables():
    resultados = {}  # Diccionario para almacenar los resultados intermedios
    for rain in [True, False]:  # Iterar sobre los posibles valores de la variable Rain
        total = 0  # Acumulador para la probabilidad total
        for sprinkler in [True, False]:  # Iterar sobre los posibles valores de la variable Sprinkler
            # Obtener las probabilidades individuales
            p_rain = P_Rain[rain]
            p_sprinkler = P_Sprinkler_given_Rain[rain][sprinkler]
            p_wet = P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)][True]

            # Calcular la probabilidad conjunta y acumular
            total += p_rain * p_sprinkler * p_wet
        resultados[rain] = total  # Guardar el resultado para el valor actual de Rain

    # Normalizar las probabilidades para que sumen 1
    normalizador = sum(resultados.values())
    for clave in resultados:
        resultados[clave] /= normalizador

    return resultados  # Retornar las probabilidades normalizadas

# Ejecutamos la función y mostramos el resultado
print("P(Rain | WetGrass=True):", eliminar_variables())
