def sumar(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int,float)):
        raise TypeError("Alguno de los argumentos o ambos no son numericos")
    return a + b

x = 1
y = "hola"

try:
    r = sumar(x, y)
except Exception as e:
    print(f"Ocurrio un error {e.__class__} ==> {e}")