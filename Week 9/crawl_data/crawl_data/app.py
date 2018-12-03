from flask import Flask
from crawlers.DFScarwler import DFSWebCrawler
import json

app = Flask(__name__)


@app.route('/run-dfs-crawler')
def crawl_dfs():
    web_crawler = DFSWebCrawler()
    sample_dict = web_crawler.crawl_start()
    return json.dumps(sample_dict)


if __name__ == '__main__':
    app.run()