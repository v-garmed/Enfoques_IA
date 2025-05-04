def oracion(palabras):
    if sustantivo(palabras[0]) and verbo(palabras[1]):
        return True
    return False

def sustantivo(p):
    return p in ["Juan", "Ana", "Perro"]

def verbo(p):
    return p in ["corre", "salta", "come"]

print(oracion(["Juan", "corre"]))  # True
print(oracion(["Perro", "baila"])) # False
