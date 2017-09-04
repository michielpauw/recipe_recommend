import urllib.request
import re
from bs4 import BeautifulSoup

url = "https://www.ah.nl//allerhande/recepten-zoeken/__/N-26vq?No=1000"
page = urllib.request.urlopen(url)
file = open('url_list', 'w')

soup = BeautifulSoup(page, 'html.parser')
cur = 0

for link in soup.find_all('a'):
    url_str = str(link.get('href'))
    if (bool(re.search('R-R', url_str)) and cur % 2 == 0):
        file.write('https://www.ah.nl' + url_str + '\n')
    cur += 1