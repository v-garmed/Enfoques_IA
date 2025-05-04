from itertools import product

def equivalentes(p, q):
    return p == q

# Evaluamos si P → Q es equivalente a ¬P ∨ Q
def implies(p, q): return (not p) or q
def equiv_form(p, q): return implies(p, q) == (not p or q)

print("P\tQ\tEquivalentes")
for p, q in product([True, False], repeat=2):
    print(f"{p}\t{q}\t{equiv_form(p, q)}")
