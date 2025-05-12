import re

# Define una función para realizar el análisis léxico de un texto dado.
def analizador_lexico(texto):
    # Lista de patrones que representan los diferentes tipos de tokens.
    # Cada patrón tiene un nombre (como 'NUM', 'ID', etc.) y una expresión regular asociada.
    patrones = [
        ('NUM', r'\d+'),  # Números (uno o más dígitos).
        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores (letras o guiones bajos seguidos de letras, números o guiones bajos).
        ('OP', r'[\+\-\*/=]'),  # Operadores (+, -, *, /, =).
        ('PAR', r'[()]'),  # Paréntesis (abiertos o cerrados).
        ('WS', r'\s+')  # Espacios en blanco (uno o más).
    ]

    tokens = []  # Lista para almacenar los tokens encontrados.
    while texto:  # Mientras quede texto por analizar.
        match = None  # Variable para almacenar el resultado de la coincidencia.
        for token_tipo, patron in patrones:  # Itera sobre cada tipo de token y su patrón.
            regex = re.compile(patron)  # Compila la expresión regular.
            match = regex.match(texto)  # Intenta hacer coincidir el patrón con el inicio del texto.
            if match:  # Si hay una coincidencia.
                valor = match.group(0)  # Obtiene el valor coincidente.
                if token_tipo != 'WS':  # Si no es un espacio en blanco.
                    tokens.append((token_tipo, valor))  # Agrega el token a la lista.
                texto = texto[len(valor):]  # Elimina el texto coincidente del inicio.
                break  # Sale del bucle de patrones.
        if not match:  # Si no se encontró ninguna coincidencia.
            raise SyntaxError(f"Token inválido: {texto}")  # Lanza un error indicando el texto no reconocido.
    return tokens  # Devuelve la lista de tokens.

# Prueba del analizador léxico con una entrada de ejemplo.
entrada = "x = 10 + 20"
print(analizador_lexico(entrada))  # Imprime los tokens generados a partir de la entrada.
