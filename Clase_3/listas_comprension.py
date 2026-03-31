# Listas por compresion
# 

# l7 = [7, 14, 21, 28, 35 .... 700 ] 


# l7 = [ expresion         ciclo    condicionales       ]

l7 = [ n*7    for n in range(1,101) ]

# De la lista previa filtrar aquellos que son tambien multiplos de 5

l7 = [ n*7    for n in range(1,101)  if (n*7)%5==0 ]
print(l7)