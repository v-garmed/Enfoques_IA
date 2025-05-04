# Algoritmo AQ simplificado (no formal)
ejemplos_positivos = [
    {'color': 'rojo', 'forma': 'círculo'},
    {'color': 'rojo', 'forma': 'cuadrado'},
]

ejemplos_negativos = [
    {'color': 'azul', 'forma': 'círculo'},
    {'color': 'verde', 'forma': 'cuadrado'},
]

def aprender_descripcion_general(positivos, negativos):
    # Inicializar con la intersección de los positivos
    descripcion = {}
    for key in positivos[0].keys():
        valores = [e[key] for e in positivos]
        if all(val == valores[0] for val in valores):
            descripcion[key] = valores[0]
        else:
            descripcion[key] = '?'

    # Eliminar condiciones que cubren negativos
    for negativo in negativos:
        for key in descripcion:
            if descripcion[key] != '?' and descripcion[key] == negativo[key]:
                descripcion[key] = '?'
    return descripcion

hipotesis = aprender_descripcion_general(ejemplos_positivos, ejemplos_negativos)
print("Hipótesis generada:", hipotesis)
