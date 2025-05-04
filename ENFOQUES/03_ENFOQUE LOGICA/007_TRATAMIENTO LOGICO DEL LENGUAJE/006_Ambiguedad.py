# Representación de dos árboles de derivación para una cadena ambigua

def derivacion_1():
    print("Árbol 1: (a + b) * c")
    print("E")
    print("├── E")
    print("│   ├── a")
    print("│   └── + b")
    print("└── * c")

def derivacion_2():
    print("Árbol 2: a + (b * c)")
    print("E")
    print("├── a")
    print("└── +")
    print("    └── E")
    print("        ├── b")
    print("        └── * c")

print("Simulación de ambigüedad gramatical:")
derivacion_1()
print("\n")
derivacion_2()
