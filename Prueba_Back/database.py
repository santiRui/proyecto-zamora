#instalacion de modulo
import psycopg2

#Conexion:
def get_conexion():
    try:
        connection=psycopg2.connect(user="postgres",
                          password="Aban12062007",
                          host='127.0.0.1',
                          port='5432',
                          database='Escuela'
                          )
        return connection
    except Exception as error:
        print(f"Error al conectar el error es {error}")
        return None
    
