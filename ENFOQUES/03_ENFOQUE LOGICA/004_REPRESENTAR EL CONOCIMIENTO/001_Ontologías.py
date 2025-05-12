# Ontología básica como diccionario
# Se define una ontología simple utilizando un diccionario, donde las claves representan conceptos generales
# y los valores son listas de subconceptos relacionados.
ontologia = {
    "Animal": ["Perro", "Gato"],  # "Animal" tiene como subconceptos "Perro" y "Gato".
    "Perro": ["Labrador", "Pug"],  # "Perro" tiene como subconceptos "Labrador" y "Pug".
    "Gato": ["Persa", "Siamés"]  # "Gato" tiene como subconceptos "Persa" y "Siamés".
}

# Función para explorar jerarquía
# Esta función recorre y muestra la jerarquía de la ontología de forma recursiva.
# Recibe un concepto inicial y un nivel de profundidad para la indentación.
def mostrar_jerarquia(concepto, nivel=0):
    # Imprime el concepto actual con una indentación basada en el nivel de profundidad.
    print("  " * nivel + concepto)
    # Recorre los subconceptos del concepto actual (si existen) y los muestra recursivamente.
    for subconcepto in ontologia.get(concepto, []):
        mostrar_jerarquia(subconcepto, nivel + 1)

# Llamada a la función para mostrar la jerarquía de la ontología comenzando desde "Animal".
mostrar_jerarquia("Animal")
