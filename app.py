from flask import Flask, render_template,request,redirect, flash,session,url_for
from conexion import get_connection
from werkzeug.security import generate_password_hash 
import psycopg2

app = Flask(__name__)
app.secret_key = '1234'

@app.route('/')
def pagina_principal():
    return render_template('pagina_principal.html')

@app.route('/login_institucional')
def login_intitucional():
    return render_template('login_institucional.html')
    



@app.route('/login_familiar', methods=['GET', 'POST'])
def login_familiar():
    if request.method == 'POST':
        dni = request.form['dni']
        password = request.form['password']

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT dni_familia, password FROM familia WHERE dni_familia = %s", (dni,))
            resultado = cur.fetchone()
            cur.close()
            conn.close()

            if resultado:
                dni_bd = resultado[0]
                pass_bd = resultado[1]
                if password == pass_bd:
                    session['dni_familia'] = dni_bd
                    return redirect(url_for('pagina_escolar'))
                else:
                    # Contraseña incorrecta
                    print("Contraseña incorrecta")
                    return render_template('login_familiar.html')
                    
            else:
                # DNI no registrado
                print("El dni no existe")
                return render_template('login_familiar.html')

        except psycopg2.Error as e:
            print("Error en login:", e)
            return render_template('login_familiar.html')

    return render_template('login_familiar.html')

@app.route('/contrasena_olvidada', methods=['GET', 'POST'])
def contrasena_olvidada():
    if request.method == 'POST':
        # Aca va la logica 
        # para mandar el gmail
        email = request.form.get('email')
        # Por ahora solo redirigimos 
        flash('Si su correo está registrado, recibirá un email para recuperar la contraseña.', 'info')
        return redirect(url_for('login_familiar'))
    
    return render_template('contraseña_olvidada.html')


@app.route('/pagina_escolar')
def pagina_escolar():
    if 'dni_familia' in session:
        # 
        return render_template('pagina_escolar.html')  # 
    else:
        return redirect(url_for('login_familiar'))
    
@app.route('/registro_familiar', methods=['GET', 'POST'])
def registro_familiar():
    if request.method == 'POST':
        dni = request.form['dni']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        password = request.form['password']

        try:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO familia (dni_familia, nombre, apellido, gmail, telefono, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (dni, nombre, apellido, email, telefono, password))
            conn.commit()
            cur.close()
            conn.close()
            flash('Familiar registrado con éxito', 'success')
            return redirect('/login_familiar')
        except Exception as e:
            print("Error al registrar:", e)
            flash('Error al registrar familiar. Verifica los datos.', 'danger')
            return redirect('/registro_familiar')

    return render_template('registro_familiar.html')


if __name__ == '__main__':
    app.run(port=2232,debug=True)
