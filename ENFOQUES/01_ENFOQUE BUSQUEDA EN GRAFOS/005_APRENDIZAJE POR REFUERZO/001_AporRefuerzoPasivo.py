import numpy as np

# Definimos el entorno
estados = [(0, 0), (0, 1), (0, 2),
           (1, 0), (1, 1), (1, 2),
           (2, 0), (2, 1), (2, 2)]
terminales = [(0, 2), (1, 2)]
recompensas = {
    (0, 2): 1,
    (1, 2): -1
}
gamma = 0.9

# Política pasiva fija: ir a la derecha si se puede, si no hacia abajo
def politica(s):
    x, y = s
    if y < 2:
        return (0, 1)  # derecha
    else:
        return (1, 0)  # abajo

# Inicializamos valores y visitas
valores = {s: 0 for s in estados}
cuentas = {s: 0 for s in estados}

# Simulamos episodios
for episodio in range(1000):
    s = (0, 0)
    trayectoria = []
    while s not in terminales:
        a = politica(s)
        siguiente = (s[0] + a[0], s[1] + a[1])
        r = recompensas.get(siguiente, 0)
        trayectoria.append((s, r))
        s = siguiente
    # Propagamos valores hacia atrás
    G = 0
    for s, r in reversed(trayectoria):
        G = r + gamma * G
        cuentas[s] += 1
        valores[s] += (G - valores[s]) / cuentas[s]  # Promedio incremental

# Mostramos utilidades estimadas
print("Utilidades estimadas por estado:")
for s in sorted(valores.keys()):
    print(f"{s}: {round(valores[s], 3)}")
