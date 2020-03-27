#!/usr/bin/env python
# -*- coding: utf-8 -

from bs4 import BeautifulSoup
import requests

class Phone(object):
    def __init__(self, name, so, memory,ram, url, price, img):
        self.name = name
        self.so = so
        self.memory = memory
        self.ram = ram
        self.url = url
        self.price = price
        self.img = img


class Mediamarkt(object):
    def __init__(self):
        self.error = ""
        self.connected = 0
    
    def connect(self, url):
        try:
            self.page_response = requests.get(url=url, timeout=5)
            self.page_content = BeautifulSoup(self.page_response.content, "html.parser")
            self.connected = 1
            return True
        except Exception as e:
            self.error="Error: %s" % (e)

    def get_content(self, tag, attribute, attribue_name):
        self.content =  self.page_content.fin


'''
phones_contents = page_content.findAll("div", {"class": "content"})

movil = Phone("Readmi Note 8 Pro", "Android", 128, 6, "https://www.mediamarkt.es/es/product/_m%C3%B3vil-xiaomi-redmi-note-8-pro-azul-128-gb-6-gb-ram-6-53-full-hd-helio-g90t-4500-mah-android-1469588.html", 249, " ")

phones = [] # Vector de moviles

phones.append(movil)

for i in phones:
    print("Nombre: " + i.name)
    print("Sistema Operativo: " + i.so)
    print("RAM: " + str(i.ram))
    print("Url: " + i.url)
    print("Almacenamiento interno: " + str(i.memory))
    print("Precio: " + str(i.price) + "€")
    print("Imagen: " + i.img)
'''
'''
def scraper(ram, so, memory):
    for features in phones_contents:
        h2 = features.find("h2")
        names = h2.find("a").getText()
'''