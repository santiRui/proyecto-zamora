function validatePasswords() {
    const newPassword = document.getElementById('new-password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (!newPassword || !confirmPassword) {
        alert('Ambos campos deben estar llenos. Por favor, inténtelo de nuevo.');
        return;
    }

    if (newPassword !== confirmPassword) {
        alert('Las contraseñas no coinciden. Por favor, inténtelo de nuevo.');
    } else {
        alert('Contraseña cambiada con éxito.');
    }
}
