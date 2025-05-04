def temperatura_fuzzy(temp):
    if temp <= 20:
        return 0.0
    elif 20 < temp <= 30:
        return (temp - 20) / 10
    else:
        return 1.0

# Evaluación de temperaturas
for t in [18, 22, 25, 31]:
    print(f"Temperatura {t}°C: Calor difuso = {temperatura_fuzzy(t):.2f}")
