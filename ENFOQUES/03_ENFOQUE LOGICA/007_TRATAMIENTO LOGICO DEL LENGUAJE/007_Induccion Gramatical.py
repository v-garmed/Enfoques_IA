def inferir_patron(cadenas):
    longitud = min(len(c) for c in cadenas)
    patron = ""
    for i in range(longitud):
        chars = set(c[i] for c in cadenas)
        patron += chars.pop() if len(chars) == 1 else "."
    return patron

ejemplos = ["abc123", "abc456", "abc789"]
print("Patrón inferido:", inferir_patron(ejemplos))  # Resultado: abc...
