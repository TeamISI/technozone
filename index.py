#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
#import pccomponentes_scraper

# Creamos un objeto app de Flask
app = Flask(__name__)

# Indicamos la ruta para la pagina principal
@app.route('/')
# Definimos una funcion para la ruta de la pagina principal
def home():
    # Ejecuta la carga de la pagina inicial
    return render_template('home.html')

# Decorador para procesar la funcion en la ruta /get_phone_name
@app.route('/procesar', methods = ['POST', 'GET'])

# Funcion para obtener el nombre del telefono
def procesar():
    # Obtiene el nombre del telefono
    so = request.form.get("SO")
    ram = request.form.get("RAM")
    almacenamiento = request.form.get("Almacenamiento")
    camara = request.form.get('Camara')
    #nombre = pccomponentes_scraper.scraper("Huawei P40 Lite 6/128GB Midnight Black Libre")
    return render_template("comparador.html", SO = so, RAM = ram, Almacenamiento = almacenamiento, nombre = 'Xiaomi Readmi Note 8', Camara = camara)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
