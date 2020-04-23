#!/usr/bin/env python
# -*- coding: utf-8 -

from bs4 import BeautifulSoup
import requests
import csv

'''
def getPages(url):
    
    page_response = requests.get(url, timeout=3)
    paginas = []
    page_content = BeautifulSoup(page_response.content, "html.parser")

    div = page_content.find("div", attrs={"class":"Carousel-container js-Carousel-container needHelp-list"})
    enlaces = div.find_all("a")

    for a in enlaces:
        paginas.append(a['href'])

    return paginas
'''

'''
def getLinks(url):
    page_response = requests.get(url, timeout=3)
    direcciones = []
    page_content = BeautifulSoup(page_response.content, "html.parser")
    principal = page_content.find_all("p", attrs={"class":"Article-desc"})

    for enlace in principal:
        cadena = enlace.find("a")['href']
        direcciones.append(cadena)

    return direcciones
'''

def changePage(url):
    page_response = requests.get(url, timeout=3)
    paginas = []
    page_content = BeautifulSoup(page_response.content, "html.parser")

    li = page_content.find_all("li", attrs={"class":"itemPage"})

    for i in li:
        a = i.find("a")['href']
        paginas.append(a)

    return paginas

'''
def getMoviles(url):
    
    #for url in urls:

    diccionario = {}
 
    page_response = requests.get(url, timeout=3)

    page_content = BeautifulSoup(page_response.content, "html.parser")

    nombre = page_content.find("h1", attrs={"class":"f-productHeader-Title"})
    if(nombre != None):
        #nombre = nombre.strip(' \n\r')
        diccionario['nombre'] = nombre.text
    else:
        diccionario['nombre'] = ''

    imagen = page_content.find("img", attrs={"class":"f-productVisuals-mainMedia js-ProductVisuals-imagePreview"})
    if(imagen != None):
        diccionario['imagen'] = imagen['src']
    else:
        diccionario['imagen'] = ''

    precio = page_content.find('span', attrs={"class":"f-priceBox-price f-priceBox-price--reco checked"})
    if(precio != None):
        #precio = precio.rstrip('€')
        diccionario['precio'] = precio.text
    else:
        diccionario['precio'] = '0,00'

    caracteristicas = page_content.find_all("li", attrs={"class":"Feature-item"})
    for row in caracteristicas:
        clave = row.find("span", attrs={"class":"Feature-label"}).text
        valor = row.find("span", attrs={"class":"Feature-desc"}).text
        diccionario[clave] = valor

    diccionario['url'] = url

    #     f.write('#\n')
    #     writer = csv.writer(f, delimiter=';')
    #     writer.writerows(diccionario.items())
        
    # f.write('#')

    return diccionario
'''


#diccionario = getMoviles('https://www.fnac.es/Xiaomi-Redmi-8-6-22-64GB-Negro-Telefono-movil-Smartphone/a7286810')

#print(diccionario.items())

#lista = getLinks('https://www.fnac.es/Smartphones-Libres/Smartphones-Xiaomi/n42587#bl=TMGSmartphones-SamsungARBO')

#paginas = getPages('https://www.fnac.es/telefono-MP3-GPS/Smartphones-Libres/s39887#bl=MMSmartphone')

paginas = changePage('https://www.fnac.es/Smartphones-Libres/Smartphones-Xiaomi/n42587')
for i in paginas:
    print(i)