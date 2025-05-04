# Red semántica simple
red = {
    "mamífero": ["perro", "gato"],
    "perro": ["ladrar"],
    "gato": ["maullar"]
}

def mostrar_red(concepto):
    if concepto in red:
        return f"{concepto} está relacionado con: {', '.join(red[concepto])}"
    return "No encontrado"

print(mostrar_red("perro"))
