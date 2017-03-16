from PIL import Image
import os

folder = '/Users/tomek/PycharmProjects/day3/dd14'
plik = 'world.jpg'

sciezka = os.path.join(folder, plik)

foto = Image.open(sciezka)

print(foto.size)
print(foto.format)
#print(foto.format.description)

nowy = foto.resize((round(foto.width/2)), round(foto.height/2))
print('Nowy rozmiwar:', nowy.size)

nowa_nazwa = 'srednplik.jpg'