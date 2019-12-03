#!/usr/bin/python3
# coding: utf-8

from binascii import a2b_base64
from urllib.request import urlopen
import tesseract
import cv2.cv as cv
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
  grayScale = cv.LoadImage('image.jpeg', cv.CV_LOAD_IMAGE_GRAYSCALE)
  cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
  api = tesseract.TessBaseAPI()
  api.Init(".", "eng", tesseract.OEM_DEFAULT)
  api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
  api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
  tesseract.SetCvImage(gray, api)
  print (api.GetUTF8Text())


