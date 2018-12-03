# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:39:43 2018

@author: Surbhi kanthed
"""

import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

y=["a","b","c","d","e","f","g","h","i"]
z=0;
html = urlopen('https://en.wikipedia.org/wiki/Elon_musk')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
        #print(image['src']+'\n')
        x='https:'+image['src']
        print(x +'\n')
        urllib.request.urlretrieve(x, y[z]+"mm.jpg")
        z=z+1
