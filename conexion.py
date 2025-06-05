import psycopg2
from werkzeug.security import generate_password_hash

def get_connection():
    return psycopg2.connect(
            host='localhost',
            database='Samora',  # Nombre de tu base de datos
            user='postgres',
            password='Aban12062007'  # Cambia esto
        )

# #  CREACION DEL ADMIN 
# def crear_admin_por_defecto():
#     conn = get_connection()
#     cursor = conn.cursor()
#     try:
#         # Verificar si ya existe un admin con ese gmail o dni
#         cursor.execute("""
#             SELECT * FROM institucion 
#             WHERE gmail = %s OR dni_institu = %s
#         """, ("tenican.3139@gmail.com", 99999999))
#         admin_existente = cursor.fetchone()

#         if not admin_existente:
#             # Verificar si ya existe el rol 'administrador'
#             cursor.execute("SELECT id_roles FROM roles WHERE nombre_roles = 'administrador'")
#             rol = cursor.fetchone()
#             if not rol:
#                 # Insertar rol administrador con id 1 (si id_roles es serial, deberías ajustarlo)
#                 cursor.execute("INSERT INTO roles (id_roles, nombre_roles) VALUES (%s, %s)", (1, 'administrador'))
#                 id_rol = 1
#             else:
#                 id_rol = rol[0]

#             hashed_password = generate_password_hash('admin')

#             cursor.execute("""
#                 INSERT INTO institucion (
#                     dni_institu, nombre, apellido, gmail, telefono, password, id_roles_institu, roles
#                 ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#             """, (
#                 99999999, 'admin', 'admin', 'tenican.3139@gmail.com', '3874320294',
#                 hashed_password, id_rol, 'administrador'
#             ))

#             conn.commit()
#             print("Administrador creado correctamente.")
#         else:
#             print("El administrador predeterminado ya existe, no se creó otro.")
#     except Exception as e:
#         print("Error al crear administrador:", e)
#     finally:
#         cursor.close()
#         conn.close()
# # FIN DE CREAR EL ADMIN    
