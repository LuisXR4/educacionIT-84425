try:
    print("Hola")
    a = 5 + 10
    b = a / 2
    lista = [1,2,3]
    print(lista[0])
except Exception as e:
    print(f"Se presento un error {e.__class__}")    
else:
    print("Todo Salio Bien!!")    