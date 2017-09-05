import pickle
import random
import math

with open('recipe_db.pkl', 'rb') as f:
    recipe_db = pickle.load(f)



# times= []
# for i in recipe_db:
#     times.append(i['time'])
#
#
# print((sorted(times, reverse=True)))

# delete items with 0 calories
# count = 0
# _recipe_db = []
# for i in range(len(recipe_db)):
#     if recipe_db[i]['calories'] != 0:
#         _recipe_db.append(recipe_db[i])
# recipe_db = _recipe_db
#
# with open('recipe_db.pkl', 'wb') as f:
#     pickle.dump(recipe_db, f)

# for i in range(len(recipe_db)):
#     for j in range(len(recipe_db[i]['ingredients'])):
#         recipe_db[i]['ingredients'][j] = recipe_db[i]['ingredients'][j]['description']
#
# print(len(recipe_db))
# print(recipe_db[6]['ingredients'])
#
# with open('recipe_db.pkl', 'wb') as f:
#     pickle.dump(recipe_db, f)

# ingredients
# qualities
# calories check
# tags check
