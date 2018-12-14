# Program to design a DFS web Crawler

# all the libraries used throughout the program
import requests
from bs4 import BeautifulSoup
import time
import wikipedia


class WebCrawler():
    #def __init__(self, x):
            #self.x = x
            #print(self.x)
     
    
    #seed = "https://en.wikipedia.org/wiki/" 
    #frontier = [[seed, 1]]
    crawled_url = []
    reverse_temp = []
    crawled_pages = {}

    def crawl_url(self, url, depth):
        self.crawled_url.append(url)
        time.sleep(1)
        get_request = requests.get(url)
        soup = BeautifulSoup(get_request.content, "html.parser")
        prettify = soup.prettify()
        p=soup.find("h1", {"id": "firstHeading"}).get_text()
        print("\n")
        print(p)
        page = wikipedia.page(p).url
        #print(page.url)
        file_value = (str(len(self.crawled_url)))
        self.crawled_pages["crawled_page" + file_value] = page
        # with open("subhi_dfs_crawled_page" + file_value + ".html", "w", encoding='utf-8') as f:
        #     f.write(prettify)

        anchor_text = soup.find_all("a")

        for link in anchor_text:
            url = (str(link.get("href")))

            if (url.startswith("/wiki")
                    or url.startswith("https://en.wikipedia.org/wiki")
                    or url.startswith("//en.wikipedia.org/wiki")):

                if ("#" not in url) and (":" not in url) and ("Main_Page" not in url):
                    complete_url = "https://en.wikipedia.org" + url

                    if complete_url not in self.crawled_url:
                        url_depth_list = [complete_url, depth]
                        self.reverse_temp.append(url_depth_list)

        self.reverse_temp.reverse()
        self.frontier = self.frontier + self.reverse_temp
        del self.reverse_temp[:]

    def crawl_start(self,x):
        self.x = x
        print(self.x)
        seed = "https://en.wikipedia.org/wiki/" +self.x
        frontier = [[seed, 1]]
        self.frontier=frontier

        while len(self.frontier) != 0 and len(self.crawled_url) < 7:
            pop_url_depth_list = self.frontier.pop()
            url_depth = pop_url_depth_list[1]
            popped_url = pop_url_depth_list[0]
            #print(url_depth)

            if popped_url not in self.crawled_url:

                if url_depth < 8:
                    self.crawl_url(popped_url, url_depth + 1)
                   # print(self.frontier)

                if url_depth == 8:
                    self.crawled_url.append(popped_url)
                    time.sleep(1)
                    get_request = requests.get(popped_url)
                    soup = BeautifulSoup(get_request.content, "html.parser")
                    prettify = soup.prettify()
                    p=soup.find("h1", {"id": "firstHeading"}).get_text()
                    print("\n")
                    print(p)
                    page = wikipedia.page(p).url
                    #print(page.url)
                   
                    file_value = (str(len(self.crawled_url)))
                    self.crawled_pages["crawled_page" + file_value] = page

        return self.crawled_pages
                    # with open("dfs_crawled_page" + file_value + ".html", "w", encoding='utf-8') as f:
                    #     f.write(prettify)

    # with open("dfs_crawled_url.txt", "w") as f:
    #
    #     for url in self.crawled_url:
    #         f.write("%s\n" % url)


# web_crawler = DFSWebCrawler()
# web_crawler.crawl_start()
