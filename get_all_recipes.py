import urllib.request

file_to_read = open('url_list', 'r')

id = 0
url = file_to_read.readline()
print(url)
while url:
    file_to_write = open('recipes_html/recipe' + str(id) + '.html', 'wb')
    page = urllib.request.urlopen(url)
    bytes = page.read().decode('utf8')
    file_to_write.write(bytes.encode('utf8'))
    page.close()
    url = file_to_read.readline()
    id += 1;
