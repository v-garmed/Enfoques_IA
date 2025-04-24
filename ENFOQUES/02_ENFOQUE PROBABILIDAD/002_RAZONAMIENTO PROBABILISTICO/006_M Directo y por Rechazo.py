import random

# Probabilidades base
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

def sample_prior():
    # Generar una muestra completa sin considerar evidencia
    rain = random.choices([True, False], weights=[0.2, 0.8])[0]
    sprinkler = random.choices([True, False], weights=[
        P_Sprinkler_given_Rain[rain][True],
        P_Sprinkler_given_Rain[rain][False]
    ])[0]
    wet = random.choices([True, False], weights=[
        P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)][True],
        P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)][False]
    ])[0]
    return {'Rain': rain, 'Sprinkler': sprinkler, 'WetGrass': wet}

def rejection_sampling(num_samples=10000):
    samples = []
    for _ in range(num_samples):
        sample = sample_prior()
        if sample['WetGrass'] == True:  # solo aceptamos muestras que coinciden con la evidencia
            samples.append(sample)
    
    # Contamos la frecuencia de Rain en las muestras aceptadas
    rain_true = sum(1 for s in samples if s['Rain'])
    rain_false = sum(1 for s in samples if not s['Rain'])
    total = rain_true + rain_false
    return {'P(Rain=True|WetGrass=True)': rain_true / total,
            'P(Rain=False|WetGrass=True)': rain_false / total}

# Ejecutamos el muestreo por rechazo
print(rejection_sampling())
