# Base de conocimiento: si llueve, la calle se moja
KB = {
    "llueve": True,
    "llueve => mojado": lambda llueve: llueve
}

# Inferencia: ¿Está mojado?
if KB["llueve"] and KB["llueve => mojado"](KB["llueve"]):
    mojado = True
else:
    mojado = False

print("¿La calle está mojada?", mojado)
