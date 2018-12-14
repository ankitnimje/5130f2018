from flask import Flask
from flask import request
from crawlers.DFScarwler import WebCrawler
from crawlers.WikiImageUrl import wiki
from flask_cors import CORS
import json


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Hello</title>
  <img src='''
  
contentp = '''alt="W3Schools.com">
</head>
<body>
Hello, World!
</body>
</html>
'''









app = Flask(__name__)
CORS(app)

#@app.route('/run-dfs-crawler', methods=['POST'])
@app.route('/run-crawler')
def crawl_dfs():
    #print(request.is_json)
    #c = request.get_json()
    #print(c)
    web_crawler = WebCrawler()
    sample_dict = web_crawler.crawl_start("Boston")
    return json.dumps(sample_dict)

@app.route('/run-wiki-image')
def crawl_wiki_image():
    imageCrawl = wiki()
    s = imageCrawl.wiki_image_url("Boston")
    q = json.dumps(s)
   
    #x = contents + " \" " + z + " \" "  + contentp
    return q
    

  

if __name__ == '__main__':
    app.run()
    