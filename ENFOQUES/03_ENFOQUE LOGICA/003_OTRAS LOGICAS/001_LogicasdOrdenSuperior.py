# Predicados
def es_par(x): return x % 2 == 0
def es_menor_que_diez(x): return x < 10

# Lista de predicados
predicados = [es_par, es_menor_que_diez]

# Lógica de orden superior: ∀P, ∀x ∈ dominio: P(x) → True
def evaluar_lógica_orden_superior(dominio, predicados):
    resultados = {}
    for pred in predicados:
        resultados[pred.__name__] = [pred(x) for x in dominio]
    return resultados

dominio = list(range(1, 11))
resultados = evaluar_lógica_orden_superior(dominio, predicados)
print("Evaluación de predicados:", resultados)
