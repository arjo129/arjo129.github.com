document.addEventListener('DOMContentLoaded', function() {
    // Get the root url: domain + port
    // For instance if its hosted at arjo129.github.io/subdirectory, then the root url is arjo129.github.io
    const root_url = window.location.origin;
    fetch(root_url + '/navbar.html')
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