# Definimos un diccionario llamado 'taxonomia' que representa una jerarquía de categorías y subcategorías.
taxonomia = {
    "Vehículo": ["Terrestre", "Aéreo"],  # 'Vehículo' tiene dos subcategorías: 'Terrestre' y 'Aéreo'.
    "Terrestre": ["Auto", "Moto"],       # 'Terrestre' tiene dos subcategorías: 'Auto' y 'Moto'.
    "Aéreo": ["Avión", "Helicóptero"]    # 'Aéreo' tiene dos subcategorías: 'Avión' y 'Helicóptero'.
}

# Definimos una función llamada 'buscar_categoria' que busca la categoría principal de un objeto dado.
def buscar_categoria(objeto, taxonomia):
    # Iteramos sobre las categorías y sus subcategorías en el diccionario 'taxonomia'.
    for categoria, subcategorias in taxonomia.items():
        # Si el objeto se encuentra en las subcategorías de la categoría actual, devolvemos un mensaje.
        if objeto in subcategorias:
            return f"{objeto} es un tipo de {categoria}"
    # Si no se encuentra el objeto en ninguna categoría, devolvemos un mensaje indicando que no se encontró.
    return "Categoría no encontrada"

# Llamamos a la función 'buscar_categoria' con el objeto "Helicóptero" y la taxonomía definida.
# Imprimimos el resultado de la búsqueda.
print(buscar_categoria("Helicóptero", taxonomia))
