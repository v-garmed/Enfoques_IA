def parser(tokens):
    def match(expected):
        nonlocal i
        if i < len(tokens) and tokens[i][1] == expected:
            i += 1
            return True
        return False

    def E():
        T()
        while match('+') or match('-'):
            T()

    def T():
        F()
        while match('*') or match('/'):
            F()

    def F():
        if match('('):
            E()
            if not match(')'):
                raise SyntaxError("Se esperaba ')'")
        elif tokens[i][0] == 'NUM' or tokens[i][0] == 'ID':
            i += 1
        else:
            raise SyntaxError("Token inesperado")

    i = 0
    E()
    if i < len(tokens):
        raise SyntaxError("Tokens sobrantes")

tokens = analizador_lexico("x + 3 * (y - 1)")
parser(tokens)
print("Cadena válida sintácticamente.")
