# Hechos y reglas como en Prolog
base_de_datos = {
    "padre": [("juan", "maria"), ("juan", "jose")],
    "madre": [("ana", "maria"), ("ana", "jose")]
}

def es_padre(x, y):
    return (x, y) in base_de_datos["padre"]

def es_madre(x, y):
    return (x, y) in base_de_datos["madre"]

def es_hijo(x, y):
    return es_padre(y, x) or es_madre(y, x)

print("¿Es maria hija de juan?", es_hijo("maria", "juan"))
