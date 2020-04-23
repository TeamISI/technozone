#!/usr/bin/env python
# -*- coding: utf-8 -

from bs4 import BeautifulSoup
import requests
import csv

def getMoviles(urls, f):
    
    for url in urls:
        
        diccionario = {}

        page_response = requests.get(url, timeout=3)

        page_content = BeautifulSoup(page_response.content, "html.parser")

        caracteristicas = page_content.find_all("li", attrs={"class":"clearfix"})

        imagen = page_content.find("img", attrs={"class":"w-product-gallery__main_image__pic"})
        if(imagen != None):
            img = 'https://www.worten.es/' + imagen['src']
            diccionario['imagen'] = img
        else:
            diccionario['imagen'] = ''

        nombre = page_content.find("span", attrs={"class":"w-section__product"})
        if(nombre != None):
            diccionario['nombre'] = nombre.text
        else:
            diccionario['nombre'] = ''
        
        precio = page_content.find('span', attrs={"class":"w-product__price__current iss-product-current-price"})
        if(precio != None):
            diccionario['precio'] = precio['content']
        else:
            diccionario['precio'] = '0,00'

        for row in caracteristicas:
            clave = row.find("span", attrs={"class":"details-label"}).text
            valor = row.find("span", attrs={"class":"details-value"}).text
            valor = valor.replace('\n','')
            diccionario[clave] = valor

        diccionario['url'] = url

        f.write('#\n')
        writer = csv.writer(f, delimiter=';')
        writer.writerows(diccionario.items())
        
    f.write('#')

def getLinks(url):
    
    page_response = requests.get(url, timeout=3)
    direcciones = []
    page_content = BeautifulSoup(page_response.content, "html.parser") 
    principal = page_content.find("div", attrs={"id":"products-list-block"})

    #for contenido in principal:
    cont_movil = principal.find_all("div", attrs={"class":"w-product__wrapper"})
    for enlace in cont_movil:
        a = enlace.findChild()
        cadena = 'https://www.worten.es' + a['href']
        direcciones.append(cadena)

    return direcciones


def getPages(url):

    page_response = requests.get(url, timeout=3)
    paginas = []
    page_content = BeautifulSoup(page_response.content, "html.parser")

    lista = page_content.find("ul", attrs={"class":"pagination text-center"})
    li = (lista.findChildren()[9])
    a = li.findChild()

    final = int(a["data-page"])
    paginas.append(url)
    for i in range(2, final+1):#final+1
        cadena = url + '?page=' + str(i)
        paginas.append(cadena)
    
    return paginas

paginas = getPages('https://www.worten.es/productos/moviles-smartphones/smartphones')

f = open("./worten.csv", "w")

for p in paginas:
    urls = getLinks(p)
    getMoviles(urls, f)

f.close()