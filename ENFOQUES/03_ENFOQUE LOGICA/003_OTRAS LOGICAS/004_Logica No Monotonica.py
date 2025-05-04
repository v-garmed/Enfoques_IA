base_conocimiento = {
    "es_pajaro": True,
    "vuela": True
}

nueva_info = {
    "es_pinguino": True
}

def razonamiento_no_monotonico(base, nueva_info):
    if base.get("es_pajaro") and not nueva_info.get("es_pinguino"):
        return "El ave vuela"
    else:
        return "El ave no vuela"

print("Conclusión:", razonamiento_no_monotonico(base_conocimiento, nueva_info))
