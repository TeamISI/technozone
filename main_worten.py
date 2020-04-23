#!/usr/bin/env python
# -*- coding: utf-8 -

from database_connection import *
from decimal import *

class Phone(object):
    def __init__(self, ean, nombre='', marca='', descripcion='', modelo=''):
        self.EAN = ean
        self.nombre = nombre
        self.marca = marca
        self.descripcion = descripcion
        self.modelo = modelo    
    
    def mostrar(self):
        cadena ='EAN: ' + self.EAN + '\n' + 'Nombre: ' + self.nombre + '\n' + 'Marca: ' + self.marca +  '\n' + 'Descripcion: ' + self.descripcion + '\n' + 'Modelo: ' + self.modelo
        return cadena

class Precios(object):
    def __init__(self, ean, precio, url, img):
        self.EAN = ean
        self.precio = precio
        self.url = url
        self.imagen = img


lista = []

f = open("./worten.csv", "r")
linea = f.readline()
separador = ';'
diccionario = {}

for linea in f:

    if(linea[0] != '#'):
        separado = linea.split(separador)
        clave = separado[0]
        valor = (separado[1]).rstrip('\n')
        diccionario[clave] = valor
    else:
        lista.append(diccionario)
        diccionario = {}

f.close()

moviles = []
precios = []

for i in lista:
    movil = Phone(i.get('EAN'), i.get('nombre'), i.get('Marca'), i.get('Descripcion'),i.get('Modelo'))
    moviles.append(movil)
    precio = Precios(i.get('EAN'), i.get('precio'), i.get('url'), i.get('imagen'))
    precios.append(precio)

obj = Technozone()

result = obj.mysqlConnect('localhost','arcadio','practicasISI/1920','technozone')


if result:
    
    for i in moviles:
        records = (i.EAN, i.nombre, i.marca, i.descripcion, i.modelo)
        obj.prepare("INSERT INTO moviles (EAN, Nombre, Marca, Descripcion, Modelo) VALUES (%s, %s, %s, %s, %s)", records)
    print (obj.lastId)

    for i in precios:
        cantidad = i.precio
        cantidad = cantidad.replace(',','.')
        records = (i.EAN, Decimal(cantidad), i.url, i.imagen)
        obj.prepare("INSERT INTO precios (EAN, Precio, Url, Imagen) VALUES (%s, %s, %s, %s)", records)
    print (obj.lastId)

    obj.mysqlClose()
else:
    print (obj.error)