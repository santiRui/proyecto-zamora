function validateFields() {
    const dni = document.getElementById('dni').value;
    const email = document.getElementById('email').value;

    if (!dni || !email) {
        alert('Ambos campos deben estar llenos. Por favor, inténtelo de nuevo.');
        return;
    }

    if (!/^\d+$/.test(dni)) {
        alert('El DNI debe contener solo números. Por favor, inténtelo de nuevo.');
        return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        alert('Ingrese un correo electrónico válido.');
        return;
    }

    alert('Datos enviados correctamente.');
}
 