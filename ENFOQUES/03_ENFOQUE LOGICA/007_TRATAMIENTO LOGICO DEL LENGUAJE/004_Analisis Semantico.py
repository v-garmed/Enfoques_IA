variables = {"x": "int", "y": "float"}

def verificar_tipo(var1, var2):
    tipo1 = variables.get(var1)
    tipo2 = variables.get(var2)
    if tipo1 == tipo2:
        return True
    else:
        raise TypeError(f"Incompatibilidad de tipos: {tipo1} vs {tipo2}")

verificar_tipo("x", "x")  # Correcto
verificar_tipo("x", "y")  # Lanza error
