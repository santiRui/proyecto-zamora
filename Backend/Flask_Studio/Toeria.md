# Flask desde Cero 🚀

## Módulo 1: Introducción a Flask

1. ¿Qué es Flask?
2. Instalación de Flask y entorno virtual (`venv`).
3. Crear tu primer servidor Flask.
4. Configurar rutas básicas (`@app.route`).
5. Uso del método `GET` y `POST`.
6. Ejecutar la aplicación en modo desarrollo (`debug=True`).

---

### Desarrollo del modulo 1 
¿Qué es Flask?

Flask es un marco ligero para crear aplicaciones web en Python. Es fácil de usar, flexible y permite construir aplicaciones rápidas con poco código. No incluye muchas funcionalidades por defecto, lo que te da más control sobre cómo diseñar tu aplicación.

Instalación de Flask y entorno virtual (venv)

Antes de empezar, es recomendable usar un entorno virtual para que los paquetes de Python no interfieran con otros proyectos:

Crear el entorno virtual:
```python 
python -m venv venv

Activar el entorno virtual:

En Windows:

.\venv\Scripts\activate



Instalar Flask:

pip install flask


```
Pagina de documentacion https://flask.palletsprojects.com/en/stable/

### Crear tu primer servidor Flask

Vamos a crear un archivo llamado app.py para nuestro primer servidor:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Mundo!"

if __name__ == '__main__':
    app.run()

```
 @app.route('/'): Define la ruta principal de la aplicación.

 app.run(): Inicia el servidor de Flask.

 Configurar rutas básicas (@app.route)

Puedes crear diferentes rutas para que tu aplicación muestre distintas páginas:

@app.route('/')
def home():
    return "Bienvenido a la página principal"

@app.route('/about')
def about():
    return "Esta es la página acerca de nosotros"

Uso del método GET y POST

Flask soporta diferentes métodos HTTP como GET (para obtener datos) y POST (para enviar datos):

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        return f"Hola, {nombre}!"
    return '''
        <form method="post">
            <input type="text" name="nombre" placeholder="Tu nombre">
            <button type="submit">Enviar</button>
        </form>
    '''

```
GET: Cuando visitas la página.

POST: Cuando envías datos desde un formulario.

Ejecutar la aplicación en modo desarrollo (debug=True)

Es buena idea usar el modo de desarrollo para que los cambios se apliquen automáticamente y se muestren errores detallados:

if __name__ == '__main__':
    app.run(debug=True)

Esto hace que el servidor se reinicie automáticamente cuando detecta cambios en el códig


## Módulo 2: Estructura del Proyecto Flask

1. Entender la estructura de carpetas:

   * `app.py` (Archivo principal)
   * `templates/` (Archivos HTML)
   * `static/` (CSS, JS, imágenes)
2. Separación de lógica y diseño (`Jinja2`).
3. Crear rutas para diferentes páginas (`home`, `about`, `contact`).

---

## Módulo 3: Plantillas y Jinja2

1. Crear tu primer archivo HTML (`index.html`).
2. Uso de variables y bloques (`{{ }}`, `{% %}`).
3. Herencia de plantillas (`base.html`).
4. Manejo de bucles y condicionales (`for`, `if`).

---

## Módulo 4: Crear y Conectar Bases de Datos (PostgreSQL)

1. **¿Qué es una base de datos relacional?**
2. **Instalación de PostgreSQL y configuración:**

   * Crear un usuario (`postgres`).
   * Crear una base de datos (`Escuela2025`).
3. **Conexión a la base de datos:**

```python
import psycopg2

def get_connection():
    return psycopg2.connect(
        host='localhost',
        database='Escuela2025',
        user='postgres',
        password='Contraseña'  # Cambia esto
    )
```

4. **Crear tablas (`CREATE TABLE`).**
5. **Ejecución de consultas básicas (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).**
6. **Manejo de errores de conexión y transacciones.**

---

## Módulo 5: Formularios y Manejo de Datos

1. Crear formularios en HTML.
2. Manejar datos con `request.form`.
3. Validación básica de datos.
4. Enviar datos entre páginas (`GET`, `POST`).
5. Uso de `Flask-WTF` para formularios avanzados.

---

## Módulo 6: Bases de Datos con Flask y SQLAlchemy

1. Conectar Flask con PostgreSQL usando `SQLAlchemy`.
2. Crear y usar modelos.
3. Crear y consultar registros.
4. Migraciones con `Flask-Migrate`.
5. Relaciones entre tablas.

---

## Módulo 7: Autenticación y Seguridad

1. Crear rutas protegidas (`@login_required`).
2. Manejo de contraseñas (`bcrypt`, `werkzeug.security`).
3. Uso de sesiones (`session`).
4. Proteger datos sensibles.

---

## Módulo 8: APIs y JSON

1. Crear y consumir APIs con Flask.
2. Uso de `Flask-RESTful`.
3. Manejar respuestas JSON.
4. Conectar el backend Flask con un frontend separado.

---

## Módulo 9: Despliegue y Optimización

1. Desplegar en servicios como `Render`, `Railway`, o `Vercel`.
2. Uso de `nginx` y `gunicorn`.
3. Optimizar el rendimiento y la seguridad.
