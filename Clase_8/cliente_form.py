import requests

datos = {   "name" : "PEDRO DE MENDOZA",
            "email" : "pm@gmail.com",
            "message" : "Estoy interesado en conocer los productos que ofrecen, y precios" }


for i in range(5):
    r = requests.post("http://localhost:8880/form", data=datos)
    if "Mensaje enviado" in r.content.decode("utf-8"):
        print("Barbaro simule un formulario desde python")
    else:    
        print("Finalizo con error", r.content.decode('utf-8'))