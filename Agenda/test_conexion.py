from conexion import obtener_conexion

conn = obtener_conexion()

if conn:
    print("TODO OK 🚀")
    conn.close()
else:
    print("Fallo la conexión ❌")

    