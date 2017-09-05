import pickle

file_name = "recipes_html/recipe"
urls = open('url_list')
urls = urls.read()
urls = urls.splitlines()

count = 0

recipes = []
# loop over all recipes and select the ingredients
for num in range(9000):  # 999

    print(num)

    recipe_data = dict()
    recipe_data['link'] = urls[num]

    # open and read in the html file
    file = open(file_name + str(num) + ".html")
    html = file.read()


    def find_occ(_html_list, count):
        for i in range(len(_html_list)):
            if isinstance(_html_list[i], str):
                if 'div id="ingredients_to_shoplist"' in _html_list[i]:
                    return i, count
                elif 'recipeproducts?noNav=true' in html_list[i]:
                    return i, count
            elif isinstance(_html_list[i][0], str):
                if 'div id="ingredients_to_shoplist"' in _html_list[i][0]:
                    return i, count
                elif 'recipeproducts?noNav=true' in html_list[i][0]:
                    return i, count
            else:
                return -1, count


    # split in lines and focus on ingredients
    html_list = html.splitlines()
    x_0 = [i for i in range(len(html_list)) if "list shopping ingredient-selector-list" in html_list[i]][0]
    x_n, count = find_occ(html_list, count)
    html_ingredients = html_list[x_0:x_n]

    # get all ingredient classes
    ind = []
    for i in range(len(html_ingredients)):
        if 'itemprop="ingredients"' in html_ingredients[i]:
            ind.append(i)
    ind.append(-1)

    ingredient_info = []
    for i in range(len(ind) - 1):
        ingredient_info.append(html_ingredients[ind[i]:ind[i + 1]])

    ingredients = []
    for single_ingredient in ingredient_info:
        # data - description - singular = "geschilde bospeen"
        # data - quantity = "8"
        # data - quantity - unit - singular = ""
        ingredient = dict()
        for j in single_ingredient:
            if "data-description-singular" in j:
                ingredient['description'] = j[j.index('"') + 1:-1]
            if "data-quantity" in j and "unit" not in j:
                ingredient['quantity'] = j[j.index('"') + 1:-1]
            if "data-quantity-unit-singular" in j:
                ingredient['unit'] = j[j.index('"') + 1:-1]
        ingredients.append(ingredient)
    recipe_data['ingredients'] = ingredients

    details_start = [i for i in range(len(html_list)) if 'window.dataLayer' in html_list[i]][0]
    details = html_list[details_start:]


    def find_end(_input):
        for i in range(len(_input)):
            if "ingredienten" in _input[i]:
                return i


    details_end = find_end(details)
    for i in details[:details_end]:
        if "titel" in i:
            recipe_data['title'] = i.split(":")[1][1:-2]
        if "gang" in i:
            recipe_data['course'] = i.split(":")[1][1:-2]
        if "personen" in i:
            recipe_data['persons'] = int(i.split(":")[1][1:-2])
        if "bereidingstijd" in i:
            recipe_data['time'] = int(i.split(":")[1][1:-2])
        if "calorien" in i:
            try:
                recipe_data['calories'] = int(float(i.split(":")[1][1:-2]))
            except ValueError:
                recipe_data['calories'] = 0

    final_tags = []
    for i in range(len(details[:details_end])):
        if "tags" in details[:details_end][i]:
            tags = details[:details_end][i + 2:-1]
            for j in (tags):
                tt = ''.join(j.split())[1:-1]
                if tt[-1] == '"':
                    tt = tt[:-1]
                final_tags.append(tt)

    recipe_data['tags'] = final_tags
    recipes.append(recipe_data)

with open('recipe_db.pkl', 'wb') as f:
    pickle.dump(recipes, f)


# < script >
# window.dataLayer = {
#     "page": {
#         "type": "recept",
#         "context": {
#             "titel": "Vegan carrot hotdog",
#             "gang": "hoofdgerecht",
#             "personen": "8",
#             "bereidingstijd": "1460",
#             "calorien": "230.0",
#             "tags": [
#
#                 "lactosevrij",
#                 "veganistisch",
#                 "vegetarisch"
#             ],
