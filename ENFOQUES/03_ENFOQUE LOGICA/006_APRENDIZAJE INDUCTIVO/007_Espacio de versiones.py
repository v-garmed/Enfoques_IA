# Algoritmo AQ simplificado (no formal)

# Lista de ejemplos positivos, cada uno representado como un diccionario con atributos y valores
ejemplos_positivos = [
    {'color': 'rojo', 'forma': 'círculo'},
    {'color': 'rojo', 'forma': 'cuadrado'},
]

# Lista de ejemplos negativos, también representados como diccionarios
ejemplos_negativos = [
    {'color': 'azul', 'forma': 'círculo'},
    {'color': 'verde', 'forma': 'cuadrado'},
]

# Función para aprender una descripción general que cubra los ejemplos positivos
# y excluya los ejemplos negativos
def aprender_descripcion_general(positivos, negativos):
    # Inicializar la descripción general con la intersección de los atributos de los ejemplos positivos
    descripcion = {}
    for key in positivos[0].keys():  # Iterar sobre las claves (atributos) de los ejemplos
        # Obtener los valores del atributo actual en todos los ejemplos positivos
        valores = [e[key] for e in positivos]
        # Si todos los valores son iguales, incluir ese valor en la descripción
        if all(val == valores[0] for val in valores):
            descripcion[key] = valores[0]
        else:
            # Si los valores son diferentes, usar '?' como comodín
            descripcion[key] = '?'

    # Refinar la descripción eliminando condiciones que cubren ejemplos negativos
    for negativo in negativos:  # Iterar sobre los ejemplos negativos
        for key in descripcion:  # Revisar cada atributo en la descripción
            # Si un atributo específico coincide con un ejemplo negativo, generalizarlo a '?'
            if descripcion[key] != '?' and descripcion[key] == negativo[key]:
                descripcion[key] = '?'
    return descripcion  # Retornar la descripción general aprendida

# Generar la hipótesis basada en los ejemplos positivos y negativos
hipotesis = aprender_descripcion_general(ejemplos_positivos, ejemplos_negativos)

# Imprimir la hipótesis generada
print("Hipótesis generada:", hipotesis)
