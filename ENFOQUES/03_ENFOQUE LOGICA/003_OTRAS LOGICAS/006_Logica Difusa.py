# Función para calcular el grado de "calor difuso" basado en una temperatura dada
def temperatura_fuzzy(temp):
    # Si la temperatura es menor o igual a 20°C, el calor difuso es 0.0 (frío)
    if temp <= 20:
        return 0.0
    # Si la temperatura está entre 20°C y 30°C, el calor difuso aumenta linealmente
    elif 20 < temp <= 30:
        return (temp - 20) / 10
    # Si la temperatura es mayor a 30°C, el calor difuso es 1.0 (calor máximo)
    else:
        return 1.0

# Evaluación de varias temperaturas para calcular su grado de calor difuso
for t in [18, 22, 25, 31]:
    # Imprime la temperatura y su correspondiente valor de calor difuso
    print(f"Temperatura {t}°C: Calor difuso = {temperatura_fuzzy(t):.2f}")
