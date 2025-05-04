import re

def analizador_lexico(texto):
    patrones = [
        ('NUM', r'\d+'),
        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),
        ('OP', r'[\+\-\*/=]'),
        ('PAR', r'[()]'),
        ('WS', r'\s+')
    ]

    tokens = []
    while texto:
        match = None
        for token_tipo, patron in patrones:
            regex = re.compile(patron)
            match = regex.match(texto)
            if match:
                valor = match.group(0)
                if token_tipo != 'WS':
                    tokens.append((token_tipo, valor))
                texto = texto[len(valor):]
                break
        if not match:
            raise SyntaxError(f"Token inválido: {texto}")
    return tokens

# Prueba
entrada = "x = 10 + 20"
print(analizador_lexico(entrada))
