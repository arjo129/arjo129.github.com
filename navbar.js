document.addEventListener('DOMContentLoaded', function() {
    fetch('navbar.html')
        .then(response => response.text())
        .then(data => {
            document.querySelector('header').innerHTML = data;
            
            // Highlight current page in navbar
            const currentPage = window.location.pathname.split('/').pop() || 'index.html';
            const currentLink = document.querySelector(`a.nav-link[href="${currentPage}"]`);
            if (currentLink) {
                currentLink.parentElement.classList.add('active');
            }
        });
});