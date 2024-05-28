document.getElementById('seePasswords').addEventListener('change', (e) => {
    const inputPassword = document.getElementById('floatingPassword1');
    const inputConfirmPassword = document.getElementById('floatingPassword2');

    if (inputPassword.type === 'password' || inputConfirmPassword.type === 'password') {
        inputPassword.type = 'text';
        inputConfirmPassword.type = 'text';
    } else {
        inputPassword.type = 'password';
        inputConfirmPassword.type = 'password';
    }
})