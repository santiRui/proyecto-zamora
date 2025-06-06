from flask import Flask, render_template,request,redirect, flash,session,url_for
from conexion import get_connection
from werkzeug.security import generate_password_hash, check_password_hash 
import psycopg2
import smtplib
from email.message import EmailMessage
import uuid
from datetime import datetime, timedelta

#Codigo echo por el equipo de backend Delagado: Aban Santiago
#Correcion de tipos de roles echo el 5/6 a hrs 13:46 Version del codigo 1.2v 


app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/login_familiar', methods=['GET', 'POST'])
def login_familiar():
    if request.method == 'POST':
        dni = request.form['dni']
        password = request.form['password']
        print(f"Intento de login con DNI: {dni}")

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT password, nombre FROM familia WHERE dni_familia = %s", (dni,))
            resultado = cur.fetchone()
            cur.close()
            conn.close()

            print(f"Resultado consulta usuario: {resultado}")

            if resultado:
                hash_guardado, nombre = resultado
                print(f"Hash guardado: {hash_guardado}, Nombre: {nombre}")

                if check_password_hash(hash_guardado, password):
                    session['dni_familia'] = dni
                    session['nombre_familia'] = nombre
                    session['rol'] = 'familiar'
                    return redirect(url_for('pagina_escolar'))
                else:
                    print("Contraseña incorrecta")
                    flash("Contraseña incorrecta.", "error")
            else:
                print("No se encontró familiar con ese DNI")
                flash("No se encontró un familiar con ese DNI.", "error")
        except Exception as e:
            print(f"Error en inicio de sesión: {e}")
            flash("Error en el inicio de sesión: " + str(e), "error")

    return render_template("login_familiar.html")



@app.route('/registro_familiar', methods=['GET', 'POST'])
def registro_familiar():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        gmail = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        verify_password = request.form['verify_password']

        print(f"Datos recibidos: dni={dni}, nombre={nombre}, apellido={apellido}, gmail={gmail}, telefono={telefono}")

        if password != verify_password:
            print("Error: las contraseñas no coinciden")
            flash("Las contraseñas no coinciden", 'error')
            return redirect(url_for('registro_familiar'))

        conn = get_connection()
        cursor = conn.cursor()

        try:
            hashed_password = generate_password_hash(password)
            print(f"Contraseña hasheada: {hashed_password}")

            cursor.execute("SELECT dni_institu FROM institucion LIMIT 1")
            institucion = cursor.fetchone()
            print(f"Institución encontrada: {institucion}")

            if not institucion:
                print("Error: no hay institución registrada")
                flash("Debe existir al menos una institución registrada para vincular familiares.", 'error')
                return redirect(url_for('registro_familiar'))

            dni_institu = institucion[0]

            cursor.execute("""
                INSERT INTO familia (
                    dni_familia, nombre, apellido, gmail, telefono, password, dni_institu_familia
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                dni, nombre, apellido, gmail, telefono,
                hashed_password, dni_institu
            ))
            conn.commit()
            print("Registro insertado correctamente en la tabla familia")
            flash("Familiar registrado exitosamente", 'success')
            return redirect(url_for('login_familiar'))  

        except psycopg2.IntegrityError:
            conn.rollback()
            print("Error: DNI o correo duplicado")
            flash("Ya existe un familiar con ese DNI o correo", 'error')
        except Exception as e:
            conn.rollback()
            print(f"Error en registro_familiar: {e}")
            flash(f"Error: {str(e)}", 'error')
        finally:
            cursor.close()
            conn.close()

    return render_template('registro_familiar.html')



@app.route('/registro_institucion', methods=['GET', 'POST'])
def registro_institucion():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        gmail = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']
        verify_password = request.form['verify_password']
        rol = request.form['rol']

        if password != verify_password:
            flash("Las contraseñas no coinciden")
            return redirect(url_for('registro_institucion'))

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT id_roles FROM roles WHERE nombre_roles = %s", (rol,))
            resultado = cursor.fetchone()
            if resultado:
                id_rol = resultado[0]
            else:
                cursor.execute("INSERT INTO roles (nombre_roles) VALUES (%s) RETURNING id_roles", (rol,))
                id_rol = cursor.fetchone()[0]

            hashed_password = generate_password_hash(password)

            cursor.execute("""
                INSERT INTO institucion (
                    dni_institu, nombre, apellido, gmail, telefono, password, id_roles_institu, roles
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                dni, nombre, apellido, gmail, telefono,
                hashed_password, id_rol, rol
            ))

            conn.commit()
            flash("Registro exitoso")
            return redirect(url_for('registro_institucion'))

        except psycopg2.IntegrityError:
            conn.rollback()
            flash("Ya existe un usuario con ese DNI o correo")
        except Exception as e:
            conn.rollback()
            flash(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    # Cargar usuarios y roles para GET y después de POST
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT dni_institu, nombre, roles FROM institucion ORDER BY dni_institu")
    usuarios = cursor.fetchall()

    cursor.execute("SELECT id_roles, nombre_roles FROM roles ORDER BY nombre_roles")
    roles = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('registro_institucion.html', usuarios=usuarios, roles=roles)

@app.route('/eliminar_usuario/<dni>', methods=['POST'])
def eliminar_usuario(dni):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM institucion WHERE dni_institu = %s", (dni,))
        conn.commit()
        print(f"[INFO] Usuario con DNI {dni} eliminado correctamente.")
        flash("Usuario eliminado correctamente")
    except Exception as e:
        print(f"[ERROR] Error al eliminar usuario: {e}")
        flash(f"Error al eliminar el usuario: {str(e)}")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('registro_institucion'))

@app.route('/editar_usuario/<dni>', methods=['GET'])
def editar_usuario(dni):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Obtener los datos del usuario a editar
        cursor.execute("""
            SELECT dni_institu, nombre, apellido, gmail, telefono, roles 
            FROM institucion WHERE dni_institu = %s
        """, (dni,))
        usuario = cursor.fetchone()

        # Obtener lista de usuarios para la tabla
        cursor.execute("""
            SELECT i.dni_institu, i.nombre, r.nombre_roles 
            FROM institucion i 
            JOIN roles r ON i.id_roles_institu = r.id_roles
        """)
        usuarios = cursor.fetchall()

        return render_template(
            'registro_institucion.html', 
            usuario_editar=usuario,
            usuarios=usuarios
        )
    except Exception as e:
        flash(f"Error al cargar datos del usuario: {str(e)}")
        return redirect(url_for('registro_institucion'))
    finally:
        cursor.close()
        conn.close()


@app.route('/actualizar_usuario/<dni>', methods=['POST'])
def actualizar_usuario(dni):
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    gmail = request.form['email']
    telefono = request.form['telefono']
    rol = request.form['rol']

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Buscar o crear el rol
        cursor.execute("SELECT id_roles FROM roles WHERE nombre_roles = %s", (rol,))
        resultado = cursor.fetchone()
        if resultado:
            id_rol = resultado[0]
        else:
            cursor.execute("INSERT INTO roles (nombre_roles) VALUES (%s) RETURNING id_roles", (rol,))
            id_rol = cursor.fetchone()[0]

        # Actualizar los datos
        cursor.execute("""
            UPDATE institucion 
            SET nombre=%s, apellido=%s, gmail=%s, telefono=%s, id_roles_institu=%s, roles=%s
            WHERE dni_institu=%s
        """, (nombre, apellido, gmail, telefono, id_rol, rol, dni))

        conn.commit()
        flash("Usuario actualizado correctamente.")
    except Exception as e:
        conn.rollback()
        flash(f"Error al actualizar el usuario: {str(e)}")
    finally:
        cursor.close()
        conn.close()
    return redirect(url_for('registro_institucion'))


@app.route('/login_institucional', methods=['GET', 'POST'])
def login_institucional():
    if request.method == 'POST':
        dni = request.form['dni']
        password = request.form['password']

        print(f"[DEBUG] Intentando login con DNI: {dni}")

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT dni_institu, password, roles FROM institucion WHERE dni_institu = %s", (dni,))
            user = cursor.fetchone()

            if user:
                print(f"[DEBUG] Usuario encontrado. Rol: {user[2]}, Hashed PW: {user[1]}")
            else:
                print("[DEBUG] Usuario no encontrado en la base de datos.")
                flash('El usuario no existe.', 'error')

            if user and check_password_hash(user[1], password):
                rol_lower = user[2].lower()
                print(f"[DEBUG] Contraseña válida. Rol: {rol_lower}")

                session['dni_institu'] = user[0]
                session['rol'] = rol_lower

                flash('Inicio de sesión exitoso.', 'success')

                if rol_lower == 'administrador':
                    print("[DEBUG] Redirigiendo a pagina_admin")
                    return redirect(url_for('pagina_admin'))

                elif rol_lower == 'familiar':
                    print("[DEBUG] Rol familiar no permitido en login_institucional")
                    flash('Acceso denegado: Use el login familiar para este rol.', 'error')
                    return redirect(url_for('login_institucional'))

                else:
                    print("[DEBUG] Redirigiendo a pagina_escolar")
                    return redirect(url_for('pagina_escolar'))

            else:
                print("[DEBUG] DNI o contraseña incorrectos")
                flash('DNI o contraseña incorrectos', 'error')

        except Exception as e:
            print(f"[ERROR] Excepción en login: {e}")
            flash(f'Error al iniciar sesión: {str(e)}', 'error')

        finally:
            cursor.close()
            conn.close()

    return render_template('login_institucional.html')


@app.route('/pagina_admin')
def pagina_admin():
    if 'rol' in session and session['rol'] == 'administrador':
        return render_template('pagina_admin.html')
    else:
        return redirect(url_for('login_institucional'))

@app.route('/pagina_escolar')
def pagina_escolar():
    if 'rol' not in session:
        return redirect(url_for('login_institucional'))

    rol = session['rol']

    if rol == 'administrador':
        return redirect(url_for('pagina_admin'))

    if rol == 'familiar':
        return render_template('pagina_escolar.html')

    # Cualquier otro rol creado dinámicamente entra acá
    return render_template('pagina_escolar.html')
    

@app.route('/crear_rol', methods=['GET', 'POST'])
def crear_rol():
    conn = get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre_rol = request.form['nombre_rol'].strip()

        if not nombre_rol:
            flash("El nombre del rol no puede estar vacío")
            return redirect(url_for('crear_rol'))

        try:
            # Verificar si el rol ya existe
            cursor.execute("SELECT id_roles FROM roles WHERE nombre_roles = %s", (nombre_rol,))
            if cursor.fetchone():
                flash("El rol ya existe")
            else:
                cursor.execute("INSERT INTO roles (nombre_roles) VALUES (%s)", (nombre_rol,))
                conn.commit()
                flash("Rol creado correctamente")
        except Exception as e:
            conn.rollback()
            flash(f"Error al crear el rol: {e}")

    # Listar roles para mostrar
    cursor.execute("SELECT id_roles, nombre_roles FROM roles ORDER BY nombre_roles")
    roles = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('crear_rol.html', roles=roles)

@app.route('/eliminar_rol/<int:id_rol>', methods=['POST'])
def eliminar_rol(id_rol):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Opcional: verificar que el rol no esté asignado a usuarios
        cursor.execute("SELECT COUNT(*) FROM institucion WHERE id_roles_institu = %s", (id_rol,))
        count = cursor.fetchone()[0]
        if count > 0:
            flash("No se puede eliminar un rol asignado a usuarios")
        else:
            cursor.execute("DELETE FROM roles WHERE id_roles = %s", (id_rol,))
            conn.commit()
            flash("Rol eliminado correctamente")
    except Exception as e:
        conn.rollback()
        flash(f"Error al eliminar el rol: {e}")
    cursor.close()
    conn.close()
    return redirect(url_for('crear_rol'))

def enviar_email(destinatario, asunto, contenido_html):
    remitente = "tenican.3139@gmail.com"
    contraseña_app = "djda jcmy fgxz qsrn"  # Código de aplicación Gmail

    msg = EmailMessage()
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario
    msg.set_content("Correo institucional ")  # Texto alternativo
    msg.add_alternative(contenido_html, subtype='html')

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, contraseña_app)
            smtp.send_message(msg)
        print(f"Correo enviado a {destinatario}")
    except Exception as e:
        print(f"Error enviando correo: {e}")
        
@app.route('/contrasena_olvidada', methods=['GET', 'POST'])
def contrasena_olvidada():
    if request.method == 'POST':
        email_o_dni = request.form.get('email', '').strip()

        if not email_o_dni:
            flash("Debe ingresar su correo o DNI.", "error")
            return render_template('contrasena_olvidada.html')

        conn = get_connection()
        cursor = conn.cursor()

        # Buscar en familia
        cursor.execute("""
            SELECT dni_familia, gmail FROM familia 
            WHERE gmail = %s OR dni_familia::text = %s
        """, (email_o_dni, email_o_dni))
        resultado_familia = cursor.fetchone()

        # Buscar en institucion si no está en familia
        cursor.execute("""
            SELECT dni_institu, gmail FROM institucion 
            WHERE gmail = %s OR dni_institu::text = %s
        """, (email_o_dni, email_o_dni))
        resultado_institucion = cursor.fetchone()

        if resultado_familia:
            dni_usuario, correo = resultado_familia
            tipo_usuario = 'familia'
        elif resultado_institucion:
            dni_usuario, correo = resultado_institucion
            tipo_usuario = 'institucion'
        else:
            flash("No se encontró un usuario con ese correo o DNI.", "error")
            cursor.close()
            conn.close()
            return render_template('contrasena_olvidada.html')

        # Generar token
        token = str(uuid.uuid4())
        expiracion = datetime.now() + timedelta(hours=1)

        # Guardar token en la base
        cursor.execute("""
            INSERT INTO recuperacion_password (token, dni_usuario, tipo_usuario, fecha_expiracion)
            VALUES (%s, %s, %s, %s)
        """, (token, dni_usuario, tipo_usuario, expiracion))
        conn.commit()
        cursor.close()
        conn.close()

        # Contenido del correo SIN el enlace
        asunto = "Solicitud de cambio de contraseña"
        cuerpo_html = f"""
        <p>Hola,</p>
        <p>Se ha solicitado un cambio de contraseña para tu cuenta.</p>
        <p>Si fuiste tú, por favor sigue los pasos en la página del sistema.</p>
        <p>Este proceso expirará en 1 hora.</p>
        <p>Si no realizaste esta solicitud, puedes ignorar este mensaje.</p>
        """

        # Enviar correo
        enviar_email(correo, asunto, cuerpo_html)

        # Redirigir directamente al formulario de creación de nueva contraseña
        return redirect(url_for('crear_nueva_contrasena', token=token))

    return render_template('contrasena_olvidada.html')


@app.route('/crear_nueva_contrasena/<token>', methods=['GET', 'POST'])
def crear_nueva_contrasena(token):
    conn = get_connection()
    cursor = conn.cursor()

    print(f"[DEBUG] Validando token: {token}")
    cursor.execute("SELECT dni_usuario, tipo_usuario, fecha_expiracion FROM recuperacion_password WHERE token = %s", (token,))
    registro = cursor.fetchone()

    if not registro:
        print("[DEBUG] Token inválido o no encontrado.")
        cursor.close()
        conn.close()
        flash("Token inválido.", "error")
        return redirect(url_for('contrasena_olvidada'))

    dni_usuario, tipo_usuario, fecha_expiracion = registro
    print(f"[DEBUG] Token válido para dni_usuario={dni_usuario}, tipo_usuario={tipo_usuario}, expira={fecha_expiracion}")

    if fecha_expiracion < datetime.now():
        print("[DEBUG] Token expirado.")
        cursor.execute("DELETE FROM recuperacion_password WHERE token = %s", (token,))
        conn.commit()
        cursor.close()
        conn.close()
        flash("El enlace ha expirado.", "error")
        return redirect(url_for('contrasena_olvidada'))

    if request.method == 'POST':
        print("[DEBUG] Recibido POST para cambiar contraseña")
        print(f"[DEBUG] Form data: {request.form}")

        nueva_password = request.form.get('new_password')
        confirmar_password = request.form.get('confirm_password')

        if not nueva_password or not confirmar_password:
            print("[DEBUG] Algún campo de contraseña está vacío")
            flash("Debe completar ambos campos de contraseña.", "error")
            return render_template('crear_nueva_contrasena.html', token=token)

        if nueva_password != confirmar_password:
            print("[DEBUG] Las contraseñas no coinciden")
            flash("Las contraseñas no coinciden.", "error")
            return render_template('crear_nueva_contrasena.html', token=token)

        hashed = generate_password_hash(nueva_password)
        print(f"[DEBUG] Contraseña hasheada: {hashed}")

        if tipo_usuario == 'familia':
            print(f"[DEBUG] Actualizando contraseña en familia para dni {dni_usuario}")
            cursor.execute("UPDATE familia SET password = %s WHERE dni_familia = %s", (hashed, dni_usuario))
        else:
            print(f"[DEBUG] Actualizando contraseña en institucion para dni {dni_usuario}")
            cursor.execute("UPDATE institucion SET password = %s WHERE dni_institu = %s", (hashed, dni_usuario))

        print("[DEBUG] Borrando token de recuperación")
        cursor.execute("DELETE FROM recuperacion_password WHERE token = %s", (token,))
        conn.commit()

        cursor.close()
        conn.close()

        flash("Contraseña actualizada correctamente.", "success")
        return redirect(url_for('pagina_principal'))

    cursor.close()
    conn.close()
    print("[DEBUG] GET: mostrando formulario de cambio de contraseña")
    return render_template('crear_nueva_contrasena.html', token=token)

if __name__ == '__main__':
    app.run(port=2232,debug=True)
