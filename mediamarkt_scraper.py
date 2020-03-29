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

class MediamarktCrawler(CrawlSpider):
    name = 'mediamarkt'
    allowed_domains = ['mediamarkt.es']
    start_urls = ['https://www.mediamarkt.es/es/category/_smartphones-701189.html']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), follow=True),
    )

    def parse_items(self, response):
        item = ItemLoader(MediamarktItem, response)

        

        yield item.load_item()