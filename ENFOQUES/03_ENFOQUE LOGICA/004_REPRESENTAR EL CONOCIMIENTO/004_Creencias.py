creencias_agente = {
    "llueve": True,
    "tiene_paraguas": False
}

def razonamiento(creencias):
    if creencias["llueve"] and not creencias["tiene_paraguas"]:
        return "El agente se moja"
    return "El agente está seco"

print("Resultado:", razonamiento(creencias_agente))
