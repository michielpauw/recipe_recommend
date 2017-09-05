import pickle

with open('recipe_db.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

for i in mynewlist:
    print(i)
