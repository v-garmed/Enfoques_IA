# Función que infiere un patrón común entre varias cadenas
def inferir_patron(cadenas):
    # Calcula la longitud de las cadenas (se asume que todas tienen la misma longitud)
    longitud = len(cadenas[0])
    # Inicializa el patrón como una cadena vacía
    patron = ""
    
    # Itera sobre cada posición de las cadenas
    for i in range(longitud):
        # Obtiene un conjunto con los caracteres en la posición 'i' de todas las cadenas
        chars = set(c[i] for c in cadenas)
        # Si todos los caracteres en la posición 'i' son iguales, los agrega al patrón
        # Si no, agrega un punto (.) como comodín
        patron += chars.pop() if len(chars) == 1 else "."
    
    # Devuelve el patrón inferido
    return patron

# Lista de cadenas de ejemplo
ejemplos = ["abc123", "abc456", "abc789"]

# Llama a la función para inferir el patrón y lo imprime
print("Patrón inferido:", inferir_patron(ejemplos))  # Resultado esperado: abc...