# Base de conocimiento
conocimiento = {
    "mamifero": ["perro", "gato", "ballena"],
    "ave": ["paloma", "aguila"],
    "puede_volar": ["paloma", "aguila"]
}

def es_mamifero(animal):
    return animal in conocimiento["mamifero"]

def puede_volar(animal):
    return animal in conocimiento.get("puede_volar", [])

animal = "aguila"
print(f"{animal} es mamífero:", es_mamifero(animal))
print(f"{animal} puede volar:", puede_volar(animal))
