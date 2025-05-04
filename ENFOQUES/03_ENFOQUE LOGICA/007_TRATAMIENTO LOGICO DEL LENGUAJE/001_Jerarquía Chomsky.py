import re

def detectar_tipo_gramatica(reglas):
    tipo = 3  # Asumimos que es tipo 3 y subimos si encontramos reglas más complejas
    
    for regla in reglas:
        izquierda, derecha = regla.split("->")
        izquierda = izquierda.strip()
        derecha = derecha.strip()
        
        # Verificamos que la izquierda tenga solo un símbolo no terminal (mayúscula)
        if not re.fullmatch(r"[A-Z]", izquierda):
            tipo = max(tipo, 1)  # Podría ser tipo 1 o tipo 0
        
        # Tipo 3: A -> aB o A -> a
        if tipo == 3:
            if not re.fullmatch(r"[a-zA-Z]?", derecha) and not re.fullmatch(r"[a-z][A-Z]", derecha):
                tipo = 2  # No es tipo 3, puede ser CFG
        
        # Tipo 2: A -> γ
        if tipo == 2:
            if not re.fullmatch(r"[a-zA-Z]*", derecha):
                tipo = 1  # Tiene variables en posiciones intermedias, podría ser tipo 1
        
    return tipo

def describir_tipo(tipo):
    if tipo == 3:
        return "Tipo 3: Gramática Regular"
    elif tipo == 2:
        return "Tipo 2: Gramática Independiente del Contexto (CFG)"
    elif tipo == 1:
        return "Tipo 1: Gramática Sensible al Contexto"
    else:
        return "Tipo 0: Gramática Irrestricta"

# ----------------------------
# Ejemplo de uso
# ----------------------------

# Cambia las reglas para probar distintos tipos de gramáticas
reglas = [
    "S -> aA",
    "A -> bB",
    "B -> c"
]

tipo = detectar_tipo_gramatica(reglas)
descripcion = describir_tipo(tipo)

print("Reglas analizadas:")
for regla in reglas:
    print(" -", regla)

print("\nClasificación según la Jerarquía de Chomsky:")
print("→", descripcion)
