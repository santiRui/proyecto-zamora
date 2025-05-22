# Envío de Correos con Flask usando Gmail y Librerías Nativas de Python

Flask facilita el envío de correos electrónicos utilizando las bibliotecas estándar de Python como `smtplib` para SMTP y `email.message` para construir mensajes. Aquí tienes una guía paso a paso:

### Configuración Básica

Crea el archivo `app.py` para manejar el envío de correos:

```python
import smtplib
from email.message import EmailMessage
from flask import Flask, request, jsonify

app = Flask(__name__)


def enviar_correo(gmail, codigo):
    # Configura el mensaje
    msg = EmailMessage()
    msg.set_content(f'Hola, para recuperar tu contraseña, utiliza el siguiente código: {codigo}')
    msg['Subject'] = 'Recuperación de Contraseña'
    msg['From'] = '2025pruebax@gmail.com'  # Tu correo de envío
    msg['To'] = gmail
    # EL SMTP ES PROTOCOLO SIMPLE de TRANFERENCIA de Correo
    try:
        # Enviar el mensaje
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('2025pruebax@gmail.com', 'vkvt ibqh uiyr fcpm')  # Cambia esto por tu contraseña real
            server.send_message(msg)
        return "Mensaje enviado exitosamente"
    except Exception as e:
        print(e)
        return "No se pudo enviar el mensaje"


@app.route('/enviar_codigo', methods=['POST'])
def enviar_codigo():
    data = request.json
    destinatario = data.get('gmail')
    codigo = data.get('codigo', '123456')
    return enviar_correo(destinatario, codigo)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
```
