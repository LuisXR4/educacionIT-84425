try:
    a = 2000 / 0
except (ValueError, TypeError, ZeroDivisionError):
    print("Error de Valor o de Tipo o Division por cero")

print("aca el programa continua")
