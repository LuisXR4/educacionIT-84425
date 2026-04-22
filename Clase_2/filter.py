anios = [1975,2008,2009,2000,2007,1996,2026]

def bisiestos(anio):
    if (anio%400==0) or (anio%4==0 and anio%100!=0):
        return True
    return False

res = filter(bisiestos, anios)
print(list(res))