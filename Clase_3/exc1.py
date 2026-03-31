"""
print(sorted([1,2,"A", 3.14])) # TypeError
print(2000/0) # ZeroDivisionError

lista = [1,2,3,4]
print(lista[10])  # IndexError

"""

try:
    int([1,2,3])
except ValueError:
    print("Error de Valor")
except TypeError:
    print("Error de Tipo")

print("aca el programa continua")
