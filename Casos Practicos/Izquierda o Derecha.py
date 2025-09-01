# Diccionario que contiene las posibles direcciones con sus probabilidades y utilidades
acciones = {
    "izquierda": {"probabilidad": 0.7, "utilidad": 8},   # Acción 1: La persona girará a la izquierda
    "derecha": {"probabilidad": 0.4, "utilidad": 6}      # Acción 2: La persona girará a la derecha
}

# Función para seleccionar la mejor predicción basada en el valor esperado
def seleccionar_direccion(acciones):
    mejor = None
    max_utilidad = -1
    for direccion, datos in acciones.items():
        # Valor esperado = probabilidad * utilidad
        valor_esperado = datos["probabilidad"] * datos["utilidad"]
        print(f"{direccion}: Valor esperado = {valor_esperado}")
        # Actualizar si encontramos un valor mejor
        if valor_esperado > max_utilidad:
            max_utilidad = valor_esperado
            mejor = direccion
    return mejor

# Imprime la dirección más probable y útil
print("El robot predice que la persona irá hacia:", seleccionar_direccion(acciones))
