from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from database import get_conexion

app = Flask(__name__)
app.secret_key = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        connection = get_conexion()
        cursor = connection.cursor()
        cursor.execute("SELECT id, password FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and check_password_hash(user[1], password):
            session["usuario_id"] = user[0]

            # Obtener el rol del usuario
            cursor.execute("""
                SELECT roles.nombre FROM roles 
                INNER JOIN usuario_rol ON roles.id = usuario_rol.rol_id 
                WHERE usuario_rol.usuario_id = %s
            """, (user[0],))
            rol = cursor.fetchone()
            session["rol"] = rol[0] if rol else "usuario"

            cursor.close()
            connection.close()

            return redirect(url_for('home'))
        
        cursor.close()
        connection.close()
    
    return render_template("login.html")  # Asegura que siempre retorna algo

@app.route("/home")
def home():
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    rol = session.get("rol", "usuario")
    if rol == "admin":
        return render_template("admin.html")
    elif rol == "profesor":
        return "Hola profe"
    elif rol == "Preceptor":
        return "Hola prece"
    else:
        return "Hola nuevo usuario"

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/admin/crear_usuario", methods=["POST"])
def crear_usuario():
    if session.get("rol") != "admin":
        return redirect(url_for("login"))

    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]
    rol = request.form["rol"]

    connection = get_conexion()
    cursor = connection.cursor()

    # Hash de la contraseña
    hashed_password = generate_password_hash(password)

    # Insertar usuario
    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s) RETURNING id",
        (nombre, email, hashed_password),
    )
    usuario_id = cursor.fetchone()[0]

    # Obtener ID del rol
    cursor.execute("SELECT id FROM roles WHERE nombre = %s", (rol,))
    rol_id = cursor.fetchone()

    if rol_id:
        cursor.execute("INSERT INTO usuario_rol (usuario_id, rol_id) VALUES (%s, %s)", (usuario_id, rol_id[0]))

    connection.commit()
    cursor.close()
    connection.close()

    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
