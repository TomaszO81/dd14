import os
from PIL import Image

folder = '/Users/tomek/PycharmProjects/day3/dd14'
root = 'obrazek'

for nr, foto in enumerate(os.listdir(folder)):
    print(nr, foto)

    ext = os.path.splitext(foto)[1]
   # print(ext)