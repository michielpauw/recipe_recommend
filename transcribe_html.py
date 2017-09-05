file_name = "recipes_html/recipe"

# loop over all recipes and select the ingredients
for num in range(3):  # 999

    recipe_data = dict()

    # open and read in the html file
    file = open(file_name + str(num) + ".html")
    html = file.read()

    # split in lines and focus on ingredients
    html_list = html.splitlines()
    x_0 = [i for i in range(len(html_list)) if "list shopping ingredient-selector-list" in html_list[i]][0]
    x_n = [i for i in range(len(html_list)) if 'div id="ingredients_to_shoplist"' in html_list[i]][0]
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
            recipe_data['calories'] = int(float(i.split(":")[1][1:-2]))

    final_tags = []
    for i in range(len(details[:details_end])):
        if "tags" in details[:details_end][i]:
            tags = details[:details_end][i+2:-1]
            for j in (tags):
                final_tags.append(''.join(j.split()))

    recipe_data['tags'] = final_tags
    print(recipe_data)

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
