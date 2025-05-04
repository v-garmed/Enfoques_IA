# Base de reglas
reglas = {
    'Q': lambda hechos: 'P' in hechos,
    'R': lambda hechos: 'Q' in hechos
}

def encadenamiento_adelante(hechos, objetivo):
    inferencias = set(hechos)
    while objetivo not in inferencias:
        cambios = False
        for concl, regla in reglas.items():
            if concl not in inferencias and regla(inferencias):
                inferencias.add(concl)
                cambios = True
        if not cambios:
            break
    return objetivo in inferencias

def encadenamiento_atras(objetivo, hechos):
    if objetivo in hechos:
        return True
    if objetivo not in reglas:
        return False
    return reglas[objetivo](hechos)

hechos = {'P'}
print("Adelante:", encadenamiento_adelante(hechos, 'R'))
print("Atrás:", encadenamiento_atras('R', hechos))
