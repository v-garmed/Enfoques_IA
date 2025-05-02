# Simulación de gramática lexicalizada
import random

# Gramática lexicalizada simplificada
grammar = {
    'S': [('NP_juan VP_ver', 0.6), ('NP_maria VP_dar', 0.4)],
    'NP_juan': [('Juan', 1.0)],
    'NP_maria': [('María', 1.0)],
    'VP_ver': [('ver NP_libro', 1.0)],
    'VP_dar': [('dar NP_regalo', 1.0)],
    'NP_libro': [('el libro', 1.0)],
    'NP_regalo': [('el regalo', 1.0)]
}

# Función para generar frases
def generate(symbol):
    if symbol not in grammar:
        return [symbol]
    productions = grammar[symbol]
    symbols, prob = zip(*productions)
    chosen = random.choices(symbols, weights=prob)[0]
    return sum([generate(sym) for sym in chosen.split()], [])

# Generar una frase
sentence = generate('S')
print("Frase generada:", ' '.join(sentence))
