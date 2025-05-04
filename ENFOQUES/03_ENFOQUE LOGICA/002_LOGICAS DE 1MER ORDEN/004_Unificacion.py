def unificar(term1, term2, unificadores={}):
    if term1 == term2:
        return unificadores
    if isinstance(term1, str) and term1.islower():  # variable
        unificadores[term1] = term2
        return unificadores
    if isinstance(term2, str) and term2.islower():
        unificadores[term2] = term1
        return unificadores
    return None

# Prueba
resultado = unificar("x", "Juan")
print("Unificación:", resultado)
