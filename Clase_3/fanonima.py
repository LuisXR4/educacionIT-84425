nombres = ["jUAN", "     ricardo", "ANA", "maria", "  mAriNa  ", "Juana", "pedro"]

"""
def limpieza(x):
    return x.strip().title()
"""

print(list(map(lambda x: x.strip().title() , nombres)))