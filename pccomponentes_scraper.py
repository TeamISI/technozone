from bs4 import BeautifulSoup
import requests

url = 'https://www.pccomponentes.com/buscar/?query=moviles'

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

phonesElements = page_content.findAll("div", {"class": "tarjeta-articulo__elementos-basicos"})


for phones in phonesElements:
    names = phones.find("a", {"class": "GTM-productClick enlace-disimulado"}).getText()

    print(names)
