# Funciones Básicas de Flask

Flask ofrece una variedad de funciones para facilitar el desarrollo de aplicaciones web. Aquí hay una lista de algunas de las más importantes:

###  `Flask()`

Crea una instancia de la aplicación Flask:

```python
from flask import Flask
app = Flask(__name__)
```

###  `@app.route()`

Define una ruta para una URL específica:

```python
@app.route('/')
def home():
    return "¡Bienvenido a mi aplicación Flask!"
```

###  `render_template()`

Renderiza un archivo HTML desde la carpeta `templates`:

```python
from flask import render_template

@app.route('/pagina')
def pagina():
    return render_template('pagina.html')
```

###  `request`

Accede a los datos enviados por el cliente, como formularios o parámetros:

```python
from flask import request

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']
    return f"Usuario: {usuario}, Contraseña: {password}"
```

###  `redirect()` y `url_for()`

Redirige al usuario a otra página:

```python
from flask import redirect, url_for

@app.route('/inicio')
def inicio():
    return redirect(url_for('home'))
```

###  `session`

Permite almacenar datos del usuario en una sesión (necesita una `secret_key`):

```python
from flask import session
app.secret_key = 'mi_secreto'

@app.route('/guardar_dato')
def guardar_dato():
    session['nombre'] = 'Juan'
    return "Dato guardado"
```

###  `abort()`

Interrumpe una solicitud y devuelve un código de error:

```python
from flask import abort

@app.route('/prohibido')
def prohibido():
    abort(403)  # Error 403 - Prohibido
```

###  `jsonify()`

Devuelve datos en formato JSON:

```python
from flask import jsonify

@app.route('/api/datos')
def datos():
    return jsonify({'nombre': 'Juan', 'edad': 30})
```

Estas son solo algunas de las funciones más comunes de Flask, pero el framework ofrece muchas más para manejar errores, autenticar usuarios y conectar con bases de datos.
