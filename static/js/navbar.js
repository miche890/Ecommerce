document.addEventListener('DOMContentLoaded', () => {
    const url = window.location.pathname
    const activeLink = document.querySelector('a[href="' + url + '"]')
    if (activeLink) {
        activeLink.classList.add('active')
    }
})