import pickle

with open('recipe_db.pkl', 'rb') as f:
    mynewlist = pickle.load(f)

testlist = mynewlist[1000:4000:100]

for test in mynewlist[0:10]:
    print(test)