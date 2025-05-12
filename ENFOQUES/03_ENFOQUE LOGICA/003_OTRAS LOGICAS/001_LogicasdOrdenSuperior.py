# Definición de predicados (funciones que evalúan condiciones específicas)
# Este predicado verifica si un número es par
def es_par(x): 
    return x % 2 == 0

# Este predicado verifica si un número es menor que diez
def es_menor_que_diez(x): 
    return x < 10

# Lista de predicados
# Aquí se agrupan los predicados definidos anteriormente en una lista
predicados = [es_par, es_menor_que_diez]

# Función para evaluar lógica de orden superior
# Esta función evalúa cada predicado en un dominio dado y devuelve los resultados
# Lógica: Para cada predicado P y cada elemento x en el dominio, se evalúa P(x)
def evaluar_lógica_orden_superior(dominio, predicados):
    resultados = {}  # Diccionario para almacenar los resultados de cada predicado
    for pred in predicados:  # Itera sobre cada predicado en la lista
        # Aplica el predicado a cada elemento del dominio y guarda los resultados
        resultados[pred.__name__] = [pred(x) for x in dominio]
    return resultados  # Devuelve el diccionario con los resultados

# Dominio de valores a evaluar
dominio = list(range(1, 11))  # Lista de números del 1 al 10

# Evaluación de los predicados sobre el dominio
resultados = evaluar_lógica_orden_superior(dominio, predicados)

# Imprime los resultados de la evaluación
print("Evaluación de predicados:", resultados)
