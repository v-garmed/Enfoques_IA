from itertools import product

# Definimos los operadores lógicos
def NOT(p): return not p
def AND(p, q): return p and q
def OR(p, q): return p or q
def IMPLIES(p, q): return (not p) or q

# Tabla de verdad para P → Q
print("P\tQ\tP → Q")
for p, q in product([True, False], repeat=2):
    print(f"{p}\t{q}\t{IMPLIES(p, q)}")
