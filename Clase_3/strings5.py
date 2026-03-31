paises = "ARGENTINA CHILE MEXICO URUGUAY PERU BOLIVIA COLOMBIA ECUADOR VENEZUELA PARAGUAY BRASIL"
csv = "1,PEDRO,44,CORRIENTES 222,1234"
lista = csv.split(",")

if "CHILE" in paises:
    print("Chile esta en el string")

print(lista)