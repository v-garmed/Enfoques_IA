from math import log2

def entropy(data):
    total = len(data)
    count_1 = sum(1 for row in data if row[-1] == 1)
    count_0 = total - count_1
    p1 = count_1 / total if count_1 else 0
    p0 = count_0 / total if count_0 else 0
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
