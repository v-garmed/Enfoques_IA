# Datos de entrenamiento
datos = [
    {'edad': 'joven',  'compra': 'sí'},
    {'edad': 'joven',  'compra': 'sí'},
    {'edad': 'adulto', 'compra': 'no'},
    {'edad': 'adulto', 'compra': 'no'},
    {'edad': 'joven',  'compra': 'sí'},
    {'edad': 'adulto', 'compra': 'sí'},
]

# Función para contar ocurrencias
def contar_ocurrencias(datos, atributo, valor, clase, clase_valor):
    return sum(1 for d in datos if d[atributo] == valor and d[clase] == clase_valor)

# Función para estimar probabilidad condicional P(edad=valor | compra=clase_valor)
def prob_condicional(datos, atributo, valor, clase, clase_valor):
    total_clase = sum(1 for d in datos if d[clase] == clase_valor)
    if total_clase == 0:
        return 0
    return contar_ocurrencias(datos, atributo, valor, clase, clase_valor) / total_clase

# Función para estimar P(clase)
def prob_clase(datos, clase, clase_valor):
    total = len(datos)
    ocurrencias = sum(1 for d in datos if d[clase] == clase_valor)
    return ocurrencias / total

# Clasificador Naive Bayes para una nueva persona
def clasificar(edad_input):
    clases = ['sí', 'no']
    probabilidades = {}

    for clase_valor in clases:
        p_clase = prob_clase(datos, 'compra', clase_valor)
        p_cond = prob_condicional(datos, 'edad', edad_input, 'compra', clase_valor)
        probabilidades[clase_valor] = p_clase * p_cond

    # Normalizar
    total = sum(probabilidades.values())
    for k in probabilidades:
        probabilidades[k] /= total

    return max(probabilidades, key=probabilidades.get), probabilidades

# Clasificamos un nuevo caso
resultado, probs = clasificar('joven')
print("Clasificación:", resultado)
print("Probabilidades:", probs)
