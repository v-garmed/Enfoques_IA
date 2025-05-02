from collections import defaultdict, Counter
import re

# Corpus: texto de ejemplo
corpus = """
me gusta el chocolate
me gusta el helado
el helado es delicioso
el chocolate es dulce
me gusta el dulce
"""

# Preprocesamiento: tokenización en palabras
palabras = re.findall(r'\b\w+\b', corpus.lower())

# Contar la frecuencia de cada palabra y par de palabras (bigramas)
frecuencia_unigramas = Counter(palabras)
frecuencia_bigramas = defaultdict(int)

for i in range(len(palabras) - 1):
    par = (palabras[i], palabras[i+1])
    frecuencia_bigramas[par] += 1

# Calcular la probabilidad condicional P(palabra2 | palabra1)
def probabilidad_condicional(palabra1, palabra2):
    bigrama = (palabra1, palabra2)
    if frecuencia_unigramas[palabra1] == 0:
        return 0
    return frecuencia_bigramas[bigrama] / frecuencia_unigramas[palabra1]

# Ejemplo de uso
palabra1 = "me"
palabra2 = "gusta"
print(f"P({palabra2} | {palabra1}) =", probabilidad_condicional(palabra1, palabra2))
