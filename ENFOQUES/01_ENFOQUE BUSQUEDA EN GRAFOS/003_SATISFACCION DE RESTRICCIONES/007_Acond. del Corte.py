from itertools import product

# Dominio de cada variable
dominios = {
    'A': [1, 2],
    'B': [1, 2],
    'C': [1, 2],
    'D': [1, 2]
}

# Restricciones entre variables
restricciones = {
    ('A', 'B'): lambda a, b: a != b,
    ('B', 'C'): lambda b, c: b != c,
    ('C', 'D'): lambda c, d: c != d,
    ('D', 'A'): lambda d, a: d != a  # Crea el ciclo
}

# Eliminar ciclo usando el conjunto de corte {'A'}
cutset = ['A']

def es_valida(asignacion, restricciones):
    for (var1, var2), restriccion in restricciones.items():
        if var1 in asignacion and var2 in asignacion:
            if not restriccion(asignacion[var1], asignacion[var2]):
                return False
    return True

# Probar todas las combinaciones posibles del conjunto de corte
for valores_cutset in product(*[dominios[v] for v in cutset]):
    asignacion = dict(zip(cutset, valores_cutset))
    
    # Resolver el resto del problema como si fuera un árbol
    for b in dominios['B']:
        for c in dominios['C']:
            for d in dominios['D']:
                asignacion_completa = {**asignacion, 'B': b, 'C': c, 'D': d}
                if es_valida(asignacion_completa, restricciones):
                    print("Solución encontrada:", asignacion_completa)
