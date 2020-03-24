#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import pccomponentes_scraper
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
    so = request.form.get("SO")
    ram = request.form.get("RAM")
    dimension = request.form.get("Dimension")
    almacenamiento = request.form.get("Almacenamiento")
    nombre = pccomponentes_scraper.scraper("Huawei P40 Lite 6/128GB Midnight Black Libre")
    return render_template("comparador.html", SO = so, RAM = ram, Dimension = dimension, Almacenamiento = almacenamiento, nombre = nombre)

if __name__ == '__main__':
    app.run(debug=True)
