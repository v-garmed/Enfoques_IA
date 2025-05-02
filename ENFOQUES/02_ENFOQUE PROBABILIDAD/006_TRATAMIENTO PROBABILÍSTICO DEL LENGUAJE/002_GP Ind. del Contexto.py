import nltk
from nltk import Nonterminal
from nltk.parse.generate import generate
from nltk.grammar import PCFG

# Definimos una gramática probabilística
gramatica = PCFG.fromstring("""
  S -> NP VP [1.0]
  NP -> Det Noun [0.6] | Name [0.4]
  VP -> Verb NP [1.0]
  Det -> 'el' [0.5] | 'un' [0.5]
  Noun -> 'gato' [0.5] | 'perro' [0.5]
  Verb -> 've' [1.0]
  Name -> 'Juan' [0.6] | 'María' [0.4]
""")

# Mostrar derivaciones posibles
print("Frases generadas por la PCFG:")
for sentence in generate(gramatica, n=10):
    print(' '.join(sentence))
