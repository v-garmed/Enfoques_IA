from collections import defaultdict

# Corpus bilingüe de entrenamiento (muy simple)
corpus = [
    ("yo soy feliz", "i am happy"),
    ("yo estoy triste", "i am sad"),
    ("ella es feliz", "she is happy"),
    ("él está triste", "he is sad"),
]

# Conteo de traducciones palabra a palabra
traducciones = defaultdict(lambda: defaultdict(int))

# Entrenamiento: contar co-ocurrencias
for esp, eng in corpus:
    esp_words = esp.split()
    eng_words = eng.split()
    for e in esp_words:
        for f in eng_words:
            traducciones[e][f] += 1

# Crear modelo de probabilidad
modelo_traduccion = {}
for e, opciones in traducciones.items():
    total = sum(opciones.values())
    modelo_traduccion[e] = {f: count / total for f, count in opciones.items()}

# Función para traducir palabra por palabra usando máxima probabilidad
def traducir(frase_esp):
    palabras = frase_esp.split()
    resultado = []
    for palabra in palabras:
        if palabra in modelo_traduccion:
            mejor_traduccion = max(modelo_traduccion[palabra], key=modelo_traduccion[palabra].get)
            resultado.append(mejor_traduccion)
        else:
            resultado.append("[?]")  # palabra no conocida
    return " ".join(resultado)

# Ejemplo de uso
oracion = "yo estoy feliz"
print("Oración original:", oracion)
print("Traducción:", traducir(oracion))
