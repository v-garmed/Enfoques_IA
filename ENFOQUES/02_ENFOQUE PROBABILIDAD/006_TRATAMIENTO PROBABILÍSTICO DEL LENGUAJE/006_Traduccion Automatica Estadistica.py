from collections import defaultdict

# Corpus bilingüe de entrenamiento (muy simple)
# Este es un conjunto de frases en español e inglés que se utilizará para entrenar el modelo de traducción.
corpus = [
    ("yo soy feliz", "i am happy"),
    ("yo estoy triste", "i am sad"),
    ("ella es feliz", "she is happy"),
    ("él está triste", "he is sad"),
]

# Conteo de traducciones palabra a palabra
# Se utiliza un diccionario anidado para contar las co-ocurrencias de palabras en español e inglés.
traducciones = defaultdict(lambda: defaultdict(int))

# Entrenamiento: contar co-ocurrencias
# Para cada par de frases en el corpus, se cuentan las co-ocurrencias de palabras entre las frases en español e inglés.
for esp, eng in corpus:
    esp_words = esp.split()  # Divide la frase en español en palabras individuales.
    eng_words = eng.split()  # Divide la frase en inglés en palabras individuales.
    for e in esp_words:  # Itera sobre cada palabra en español.
        for f in eng_words:  # Itera sobre cada palabra en inglés.
            traducciones[e][f] += 1  # Incrementa el conteo de co-ocurrencias.

# Crear modelo de probabilidad
# Se calcula la probabilidad de traducción de cada palabra en español a cada palabra en inglés.
modelo_traduccion = {}
for e, opciones in traducciones.items():
    total = sum(opciones.values())  # Suma total de co-ocurrencias para la palabra en español.
    modelo_traduccion[e] = {f: count / total for f, count in opciones.items()}  # Calcula la probabilidad.

# Función para traducir palabra por palabra usando máxima probabilidad
# Traduce una frase en español al inglés seleccionando la palabra con la mayor probabilidad de traducción.
def traducir(frase_esp):
    palabras = frase_esp.split()  # Divide la frase en español en palabras individuales.
    resultado = []
    for palabra in palabras:  # Itera sobre cada palabra en la frase.
        if palabra in modelo_traduccion:  # Si la palabra tiene traducción en el modelo.
            mejor_traduccion = max(modelo_traduccion[palabra], key=modelo_traduccion[palabra].get)  # Selecciona la traducción con mayor probabilidad.
            resultado.append(mejor_traduccion)  # Agrega la traducción al resultado.
        else:
            resultado.append("[?]")  # Si la palabra no está en el modelo, agrega un marcador de desconocido.
    return " ".join(resultado)  # Une las palabras traducidas en una frase.

# Ejemplo de uso
# Traduce una frase de ejemplo y muestra el resultado.
oracion = "yo estoy feliz"
print("Oración original:", oracion)
print("Traducción:", traducir(oracion))
