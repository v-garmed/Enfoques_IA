taxonomia = {
    "Vehículo": ["Terrestre", "Aéreo"],
    "Terrestre": ["Auto", "Moto"],
    "Aéreo": ["Avión", "Helicóptero"]
}

def buscar_categoria(objeto, taxonomia):
    for categoria, subcategorias in taxonomia.items():
        if objeto in subcategorias:
            return f"{objeto} es un tipo de {categoria}"
    return "Categoría no encontrada"

print(buscar_categoria("Helicóptero", taxonomia))
