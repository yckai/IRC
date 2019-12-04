from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from seleniumrequests import Firefox
from binascii import a2b_base64
import pytesseract
import requests
import os
from seleniumwire import webdriver
from PIL import Image, ImageOps, ImageEnhance

driver = Firefox()
driver.get('http://challenge01.root-me.org/programmation/ch8/index.php')
html = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
for res in soup.findAll('img'):
    imgsrc = res.get('src').replace("data:image/png;base64,", "")
    binary_data = a2b_base64(imgsrc)
    fd = open('image.png', 'wb')
    fd.write(binary_data)
    fd.close()


def solve_captcha(path):
    image = Image.open(path).convert('RGB')
    image = ImageOps.autocontrast(image)

    filename = "{}.png".format(os.getpid())
    image.save(filename)

    text = pytesseract.image_to_string(Image.open(filename))
    return text


print('-- Resolving')
captcha_text = solve_captcha('image.png')
print('-- Result: {}'.format(captcha_text))
urlrtm = "http://challenge01.root-me.org/programmation/ch8/index.php"
data1 = format(captcha_text).replace(" ", "")
print(data1)
response = driver.request('POST', urlrtm, data={'cametu': data1})
print(response.content)




