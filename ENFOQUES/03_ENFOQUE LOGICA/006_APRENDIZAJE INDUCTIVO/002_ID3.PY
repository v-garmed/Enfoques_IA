from math import log2

# Función para calcular la entropía de un conjunto de datos
def entropy(data):
    # Total de elementos en los datos
    total = len(data)
    
    # Contar cuántos elementos tienen la etiqueta 1
    count_1 = sum(1 for row in data if row[-1] == 1)
    
    # Contar cuántos elementos tienen la etiqueta 0
    count_0 = total - count_1
    
    # Calcular la probabilidad de que la etiqueta sea 1
    p1 = count_1 / total if count_1 else 0
    
    # Calcular la probabilidad de que la etiqueta sea 0
    p0 = count_0 / total if count_0 else 0
    
    # Calcular y devolver la entropía usando la fórmula de Shannon
    # Si alguna probabilidad es 0, la entropía es 0
    return -p1*log2(p1) - p0*log2(p0) if p1 and p0 else 0

# Datos: [sol, lluvia, jugar]
data = [
    ['sol', 1],
    ['sol', 1],
    ['lluvia', 0],
    ['sol', 1],
    ['lluvia', 0]
]

print("Entropía:", entropy(data))
