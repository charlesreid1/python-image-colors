from PIL import Image
import sys
import os.path

for imgFile in os.listdir('/Users/charles/codes/python_img'):
    if( imgFile.find('JPG') > 0 ):
        img = Image.open(imgFile)
        img.resize((200,200))
        img.save(imgFile)

