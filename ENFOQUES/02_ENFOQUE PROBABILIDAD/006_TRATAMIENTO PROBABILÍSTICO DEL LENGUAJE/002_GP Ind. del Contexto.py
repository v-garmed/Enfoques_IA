# Importamos la librería nltk (Natural Language Toolkit), que es una biblioteca para trabajar con procesamiento de lenguaje natural.
# También importamos clases y funciones específicas de nltk necesarias para trabajar con gramáticas y generación de oraciones.
import nltk
from nltk import Nonterminal  # Representa un símbolo no terminal en una gramática.
from nltk.parse.generate import generate  # Permite generar oraciones a partir de una gramática.
from nltk.grammar import PCFG  # Define una gramática libre de contexto probabilística (Probabilistic Context-Free Grammar).

# Definimos una gramática probabilística (PCFG) usando la función `fromstring`.
# La gramática describe cómo se pueden construir oraciones en un lenguaje, asignando probabilidades a cada regla de producción.
gramatica = PCFG.fromstring("""
  S -> NP VP [1.0]  # Una oración (S) se compone de un sintagma nominal (NP) y un sintagma verbal (VP) con probabilidad 1.0.
  NP -> Det Noun [0.6] | Name [0.4]  # Un sintagma nominal (NP) puede ser un determinante (Det) seguido de un sustantivo (Noun) con probabilidad 0.6, o un nombre propio (Name) con probabilidad 0.4.
  VP -> Verb NP [1.0]  # Un sintagma verbal (VP) se compone de un verbo (Verb) seguido de un sintagma nominal (NP) con probabilidad 1.0.
  Det -> 'el' [0.5] | 'un' [0.5]  # Un determinante (Det) puede ser 'el' o 'un', cada uno con probabilidad 0.5.
  Noun -> 'gato' [0.5] | 'perro' [0.5]  # Un sustantivo (Noun) puede ser 'gato' o 'perro', cada uno con probabilidad 0.5.
  Verb -> 've' [1.0]  # Un verbo (Verb) es 've' con probabilidad 1.0.
  Name -> 'Juan' [0.6] | 'María' [0.4]  # Un nombre propio (Name) puede ser 'Juan' con probabilidad 0.6 o 'María' con probabilidad 0.4.
""")

# Mostramos las frases generadas por la gramática probabilística.
print("Frases generadas por la PCFG:")
# Usamos la función `generate` para generar hasta 10 oraciones posibles a partir de la gramática definida.
for sentence in generate(gramatica, n=10):
    # Cada oración generada es una lista de palabras, que unimos con espacios para mostrarla como una cadena.
    print(' '.join(sentence))
