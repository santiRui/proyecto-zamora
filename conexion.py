import psycopg2

def get_connection():
    return psycopg2.connect(
            host='localhost',
            database='Escuela2025',  # Nombre de tu base de datos
            user='postgres',
            password='Contraseña'  # Cambia esto
        )

        
