#!/usr/bin/env python
# -*- coding: utf-8 -

#pip install scrapy
import scrapy
from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

# Clase que almacena el contenido del scraping
class PhoneHouseItem(Item):
    nombre = Field()
    sistemaOperativo = Field()
    ram = Field()
    almacenamiento = Field()
    url = Field()
    imagen = Field()
    precio = Field()

class PhoneHouseCrawler(CrawlSpider):
    name = 'phone_house'
    allowed_domains = ['phonehouse.es']
    start_urls = ['https://www.phonehouse.es/moviles-y-telefonia/moviles/todos-los-smartphones.html']


    rules = (
        Rule(LinkExtractor(allow=r'/movil'), follow=True, callback='parse_items'),
    )

    def parse_items(self, response):
        item = ItemLoader(PhoneHouseItem(), response)
        item.add_xpath('nombre', '//*[@id="top-contenedor-principal"]/main/section[1]/div[1]/div/h1/text()')
        item.add_xpath('sistemaOperativo', '//*[@id="modulo-caracteristicas"]/div/div/div[5]/ul/li[1]/div[2]/text()')
        # Faltaría eliminar los caracteres GB
        item.add_xpath('ram', '//*[@id="modulo-caracteristicas"]/div/div/div[3]/ul/li[1]/div[2]/text()') #MapCompose(lambda i:i[0])
        # Faltaría eliminar los espacios en blanco y GB
        item.add_xpath('almacenamiento', '//*[@id="modulo-caracteristicas"]/div/div/div[3]/ul/li[2]/div[2]/text()')
        item.add_value('url', response.url)
        item.add_xpath('precio', '//*[@id="precios"]/div[2]/div[1]/h3/span[2]/text()')
        img = item.get_xpath('//*[@id="top-contenedor-principal"]/main/section[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/img/@src')
        contenido = 'https:' + str(img[0])
        item.add_value('imagen', contenido)

        # Faltaría eliminar los atributos del objeto que aparecen cada vez que se descargan los datos de la web

        yield item.load_item()
        
