# Documentación Básica de Flask

### 🔹 Introducción

Flask es un microframework para Python diseñado para ser minimalista, rápido y flexible. Es ideal para crear APIs y aplicaciones web pequeñas o medianas, permitiendo un control detallado sobre el manejo de rutas, respuestas y plantillas HTML.

### 🔹 Instalación

Para instalar Flask, ejecuta el siguiente comando en tu entorno virtual o en el sistema global:

```bash
pip install flask
```

### 🔹 Configuración del Proyecto

Crea una carpeta para tu proyecto y, dentro de ella, un archivo principal `app.py` para tu aplicación Flask. La estructura básica puede ser algo como:

```
mi_proyecto/
│
├── app.py          # Archivo principal
├── templates/      # Plantillas HTML
├── static/         # Archivos estáticos (CSS, JS, imágenes)
└── requirements.txt # Lista de dependencias (opcional)
```

### 🔹 Estructura Básica de un Archivo Flask

El archivo principal `app.py` debe tener al menos la estructura básica para iniciar la aplicación:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### 🔹 Ejecutando el Servidor

Para iniciar el servidor de Flask, asegúrate de estar en la carpeta raíz del proyecto y ejecuta:

```bash
python app.py
```

Esto levantará el servidor en `http://127.0.0.1:5000` de forma predeterminada.

### 🔹 Conexión a Base de Datos (PostgreSQL)

Si planeas usar PostgreSQL, instala el conector `psycopg2`:

```bash
pip install psycopg2-binary
```

Luego, configura la conexión en un archivo como `database.py`:

```python
import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='123456', #Se pone contraseña 
        database='mi_base_de_datos'
    )
    return connection
```

Esto te permitirá manejar la conexión a tu base de datos de forma centralizada.
