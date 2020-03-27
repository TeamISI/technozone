from mediamarkt_scraper import Mediamarkt, Phone

url = 'https://www.mediamarkt.es/es/category/_smartphones-701189.html'

obj = Mediamarkt()
result = obj.connect(url)

if result:
    print ("Conectado")
else:
    print(obj.error)