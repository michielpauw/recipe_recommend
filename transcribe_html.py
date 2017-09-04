from bs4 import BeautifulSoup
import urllib.request

recipe_link = urllib.request.urlopen(
    "https://www.ah.nl/allerhande/recept/R-R1188623/thaise-noedels-met-varkensreepjes-en-wortellinten")
recipe_html = recipe_link.read()
recipe_link.close()

soup = BeautifulSoup(recipe_html, "html.parser")  # take html and make searchable tree

# print(soup.title.string)  # get page title
# print(soup.body)

# 4 personen, 615 kcal voedingswaarden, 25 min. bereiden
#
# <h2 class="hidden-phones">Naast échte noedels eet je vanavond oranje noedel-lookalikes: wortellinten. </h2>
# </header> </section>
# section class="info hidden-phones">
# <ul class="short">
# <li><div class="icon icon-course"></div><span>hoofdgerecht</span></li>
# <li><div class="icon icon-people"></div><span><a class="servings js-scaler__scrollto">4 personen</a></span></li>
# <li><div class="icon icon-nutritional"></div><span>615 kcal <a class="more" href="#">voedingswaarden</a></span></li>
# <li class="cooking-time">
# <ul>
# <li content="PT25M"><div class="icon icon-time"></div>25 min. bereiden</li>
# </ul> </li> </ul> <form action="/allerhande/cartridges/PageSlot/PageSlot.jsp;WLSESSIONID=J8NM_d6lwMqBJyeutBGT4VYxG0rMne29Y4CEVC1CwrEFnsTXBIER!2085701064?_DARGS=/allerhande/cartridges/RecipeDetail2.0/Summary.jsp.rateRecipeForm" id="rateRecipeForm" method="POST" style="display: none;"><div style="display:none"><input name="_dyncharset" type="hidden" value="UTF-8"/> </div><div style="display:none"><input name="_dynSessConf" type="hidden" value="-1184681002497417532"/> </div><input name="/allerhande/rating/RateRecipeFormHandler.recipeId" type="hidden" value="1188623"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.recipeId" type="hidden" value=" "/><input id="submitRatingValue" name="/allerhande/rating/RateRecipeFormHandler.rating" size="1" type="hidden" value="3"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.rating" type="hidden" value=" "/><input name="/allerhande/rating/RateRecipeFormHandler.rateRecipe" type="hidden" value="true"/><input name="_D:/allerhande/rating/RateRecipeFormHandler.rateRecipe" type="hidden" value=" "/><div style="display:none"><input name="_DARGS" type="hidden" value="/allerhande/cartridges/RecipeDetail2.0/Summary.jsp.rateRecipeForm"/> </div></form>
# <div class="rating ">

list_child = []
list_child2 = []
list_child3 = []
list_child4 = []
for child in soup.body.children:
    list_child.append(child)

for child in list_child[3].children:
    list_child2.append(child)

for child in list_child2[3].children:
    # print('-'*50)
    # print(child)
    list_child3.append(child)

ts = list_child3[-2]
for child in ts.children:
    ts = child

strt = ts.find('context": {')
ts = ts[strt::]
ss = ts.find("{")
nd = ts.find("}")
chart = ts[(ss+1):nd]
elmst = chart.split(',')
# for j in elmst:
#     print("-"*50)
#     print(j)

recipe_details = dict()

for i in elmst:
    if "titel" in i:
        recipe_details['titel'] = i.split(":")[1][1:-2]
    if "personen" in i:
        recipe_details['personen'] = i.split(":")[1][1:-1]
    if "bereidingstijd" in i:
        recipe_details['bereidingstijd'] = i.split(":")[1][1:-1]
    if "calorien" in i:
        recipe_details['calorien'] = i.split(":")[1][1:-1]

for i in range(len(elmst)):
    if "tags" in elmst[i]:
        start = i
    if "ingredienten" in elmst[i]:
        end = i

print(elmst[start:end])
print(elmst[end:])

# for i in elmst:
#     if "tags" in i:
#         recipe_details['tags'] = i.split(":")[1][1:-2]
#     if "ingredienten" in i:
#         recipe_details['ingredienten'] = i.split(":")[1][1:-2]
print(recipe_details)