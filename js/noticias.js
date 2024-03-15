document.querySelectorAll('.leer-mas').forEach(button => {
    button.addEventListener('click', function() {
      const card = this.closest('.card');
      const imagen = card.querySelector('.card-img-top').src;
      const titulo = card.querySelector('.card-title').textContent;
      const descripcion = this.getAttribute('data-descripcion');

      document.getElementById('noticiaModalLabel').textContent = titulo;
      document.getElementById('noticiaImagen').src = imagen;
      document.getElementById('noticiaTexto').textContent = descripcion;

      $('#noticiaModal').modal('show');
    });
  });
