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

def likelihood_weighting(evidence, num_samples=10000):
    weights = []
    for _ in range(num_samples):
        weight = 1.0
        sample = {}

        # Sample Rain
        rain = random.choices([True, False], weights=[0.2, 0.8])[0]
        sample['Rain'] = rain

        # Sample Sprinkler given Rain
        sprinkler = random.choices([True, False],
            weights=[
                P_Sprinkler_given_Rain[rain][True],
                P_Sprinkler_given_Rain[rain][False]
            ])[0]
        sample['Sprinkler'] = sprinkler

        # WetGrass es evidencia, así que no se samplea
        if evidence['WetGrass'] is not None:
            prob = P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)][evidence['WetGrass']]
            weight *= prob
            sample['WetGrass'] = evidence['WetGrass']

        weights.append((sample, weight))

    # Contar pesos según Rain
    rain_true = sum(w for s, w in weights if s['Rain'] == True)
    rain_false = sum(w for s, w in weights if s['Rain'] == False)
    total = rain_true + rain_false
    return {
        'P(Rain=True|WetGrass=True)': rain_true / total,
        'P(Rain=False|WetGrass=True)': rain_false / total
    }

# Ejecutamos con evidencia WetGrass = True
print(likelihood_weighting({'WetGrass': True}))
