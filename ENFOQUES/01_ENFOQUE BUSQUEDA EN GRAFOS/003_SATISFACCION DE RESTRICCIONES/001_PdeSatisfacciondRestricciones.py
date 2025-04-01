def es_valido(tablero, fila, col, num):
    """ Verifica si un número puede colocarse en la celda sin violar las reglas del Sudoku """
    # Verificar fila
    if num in tablero[fila]:
        return False

    # Verificar columna
    if num in [tablero[i][col] for i in range(9)]:
        return False

    # Verificar caja 3x3
    inicio_fila, inicio_col = (fila // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    return True

def encontrar_vacio(tablero):
    """ Encuentra la próxima celda vacía en el Sudoku """
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j  # Retorna la posición de la celda vacía
    return None

def resolver_sudoku(tablero):
    """ Resuelve el Sudoku usando Backtracking """
    vacio = encontrar_vacio(tablero)
    
    if not vacio:  # Si no hay celdas vacías, el Sudoku está resuelto
        return True
    
    fila, col = vacio

    for num in range(1, 10):  # Intentar números del 1 al 9
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num  # Asignar número si es válido
            
            if resolver_sudoku(tablero):  # Llamada recursiva
                return True
            
            tablero[fila][col] = 0  # Deshacer asignación si no conduce a una solución

    return False  # No hay solución válida

def imprimir_tablero(tablero):
    """ Imprime el Sudoku de forma legible """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Línea separadora cada 3 filas
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Línea separadora cada 3 columnas
            print(tablero[i][j] if tablero[i][j] != 0 else ".", end=" ")
        print()

# Sudoku de ejemplo con espacios vacíos representados por 0
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku inicial:")
imprimir_tablero(sudoku)

if resolver_sudoku(sudoku):
    print("\nSudoku resuelto:")
    imprimir_tablero(sudoku)
else:
    print("\nNo tiene solución.")
