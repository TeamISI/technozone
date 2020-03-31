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
class MediaMarktItem(Item):
    nombre = Field()
    sistemaOperativo = Field()
    ram = Field()
    almacenamiento = Field()
    url = Field()
    imagen = Field()
    precio = Field()

class Worten(CrawlSpider):
    name = 'Worten'
    allowed_domains = ['worten.es']
    start_urls = ['https://www.worten.es/productos/moviles-smartphones/smartphones']


    rules = (
        Rule(LinkExtractor(callback='parse_items'),
         Rule(LinkExtractor(allow=r'page=\d+'), follow=True),
    )

    def parse_items(self, response):
       
        item = ItemLoader(WortenItem(), response)
       
        marca= item.get_xpath('//[@id="wrapper"]/div[3]/div[2]/div[4]/div/div/section[3]/div/div/div[2]/ul[1]/li[3]/span[2]/text()')
        modelo = item.get_xpath('//[@id="wrapper"]/div[3]/div[2]/div[4]/div/div/section[3]/div/div/div[2]/ul[1]/li[4]/span[2]/text()')
       
        marca = str(marca[0])
        modelo = str(modelo[0])
       
        name = marca + modelo
       
        item.add_value('nombre', name)

        item.add_xpath('sistemaOperativo', '//*[@id="wrapper"]/div[3]/div[2]/div[4]/div/div/section[3]/div/div/div[1]/ul[1]/li[1]/span[2]/text()')
        
        item.add_xpath('ram', '//*[@id="wrapper"]/div[3]/div[2]/div[4]/div/div/section[3]/div/div/div[2]/ul[3]/li[1]/span[2]/text()')
        
        item.add_xpath('almacenamiento', '//*[@id="wrapper"]/div[3]/div[2]/div[4]/div/div/section[3]/div/div/div[2]/ul[3]/li[2]/span[2]/text()')
        
        item.add_value('url', response.url)
        
        item.add_xpath('precio', '//*[@id="panel1c"]/div/div[1]/div[1]/span/text()')

        img = item.get_xpath('//*[@id="wrapper"]/div[3]/div[2]/div[2]/div/div/section/div/section[1]/div/div[1]/div/div[1]/div/img/@src')
        
        contenido = 'https:' + str(img[0])
        item.add_value('imagen', contenido)

        # Faltaría eliminar los atributos del objeto que aparecen cada vez que se descargan los datos de la web

        yield item.load_item()
        
