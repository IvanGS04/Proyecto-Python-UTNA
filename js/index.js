//Funcionalidad del loader
window.addEventListener("load", function(){
  this.document.getElementById("loader").classList.toggle("loader2");
});


const imagen = document.getElementById('imagen');

imagen.addEventListener('click', function() {
  if (this.classList.contains('ampliada')) {
    this.classList.remove('ampliada');
  } else {
    this.classList.add('ampliada');
  }
});