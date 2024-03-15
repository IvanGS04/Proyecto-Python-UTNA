document.getElementById("btnPopup").addEventListener("click", function() {
  document.getElementById("popup").style.display = "block";
});

document.getElementById("close").addEventListener("click", function() {
  document.getElementById("popup").style.display = "none";
});

window.onclick = function(event) {
  if (event.target == document.getElementById("popup")) {
    document.getElementById("popup").style.display = "none";
  }
}

document.getElementById("registrationForm").addEventListener("submit", function(event) {
  event.preventDefault();
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  
  var users = JSON.parse(localStorage.getItem("users")) || [];
  users.push({ username: username, email: email, password: password });
  localStorage.setItem("users", JSON.stringify(users));
  
  alert("Usuario registrado exitosamente.");
  document.getElementById("popup").style.display = "none";
  enableDownload();
});

function enableDownload() {
  document.getElementById("btnPopup").style.display = "none"; // Oculta el botón de descarga
  document.getElementById("btnDownloaded").style.display = "block"; // Muestra el nuevo botón
  document.getElementById("btnDownloaded").setAttribute("onclick", "downloadFile()");
  
}

function downloadFile() {
  window.location.href = "/dist/interfazGrafica.exe";
}