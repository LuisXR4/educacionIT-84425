ausentes = ["ana", "juan", "maria", "jose", "ana", "ana", "ana", "jose", "maria", "maria"]

# RH armar informacion de cada ausente, y la cantidad de ausencias que tuvo en el mes
# {"ana": 4, "juan": 1, "maria": 3, "jose": 2}

"""
dic = {}

for n in ausentes:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
"""

dic = { n : ausentes.count(n)  for n in set(ausentes) } # Es performante

print(dic)        