# Modelo modal simple con mundos posibles
mundos_posibles = {
    "m1": {"P": True},
    "m2": {"P": False},
    "m3": {"P": True}
}

def necesariamente(hecho):
    return all(mundo.get(hecho, False) for mundo in mundos_posibles.values())

def posiblemente(hecho):
    return any(mundo.get(hecho, False) for mundo in mundos_posibles.values())

print("□P:", necesariamente("P"))
print("◇P:", posiblemente("P"))
