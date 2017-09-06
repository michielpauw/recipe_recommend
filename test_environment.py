import pickle
import random
import math

with open('recipe_db.pkl', 'rb') as f:
    recipe_db = pickle.load(f)