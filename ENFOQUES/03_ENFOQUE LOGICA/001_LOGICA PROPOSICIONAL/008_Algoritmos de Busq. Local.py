import random

# Función de evaluación
def f(x): return -x**2 + 4

def ascenso_colinas():
    x = random.uniform(-3, 3)
    for _ in range(100):
        vecino = x + random.uniform(-0.1, 0.1)
        if f(vecino) > f(x):
            x = vecino
    return x, f(x)

sol = ascenso_colinas()
print("Máximo aproximado en:", sol)
