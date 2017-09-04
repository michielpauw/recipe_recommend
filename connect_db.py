from pymongo import MongoClient
client = MongoClient()

db = client.recipe_recommend
recipes = db.recipes