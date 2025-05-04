# Ontología básica como diccionario
ontologia = {
    "Animal": ["Perro", "Gato"],
    "Perro": ["Labrador", "Pug"],
    "Gato": ["Persa", "Siamés"]
}

# Función para explorar jerarquía
def mostrar_jerarquia(concepto, nivel=0):
    print("  " * nivel + concepto)
    for subconcepto in ontologia.get(concepto, []):
        mostrar_jerarquia(subconcepto, nivel + 1)

mostrar_jerarquia("Animal")
