document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menu-icon');
    const menu = document.getElementById('menu');

    menuIcon.addEventListener('click', function() {
        console.log('Clique no ícone de menu');
        menu.classList.toggle('show');
    });
});
