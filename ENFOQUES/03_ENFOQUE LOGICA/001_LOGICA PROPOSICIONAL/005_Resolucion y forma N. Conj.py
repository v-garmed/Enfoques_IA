# Representamos cláusulas como listas de literales
KB = [['¬P', 'Q'], ['P'], ['¬Q', 'R'], ['¬R']]

def resolucion(cl1, cl2):
    for l1 in cl1:
        for l2 in cl2:
            if l1 == '¬' + l2 or l2 == '¬' + l1:
                nueva = list(set(cl1 + cl2))
                nueva.remove(l1)
                nueva.remove(l2)
                return nueva
    return None

# Ejemplo: resolver la primera y segunda cláusula
cl_nueva = resolucion(KB[0], KB[1])
print("Nueva cláusula generada por resolución:", cl_nueva)
