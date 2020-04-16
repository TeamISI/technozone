class Phone(object):
    def __init__(self, name="Hola", so="Hola", memory="Hola",ram="Hola", url="Hola", price="Hola", img="Hola"):
        self.name = name
        self.so = so
        self.memory = memory
        self.ram = ram
        self.url = url
        self.price = price
        self.img = img

    def mostrar(self):
        cadena ='Nombre: ' + self.name + '\n' + 'SO: ' + self.so + '\n' + 'Almacenamiento: ' + self.memory + '\n' + 'Ram: ' + self.ram + '\n' + 'Url: ' + self.url + '\n' +'Precio: ' + self.price + '\n' + 'Imagen: ' + self.img
        return cadena


lista = []

f = open("./phone_house_data.csv", "r")
linea = f.readline()

for linea in f:
    contenido = ''
    contador = 0
    movil = Phone()
    for a in linea:

        if(a != ',' and a != '\n'):
            contenido += a
        else:
            if (contador == 0):
                movil.img = contenido
            elif (contador == 1):
                movil.url = contenido
            elif (contador == 2):
                movil.ram = contenido
            elif (contador == 3):
                movil.price = contenido
            elif (contador == 4):
                movil.name = contenido
            elif (contador == 5):
                movil.memory = contenido
            else:
                movil.so = contenido

            contador = contador + 1
            contenido = ''

    lista.append(movil)

f.close()
