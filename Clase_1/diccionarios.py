"""
Diccionarios: { clave: valor, clave1 : valor1 }

1. Orden NO (no trabajamos con indices numericos)
2. Mutabilidad SI 
3. Repetición de elementos SI (pero solo del valor)

"""

paises  = { "arg": 47, "bra": 213, "uru": 3, "col": 51, "mex": 132, "chi": 17, "per": 51 }

# Orden NO

print(paises["col"])

# Mutabilidad

paises["bol"] = 14
paises["chi"] = 18

del paises["chi"]


print(paises)