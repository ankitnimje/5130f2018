import urllib.request
import re
import time
from bs4 import BeautifulSoup

def focus_crawl(a_href):
    focus_counter = 0
    a_text = a_href.text
    f_url = a_href.get('href',None)
    array_words = str(a_href).split("/")
    for array in array_words:
        if  ((array.startswith('Rain'))
             or (array.startswith('rain'))
             or (array.endswith('Rain'))
             or (array.endswith('rain'))
             or ('_rain' in array)
             or ('rain_' in array)
             or ('Rain_' in array)
             or ('-rain' in array)
             or ('rain-' in array)
             or ('Rain-' in array)):
            focus_counter = focus_counter + 1

    if ((a_text.startswith('Rain'))
        or (a_text.startswith('rain'))
        or (a_text.endswith('Rain'))
        or (a_text.endswith('rain'))
        or ('_rain' in a_text)
        or ('rain_' in a_text)
        or ('Rain_' in a_text)
        or ('-rain' in a_text)
        or ('rain-' in a_text)
        or ('Rain-' in a_text)):
        focus_counter = focus_counter + 1

    if (focus_counter > 1):
        return True
    else: return False

def url_scraping(url):
    time.sleep(1)
    html_page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_page, "html.parser")
    return_val = 0

    f = 1
    input_html = open('focused_crawler_html' + str(f) + '.txt', 'w')
    input_html.write(str(html_page))
    input_html.close
    f = f + 1

    wiki_list = soup.find_all('a', attrs={'href': re.compile("^/wiki/")})
    for wurl in wiki_list:
        anchor_text = wurl.text
        wiki_url = wurl.get('href',None)
        if ':' not in wiki_url:
            frontier_url = "https://en.wikipedia.org" + str(wiki_url)
            in_url = "https://en.wikipedia.org" + str(wiki_url)
        elif '/wiki/Main_Page' not in wiki_url:
            frontier_url = "https://en.wikipedia.org" + str(wiki_url)
            in_url = "https://en.wikipedia.org" + str(wiki_url)
        else:
            in_url = "https://en.wikipedia.org" + str(wiki_url)
        if focus_crawl(wurl):
            frontier_url = "https://en.wikipedia.org" + str(wiki_url)
            if frontier_url not in frontier:
                frontier.append(frontier_url)
        if in_url not in seen:
            seen.append(in_url)
        return_val = return_val + 1
    return return_val

seed = "https://en.wikipedia.org/wiki/Tropical_cyclone"
seen = [seed]
frontier = []
i = 0
depth = 1
counter = 0
count_url = 1

while (i <= len(seen)):
    if(depth <= 6 and len(frontier) < 5):
        url_returned = url_scraping(seen[i])
        i = i + 1
        if(count_url != 0):
            counter = counter + url_returned
            count_url = count_url - 1
        if(count_url == 0):
            depth = depth + 1
            count_url = counter
            counter = 0
    else: break

input_url = open('Focused_crawled_url' + '.txt','w')
for f in frontier:
    input_url.write(str(f))
input_url.close