# Tablas de probabilidad condicional (simplificadas)
P_Rain = {True: 0.2, False: 0.8}

P_Sprinkler_given_Rain = {
    True: {True: 0.01, False: 0.99},
    False: {True: 0.4, False: 0.6}
}

P_WetGrass_given_Sprinkler_Rain = {
    (True, True): {True: 0.99, False: 0.01},
    (True, False): {True: 0.9, False: 0.1},
    (False, True): {True: 0.9, False: 0.1},
    (False, False): {True: 0.0, False: 1.0}
}

def eliminar_variables():
    resultados = {}
    for rain in [True, False]:
        total = 0
        for sprinkler in [True, False]:
            p_rain = P_Rain[rain]
            p_sprinkler = P_Sprinkler_given_Rain[rain][sprinkler]
            p_wet = P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)][True]

            total += p_rain * p_sprinkler * p_wet
        resultados[rain] = total

    # Normalizar
    normalizador = sum(resultados.values())
    for clave in resultados:
        resultados[clave] /= normalizador

    return resultados

# Ejecutamos
print("P(Rain | WetGrass=True):", eliminar_variables())
