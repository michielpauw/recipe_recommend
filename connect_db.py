from pymongo import MongoClient
client = MongoClient()
import pickle

db = client.recipe_recommend

# create collections
recipes = db.recipes
users = db.users

with open('recipe_db.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

for test in mynewlist[0:10]:
    recipes.insert_one(test)

user = {"first_name": "Michiel",
        "last_name": "Pauw",
        "email": "pauw.michiel@gmail.com",
        "recipes_rec": set(),
        "recipes_made": dict()}