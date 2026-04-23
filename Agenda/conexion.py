import psycopg2

def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="agenda_db",
            user="postgres",
            password="Winner77",
            port="5432"
        )
        print("✅ Conexión exitosa a PostgreSQL")
        return conexion

    except Exception as e:
        print("❌ Error al conectar:", e)
        return None
    
    