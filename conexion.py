import psycopg2

def get_connection():
    return psycopg2.connect(
            host='localhost',
            database='Samora',  # Nombre de tu base de datos
            user='postgres',
            password='Aban12062007'  # Cambia esto
        )

        
