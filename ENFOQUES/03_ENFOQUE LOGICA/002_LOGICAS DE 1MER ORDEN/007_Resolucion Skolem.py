# Transformamos ∃x P(x) a P(skolem_x)
def skolemizar(formula_existencial):
    variable = formula_existencial.split(" ")[1]
    return formula_existencial.replace(variable, "skolem_" + variable)

formula = "∃x Humano(x)"
formula_skolem = skolemizar(formula)
print("Fórmula Skolemizada:", formula_skolem)
