from bs4 import BeautifulSoup
import urllib.request

recipe_link = urllib.request.urlopen("https://www.ah.nl/allerhande/recept/R-R1188623/thaise-noedels-met-varkensreepjes-en-wortellinten")
recipe_html = recipe_link.read()
recipe_link.close()

soup = BeautifulSoup(recipe_html, "html.parser")  # take html and make searchable tree
print(soup.title.string)  # get page title
print(soup.body.a)


# 4 personen, 615 kcal voedingswaarden, 25 min. bereiden
# Ingrediënten
# tags