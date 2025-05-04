eventos = [
    {"tiempo": 0, "llueve": False},
    {"tiempo": 1, "llueve": True},
    {"tiempo": 2, "llueve": True},
    {"tiempo": 3, "llueve": False}
]

def G(propiedad):
    return all(e[propiedad] for e in eventos)

def F(propiedad):
    return any(e[propiedad] for e in eventos)

def X(propiedad, t):
    if t + 1 < len(eventos):
        return eventos[t + 1][propiedad]
    return None

print("G(llueve):", G("llueve"))
print("F(llueve):", F("llueve"))
print("X(llueve, 1):", X("llueve", 1))
