# Lista de eventos que representan un conjunto de estados en diferentes momentos de tiempo.
# Cada evento es un diccionario con un tiempo y una propiedad "llueve" que indica si está lloviendo.
eventos = [
    {"tiempo": 0, "llueve": False},
    {"tiempo": 1, "llueve": True},
    {"tiempo": 2, "llueve": True},
    {"tiempo": 3, "llueve": False}
]

# Función G (siempre): Verifica si una propiedad es verdadera en todos los eventos.
def G(propiedad):
    return all(e[propiedad] for e in eventos)

# Función F (eventualmente): Verifica si una propiedad es verdadera en al menos un evento.
def F(propiedad):
    return any(e[propiedad] for e in eventos)

# Función X (siguiente): Verifica el valor de una propiedad en el evento siguiente al tiempo dado.
# Si no hay un evento siguiente, devuelve None.
def X(propiedad, t):
    if t + 1 < len(eventos):  # Verifica si existe un evento siguiente.
        return eventos[t + 1][propiedad]  # Devuelve el valor de la propiedad en el siguiente evento.
    return None  # Si no hay un evento siguiente, devuelve None.

# Imprime si la propiedad "llueve" es verdadera en todos los eventos.
print("G(llueve):", G("llueve"))

# Imprime si la propiedad "llueve" es verdadera en al menos un evento.
print("F(llueve):", F("llueve"))

# Imprime el valor de la propiedad "llueve" en el evento siguiente al tiempo 1.
print("X(llueve, 1):", X("llueve", 1))
