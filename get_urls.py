import urllib.request
import re
from bs4 import BeautifulSoup

file = open('url_list', 'w')

for i in range(0, 9):
    url = "https://www.ah.nl/allerhande/recepten-zoeken/__/N-26vq?Nrpp=1000&No=" + str(i) + "000"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    cur = 0
    for link in soup.find_all('a'):
        url_str = str(link.get('href'))
        if (bool(re.search('R-R', url_str)) and cur % 2 == 0):
            file.write('https://www.ah.nl' + url_str + '\n')
        if (bool(re.search('recepten-zoeken', url_str))):
            print(url_str)
        cur += 1