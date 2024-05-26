document.getElementById('minus').addEventListener('click', function () {
    const inputCantidad = document.getElementById('cantidad');
    const valueCantidad = parseInt(inputCantidad.value)

    if (valueCantidad > 1) {
        inputCantidad.value = valueCantidad - 1;
    }
})

document.getElementById('plus').addEventListener('click', function () {
    const inputCantidad = document.getElementById('cantidad');
    const valueCantidad = parseInt(inputCantidad.value)

    inputCantidad.value = valueCantidad + 1;
})