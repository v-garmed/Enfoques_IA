# Supuestos: relación "padre"
positivos = [
    ('juan', 'ana'),
    ('juan', 'carlos')
]

negativos = [
    ('ana', 'juan'),
    ('carlos', 'juan')
]

def inducir_regla_padre(positivos, negativos):
    # FOIL simulado: encontrar patrón común
    reglas = set()
    for padre, hijo in positivos:
        reglas.add(f"padre({padre}, {hijo}) :- humano({padre}), humano({hijo}), progenitor({padre}, {hijo})")
    return reglas

reglas = inducir_regla_padre(positivos, negativos)
print("Reglas inducidas:")
for r in reglas:
    print(r)
