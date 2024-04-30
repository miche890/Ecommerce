document.addEventListener('DOMContentLoaded', () => {
    const url = window.location.pathname
    console.log(url)
    const activeLink = document.querySelector('a[href="' + url + '"]')

    if (activeLink) {
        activeLink.classList.add('active')
    }
})