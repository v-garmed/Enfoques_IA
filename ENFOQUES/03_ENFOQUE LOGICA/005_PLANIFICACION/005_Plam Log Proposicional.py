# Uso de un solucionador SAT para un problema simple
from pysat.solvers import Glucose3

# Variables: A, B
# Restricciones: A OR B, NOT A OR NOT B (solo una puede ser verdadera)
solver = Glucose3()
solver.add_clause([1, 2])    # A OR B
solver.add_clause([-1, -2])  # NOT A OR NOT B

if solver.solve():
    modelo = solver.get_model()
    print("Solución encontrada:", modelo)
else:
    print("No hay solución.")
