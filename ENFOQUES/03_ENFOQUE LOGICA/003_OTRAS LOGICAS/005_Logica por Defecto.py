# Diccionario que contiene los hechos o características del animal
hechos = {
    "es_gato": True,  # Indica si el animal es un gato
    "es_mudo": False  # Indica si el animal es mudo
}

# Función que determina si el animal maúlla por defecto
def maulla_por_defecto(hechos):
    # Verifica si el animal es un gato y no es mudo
    if hechos.get("es_gato") and not hechos.get("es_mudo"):
        return "Maúlla"  # Si cumple las condiciones, devuelve "Maúlla"
    return "No maúlla"  # Si no cumple, devuelve "No maúlla"

# Imprime el resultado de la función indicando si el gato maúlla o no
print("¿El gato maúlla?:", maulla_por_defecto(hechos))
