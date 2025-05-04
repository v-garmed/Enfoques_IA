# Dominio: conjunto de personas
dominio = ["Socrates", "Platon", "Aristoteles"]

# Propiedades
humanos = {"Socrates": True, "Platon": True, "Aristoteles": True}
mortales = {"Socrates": True, "Platon": True, "Aristoteles": True}

# Cuantificador Universal: ∀x (Humano(x) → Mortal(x))
def cuantificador_universal(dominio, humanos, mortales):
    for persona in dominio:
        if humanos[persona] and not mortales[persona]:
            return False
    return True

# Cuantificador Existencial: ∃x (Humano(x) ∧ Científico(x))
cientificos = {"Socrates": False, "Platon": False, "Aristoteles": True}

def cuantificador_existencial(dominio, humanos, cientificos):
    for persona in dominio:
        if humanos[persona] and cientificos[persona]:
            return True
    return False

print("∀x (Humano(x) → Mortal(x)):", cuantificador_universal(dominio, humanos, mortales))
print("∃x (Humano(x) ∧ Científico(x)):", cuantificador_existencial(dominio, humanos, cientificos))
