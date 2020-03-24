from bs4 import BeautifulSoup
import requests

url = 'https://www.pccomponentes.com/buscar/?query=moviles'

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

phonesElements = page_content.findAll("div", {"class": "tarjeta-articulo__elementos-basicos"})

datos = []

def scraper(nombre):

    for phones in phonesElements:
        names = phones.find("a", {"class": "GTM-productClick enlace-disimulado"}).getText()
        datos.append(names)
    return datos[datos.index(nombre)]