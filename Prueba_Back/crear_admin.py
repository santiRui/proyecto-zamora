from werkzeug.security import generate_password_hash
from database import get_conexion

def crear_admin():
    connection = get_conexion()
    if connection:
        cursor = connection.cursor()
        
        #Verificar si esta el admin existe
        cursor.execute("SELECT id from usuarios WHERE nombre = 'admin' ")
        if not cursor.fetchone():
            cursor.execute(
                "INSERT INTO usuarios (nombre,password,email) VALUES (%s,%s,%s) returning id",
                ("admin", generate_password_hash("admin"),"admin@gmail.com"),
            )
            usuario_id = cursor.fetchone()[0]
            
            # Crear rol de admin si no esta
            cursor.execute ("SELECT id FROM roles WHERE nombre = 'admin' ")
            rol = cursor.fetchone()
            if not rol:
                cursor.execute("INSERT INTO roles (nombre) VALUES ('admin') RETURNING id")
                rol_id= cursor.fetchone()[0]
            else:
                rol_id = rol[0]
                
            # Asignar admin al usuario
            cursor.execute(
                "INSERT INTO usuario_rol (usuario_id, rol_id) VALUES (%s,%s)",
                (usuario_id,rol_id)
                
            )
            connection.commit()
            
        cursor.close()
        connection.close()

if __name__ == "__main__":
    crear_admin()
            