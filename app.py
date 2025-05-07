from conexion import get_connection
from flask import Flask, render_template, request, redirect, url_for
import bcrypt

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("pagina_principal.html")

@app.route("/login_institucional", methods=["GET", "POST"])
def login_institucional():
    if request.method == "POST":
        dni = request.form['dni']
        password_input = request.form['password']

        # Verificar si el DNI y la contraseña coinciden con los valores predefinidos
        if dni == '12345678' and password_input == 'admin':
            return redirect(url_for('pagina_admin'))  # Redirige si DNI y contraseña son correctos

        # Si no, realiza la verificación con la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Administradores WHERE dni = %s", (dni,))
        admin = cursor.fetchone()
        conn.close()

        if admin:
            stored_hashed_password = admin[5]  # Se guarda en la bd
            if bcrypt.checkpw(password_input.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                # Contra
                return redirect(url_for('pagina_admin'))
            else:
                # Contraseña incorrecta
                return "Contraseña incorrecta"
        else:
            # Usuario no encontrado
            return "Usuario no encontrado"
    return render_template("login_institucional.html")

@app.route("/pagina_admin")
def pagina_admin():
    return render_template("pagina_admin.html")

@app.route("/crear_profesor")
def crear_profesor():
    return render_template("crear_profesor.html")

@app.route("/crear_directivo")
def crear_directivo():
    return render_template("crear_directivo.html")

@app.route("/crear_preceptor")
def crear_preceptor():
    return render_template("crear_preceptor.html")

@app.route("/crear_jefe_taller")
def crear_jefe_taller():
    return render_template("crear_jefe_taller.html")

@app.route("/login_familiar")
def login_familiar():
    return render_template("login_familiar.html")

@app.route('/registro_institucion')
def registro_institucion():
    return render_template('registro_institucion.html')

@app.route('/registro_familiar')
def registro_familiar():
    return render_template('registro_familiar.html')


if __name__ == "__main__":
    app.run(port=6990, debug=True)
