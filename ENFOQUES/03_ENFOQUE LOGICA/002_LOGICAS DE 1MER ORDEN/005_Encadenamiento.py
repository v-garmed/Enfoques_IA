# Hechos conocidos
hechos = {"llueve", "nublado"}

# Reglas
reglas = [
    (["llueve", "nublado"], "mojado"),
    (["mojado"], "resbaloso")
]

def encadenamiento_adelante(hechos, reglas):
    nuevos_hechos = hechos.copy()
    while True:
        cambios = False
        for condiciones, consecuencia in reglas:
            if set(condiciones).issubset(nuevos_hechos) and consecuencia not in nuevos_hechos:
                nuevos_hechos.add(consecuencia)
                cambios = True
        if not cambios:
            break
    return nuevos_hechos

print("Encadenamiento hacia adelante:", encadenamiento_adelante(hechos, reglas))
