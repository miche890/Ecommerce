document.addEventListener('DOMContentLoaded', function() {
    const url = new URL(window.location.href);
    const selectedValue = url.searchParams.get('campo')
    if (selectedValue) {
        const selectElement = document.getElementById('campos_select')
        selectElement.value = selectedValue;
    }
});

document.getElementById('campos_select').addEventListener('change', function() {
    const selectedValue = this.value;
    if (selectedValue && selectedValue !== '---') {
        const currentUrl = window.location.href;
        const url = new URL(currentUrl)
        url.searchParams.set('campo', selectedValue)
        window.location.href = url.toString();
    } else if (selectedValue === '---') {
        const currentUrl = window.location.href;
        const url = new URL(currentUrl)
        url.searchParams.delete('campo')
        window.location.href = url.toString();
    }
})

