from conexion import get_connection
import bcrypt
import json

def create_super_user():
    # Defino los datos
    dni = "12345678"
    nombre = "admin"
    apellido = "tec3"
    telefono = "1234567890"
    gmail = "tecnica@gmail.com"
    password = "admin"  # Contraseña en texto claro
    llave_desemcriptacion = "llave1"
    
    # Permisos completos para todos los roles
    permisos = {
        "crear_directivo": True,
        "crear_preceptor": True,
        "crear_alumno": True,
        "crear_jefe_taller": True,  # Permiso para crear jefes de taller
        "crear_profesor": True,     # Permiso para crear profesores
        
        
    }

    # Hashear la contraseña
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Establecer la conexión a la base de datos
    conn = get_connection()
    cursor = conn.cursor()

    # Crear la consulta SQL para insertar el super usuario
    query = """
    INSERT INTO Administradores (dni, nombre, apellido, telefono, gmail, password, llave_desemcriptacion, permisos, activo)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (dni, nombre, apellido, telefono, gmail, hashed_password, llave_desemcriptacion, json.dumps(permisos), True))

    # Confirmar la transacción
    conn.commit()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    print("Super usuario creado correctamente con permisos completos.")

# Llamar a la función para crear el super usuario
if __name__ == "__main__":
    create_super_user()
