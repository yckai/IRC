#!/usr/bin/python3
# coding: utf-8

from binascii import a2b_base64
from urllib.request import urlopen
import tesserocr
url = "http://challenge01.root-me.org/programmation/ch8/index.php"
html = urlopen(url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
for res in soup.findAll('img'):
  imgsrc = res.get('src').replace("data:image/png;base64,", "")
  print (imgsrc)
  binary_data = a2b_base64(imgsrc)
  fd = open('image.png', 'wb')
  fd.write(binary_data)
  fd.close()


