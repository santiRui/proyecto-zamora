#instalacion de modulo
import psycopg2

#Conexion:
conexion=psycopg2.connect(user="postgres",
                          password="--",
                          host='--',
                          port='---',
                          database='--'
                          )


# Utilizo para manejera el postgres
cursor= conexion.cursor()

#Crear sentencia SQL




"""# Leer la base
sql= 'SELECT  * FROM persona'


# cursor.execute(sql)

# #Muestra
# registro= cursor.fetchall()

# print(registro)
"""



"""# Insertar datos a la BD
sql= "INSERT INTO persona (nombre,apellido,edad) VALUES (%s,%s,%s)"
Datos= "Luis","Mendez","34"

try:
    cursor.execute(sql,Datos) # Ejecuta la consulta
    conexion.commit() #Guarda los cambios
    print("Bien.. se subio ")
except Exception as e:
    print("error en la base no se pudo subir ")
    conexion.rollback() # Si llega a haber algun error se evita/deshacer los cambie 
    

"""

"""#Actualizar datos de la BD
sql= "UPDATE persona SET edad = %s WHERE id_per = %s"
Datos= (27,1) # Cambia la edad


try:
    cursor.execute(sql,Datos) # Ejecuta la consulta
    conexion.commit() #Guarda los cambios
    print("Bien.. se subio pero actualizamos su pedido ")
except Exception as e:
    print(f"error en la base no se pudo actualizar:  {e}")
    conexion.rollback() # Si llega a haber algun error se evita/deshacer los cambie 
    
"""


"""sql= "DELETE FROM persona WHERE id_per = %s"
Datos= (4, ) 


try:
    cursor.execute(sql,Datos) # Ejecuta la consulta
    conexion.commit() #Guarda los cambios
    print("Bien.. se elimino el dato que querias ")
except Exception as e:
    print(f"error en el dato no se pudo borrar:  {e}")
    conexion.rollback() # Si llega a haber algun error se evita/deshacer los cambio """


#Cerrar conexion
cursor.close()
conexion.close()