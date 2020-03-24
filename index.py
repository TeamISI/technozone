#workon venv // deactivated
from flask import Flask, render_template, request

# Creamos un objeto app de Flask
app = Flask(__name__)

# Indicamos la ruta para la página principal
@app.route('/')
# Definimos una función para la ruta de la página principal
def home():
    # Ejecuta la carga de la página inicial
    return render_template('home.html')

# Decorador para procesar la función en la ruta /get_phone_name
@app.route('/procesar', methods = ['POST', 'GET'])
# Función para obtener el nombre del teléfono
def procesar():
    # Obtiene el nombre del telefono
    phone_name = request.form.get("nombre")
    return render_template("comparador.html", nombre = phone_name)

if __name__ == '__main__':
    app.run(debug=True)
