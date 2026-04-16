# pip install peewee 

from peewee import *

# Conexión a la base SQLite (archivo local)
db = SqliteDatabase('usuarios_peewee.db')

# Definir el modelo
class Usuario(Model):
    nombre = CharField()
    email = CharField()

    class Meta:
        database = db

# Crear la tabla
db.connect()
db.create_tables([Usuario])

# ------------------------
# INSERT
Usuario.create(nombre="Juan Pérez", email="juan@example.com")
Usuario.create(nombre="Ana Gómez", email="ana@example.com")
Usuario.create(nombre="Jose Rodirguez", email="jr@example.com")
Usuario.create(nombre="Ricardo Pereira", email="jp@example.com")
Usuario.create(nombre="Juan Pereira", email="jpe@example.com")

# ------------------------
# SELECT (todos)
print("\n📋 Todos los usuarios:")
for u in Usuario.select():
    print(f"{u.id}: {u.nombre} <{u.email}>")

# ------------------------
# UPDATE
juan = Usuario.get(Usuario.nombre == "Juan Pérez")
juan.email = "juan.perez@nuevo.com"
juan.save()

# ------------------------
# SELECT con filtro
print("\n🔍 Usuarios que contienen 'Juan':")
query = Usuario.select().where(Usuario.nombre.contains("Juan"))
for u in query:
    print(f"{u.id}: {u.nombre} <{u.email}>")

# ------------------------
# DELETE
ana = Usuario.get(Usuario.nombre == "Ana Gómez")
ana.delete_instance()

try:
    mario = Usuario.get(Usuario.nombre == "Mario Arancibia")
    mario.delete_instance()
except Exception as e:
    print(f"El usuario buscado no existe en la BD {e.__class__}")    


# ------------------------
# SELECT final
print("\n📋 Usuarios después de eliminar a Ana:")
for u in Usuario.select():
    print(f"{u.id}: {u.nombre} <{u.email}>")

# Cerrar la conexión
db.close()