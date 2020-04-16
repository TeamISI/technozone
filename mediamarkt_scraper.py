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
class MediamarktItem(Item):
    nombre = Field()
    sistemaOperativo = Field()
    ram = Field()
    almacenamiento = Field()
    url = Field()
    imagen = Field()
    precio = Field()

class MediaMarkt(CrawlSpider):
    name = 'mediamarkt'
    allowed_domains = ['mediamarkt.es']
    start_urls = ['https://www.mediamarkt.es/es/category/_smartphones-701189.html']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/product'), callback='parse_items', follow=True),
    )

    def parse_items(self, response):

        item = ItemLoader(MediamarktItem(), response)

        name = item.get_xpath('//*[@id="product-details"]/div[1]/h1/text()')
        name = str(name[0])
        result = ' '
        for a in name:
            if(a == ','):
                break
            result += a

        item.add_value('nombre', result)

        ram = item.get_xpath('//*[@id="features"]/section[1]/dl/dd[7]/text()')
        ram = str(ram[0])
        contenido = ram[0].rstrip(' GB')
        item.add_value('ram', contenido)
        
        item.add_xpath('sistemaOperativo', '//*[@id="features"]/section[1]/dl/dd[2]/text()')
        
        alm = item.get_xpath('//*[@id="features"]/section[1]/dl/dd[5]/text()')
        alm = str(alm[0])
        contenido = alm.rstrip(' GB')
        item.add_value('almacenamiento', contenido)

        item.add_value('url', response.url)
        
        item.add_xpath('precio', '//*[@id="product-details"]/div[2]/div[1]/meta[2]/@content')

        img = item.get_xpath('//*[@id="product-sidebar"]/div[1]/a/img/@src')
        contenido = 'https:' + str(img[0])
        item.add_value('imagen', contenido)

        
        # Faltaría eliminar los atributos del objeto que aparecen cada vez que se descargan los datos de la web

        yield item.load_item()
        