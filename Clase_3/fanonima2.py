# Lambda: funciona anonima
#   - Se use una sola vez y la notacion es lambda par1, par2 ... parN :  (lo que debe retornar)

ecuacion = lambda x,y,z: x**2 + (x*y*z) + y**2 + z

print(ecuacion(1,2,3))