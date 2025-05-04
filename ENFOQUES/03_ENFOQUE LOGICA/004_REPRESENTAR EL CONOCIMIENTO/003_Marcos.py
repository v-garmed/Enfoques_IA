# Marco para una acción
marco_comer = {
    "acción": "comer",
    "agente": "humano",
    "objeto": "comida",
    "lugar": "mesa",
    "tiempo": "mediodía"
}

def describir_marco(marco):
    return f"{marco['agente']} va a {marco['acción']} {marco['objeto']} en la {marco['lugar']} a las {marco['tiempo']}."

print(describir_marco(marco_comer))
