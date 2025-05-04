hechos = {
    "es_gato": True,
    "es_mudo": False
}

def maulla_por_defecto(hechos):
    if hechos.get("es_gato") and not hechos.get("es_mudo"):
        return "Maúlla"
    return "No maúlla"

print("¿El gato maúlla?:", maulla_por_defecto(hechos))
