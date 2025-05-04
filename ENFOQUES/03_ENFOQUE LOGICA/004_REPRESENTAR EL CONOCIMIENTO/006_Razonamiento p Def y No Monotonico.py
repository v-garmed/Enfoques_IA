hechos = {
    "es_ave": True,
    "es_avestruz": True  # contradice que pueda volar
}

def razonamiento_defecto(hechos):
    if hechos["es_ave"] and not hechos["es_avestruz"]:
        return "El ave vuela"
    return "El ave no vuela"

print("Conclusión:", razonamiento_defecto(hechos))
