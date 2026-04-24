import requests, json

def consultar():
    r = requests.get("http://localhost:7001/student")
    print(f"Status {r.status_code}  Respuesta {r.json()}")


def crear(nombre, curso):
    r = requests.post("http://localhost:7001/student", json={"name": nombre, "courses": curso} )
    print(f"Status {r.status_code}  Respuesta {r.json()}")

def modificar(id, nombre, curso):
    r = requests.put("http://localhost:7001/student/"+str(id), json={"name": nombre, "courses": curso})
    print(f"Status {r.status_code}")

def borrar(id):
    r = requests.delete("http://localhost:7001/student/"+str(id))
    print(f"Status {r.status_code}")


#______________________________________ main

"""
crear("MARIO GOMEZ", 4)
crear("MARIA PEREZ", 9)
crear("JOSE LOPEZ", 10)
crear("ESTEBAN QUITO", 7)
"""

#modificar(3, "JUANA MARTINEZ", 8)

borrar(0)
consultar()