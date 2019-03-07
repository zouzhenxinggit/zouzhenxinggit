#!/usr/bin/python
#coding=utf-8

import pytesseract
from PIL import Image

image = Image.open('qwer.png')
qwer = pytesseract.image_to_string(image)
print qwer
