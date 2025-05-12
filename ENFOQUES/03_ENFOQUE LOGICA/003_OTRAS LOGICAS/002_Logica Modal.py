# Modelo modal simple con mundos posibles
# Se define un diccionario que representa los mundos posibles y los valores de verdad de un hecho "P" en cada mundo.
mundos_posibles = {
    "m1": {"P": True},  # En el mundo "m1", el hecho "P" es verdadero.
    "m2": {"P": False}, # En el mundo "m2", el hecho "P" es falso.
    "m3": {"P": True}   # En el mundo "m3", el hecho "P" es verdadero.
}

# Función para verificar si un hecho es necesariamente verdadero (□P).
# Esto significa que el hecho debe ser verdadero en todos los mundos posibles.
def necesariamente(hecho):
    return all(mundo.get(hecho, False) for mundo in mundos_posibles.values())

# Función para verificar si un hecho es posiblemente verdadero (◇P).
# Esto significa que el hecho debe ser verdadero en al menos un mundo posible.
def posiblemente(hecho):
    return any(mundo.get(hecho, False) for mundo in mundos_posibles.values())

# Imprime si el hecho "P" es necesariamente verdadero (□P) y posiblemente verdadero (◇P).
print("□P:", necesariamente("P"))  # Verifica si "P" es verdadero en todos los mundos.
print("◇P:", posiblemente("P"))    # Verifica si "P" es verdadero en al menos un mundo.
