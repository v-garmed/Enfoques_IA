base_conocimiento = {
    "llueve": True,
    "llevo_paraguas": False
}

def decidir(base):
    if base["llueve"] and not base["llevo_paraguas"]:
        return "Buscar refugio"
    return "Continuar"

print("Acción del agente:", decidir(base_conocimiento))
