document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchInput = document.getElementById('searchInput');
    
    searchForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Evita que se envíe el formulario
        
        const searchTerm = searchInput.value.trim();
        
        // Utiliza window.find() para buscar y resaltar la palabra
        const found = window.find(searchTerm);
        
        // Si no se encuentra la palabra, muestra un mensaje
        if (!found) {
            alert('La palabra no se encontró en la página.');
        }
    });
});
