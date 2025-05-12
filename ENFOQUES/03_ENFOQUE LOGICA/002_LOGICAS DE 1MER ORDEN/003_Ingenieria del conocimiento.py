# Base de conocimiento
# Este diccionario almacena categorías de animales y sus características.
conocimiento = {
    "mamifero": ["perro", "gato", "ballena"],  # Lista de animales que son mamíferos.
    "ave": ["paloma", "aguila"],              # Lista de animales que son aves.
    "puede_volar": ["paloma", "aguila"]       # Lista de animales que pueden volar.
}

# Función para verificar si un animal es mamífero.
# Devuelve True si el animal está en la lista de mamíferos, de lo contrario False.
def es_mamifero(animal):
    return animal in conocimiento["mamifero"]

# Función para verificar si un animal puede volar.
# Devuelve True si el animal está en la lista de animales que pueden volar, de lo contrario False.
def puede_volar(animal):
    return animal in conocimiento.get("puede_volar", [])  # Usa get para evitar errores si la clave no existe.

# Variable que almacena el nombre de un animal a verificar.
animal = "aguila"

# Imprime si el animal es mamífero.
print(f"{animal} es mamífero:", es_mamifero(animal))

# Imprime si el animal puede volar.
print(f"{animal} puede volar:", puede_volar(animal))
