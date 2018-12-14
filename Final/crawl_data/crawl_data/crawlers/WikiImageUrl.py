# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 23:39:43 2018

@author: Surbhi kanthed
"""

import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class wiki:
    
    def wiki_image_url(self,x):
        self.x=x
        seed = "https://en.wikipedia.org/wiki/" +self.x
      #  y=["a","b","c","d","e","f","g","h","i"]
        #z=0;
        html = urlopen(seed)
        bs = BeautifulSoup(html, 'html.parser')
        images = bs.find_all('img', {'src':re.compile('.jpg')})
        lis=[]
        for image in images: 
                
                #print(image['src']+'\n')
                x='https:'+image['src']
                print(x +'\n')
                lis.append(x)
                #urllib.request.urlretrieve(x, y[z]+"mm.jpg")
               # z=z+1
        return lis    

#w=wiki()
#w.wiki_image_url()