def es_seguro(fila, col, posiciones):
    """ Verifica si es seguro colocar una reina en (fila, col) """
    for f in range(fila):
        c = posiciones[f]
        if c == col or abs(c - col) == abs(f - fila):  
            return False  # Mismo columna o diagonal
    return True

def forward_checking(posiciones, fila, N, dominios):
    """ Reduce los valores en el dominio de cada fila siguiente """
    if fila >= N:
        soluciones.append(posiciones[:])  
        return

    for col in list(dominios[fila]):  
        if es_seguro(fila, col, posiciones):
            posiciones[fila] = col  

            # Guardamos una copia de los dominios antes de modificar
            backup_dominios = [set(d) for d in dominios]

            # Eliminamos valores inconsistentes en las siguientes filas
            for f in range(fila + 1, N):
                if col in dominios[f]:  
                    dominios[f].remove(col)
                diagonal1 = col + (f - fila)
                diagonal2 = col - (f - fila)
                if diagonal1 in dominios[f]:
                    dominios[f].remove(diagonal1)
                if diagonal2 in dominios[f]:
                    dominios[f].remove(diagonal2)

            forward_checking(posiciones, fila + 1, N, dominios)

            # Restauramos los dominios después del retroceso
            dominios[:] = backup_dominios

def imprimir_soluciones(soluciones, N):
    """ Muestra las soluciones encontradas """
    for sol in soluciones:
        for i in range(N):
            fila = ["."] * N
            fila[sol[i]] = "Q"
            print(" ".join(fila))
        print("\n" + "-" * (2 * N))

# Parámetro N (Tamaño del tablero)
N = 8  

# Lista de soluciones
soluciones = []

# Inicialización de dominios (cada fila puede tomar cualquier columna)
dominios = [set(range(N)) for _ in range(N)]
posiciones = [-1] * N  

# Ejecutar Forward Checking
forward_checking(posiciones, 0, N, dominios)

# Mostrar resultados
print(f"Se encontraron {len(soluciones)} soluciones para {N}-reinas:")
imprimir_soluciones(soluciones, N)
