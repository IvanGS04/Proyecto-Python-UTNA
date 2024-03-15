from flask import Flask, render_template
# app.py
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bienvenido a la interfaz web de TinyGS</h1><p><a href="/descargar-app">Descargar la aplicación de escritorio</a></p>'

@app.route('/descargar-app')
def descargar_app_desktop():
    # Ruta a tu aplicación de escritorio (reemplaza con la ruta correcta)
    ruta_app_desktop = 'interfazGrafica.py'
    return send_file(ruta_app_desktop, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

