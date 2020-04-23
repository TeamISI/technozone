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

        nombre = page_content.find("h", attrs={"class":"f-productHeader-Title"})
        if(nombre != None):
            diccionario['nombre'] = nombre.text
        else:
            diccionario['nombre'] = ''

        imagen = page_content.find("img", attrs={"class":"f-productVisuals-mainMedia js-ProductVisuals-imagePreview"})
        if(imagen != None):
            diccionario['imagen'] = imagen['src']
        else:
            diccionario['imagen'] = ''

        # precio = page_content.find('span', attrs={"class":"w-product__price__current iss-product-current-price"})
        # if(precio != None):
        #     diccionario['precio'] = precio['content']
        # else:
        #     diccionario['precio'] = '0,00'



        diccionario['url'] = url

        f.write('#\n')
        writer = csv.writer(f, delimiter=';')
        writer.writerows(diccionario.items())
        
    f.write('#')