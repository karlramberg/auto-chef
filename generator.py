# karl ramberg, paul ramberg, trenton morgan, isaih slater
# pickhacks 2019 - 3/1/19
import json
import random
from Food import Food
from pprint import PrettyPrinter
pp = PrettyPrinter()

diet = []

def getTokens(path):
    return open(path).read().splitlines()

def generateJsonFile():

    for x in range(5):
        if x == 0:
            filename = "meats.txt"
        elif x == 1:
            filename = "carbs.txt"
        elif x == 2:
            filename = "vegetables.txt"
        elif x == 3:
            filename = "fruits.txt"
        else:
            filename = "spices.txt"

        tokens = getTokens("food/" + filename)

        for token in tokens:
            if x == 0:
                weight = 0.6
                category = "meats"
                probability = 0.05
            elif x == 1:
                weight = 0.4
                category = "carbs"
                probability = 0.05
            elif x == 2:
                weight = 0.15
                category = "vegetables"
                probability = 0.05
            elif x == 3:
                weight = 0.15
                category = "fruits"
                probability = 0.05
            else:
                weight = 0.05
                category = "spices"
                probability = 0.05

            diet.append(Food(token, category, weight, probability))

    json_file = open("diet.json", "w")
    json_file.write(json.dumps([ob.__dict__ for ob in diet], indent = 4))

def newRecipe():
    recipe = []
    for x in range(4):
        index = random.randint(0, len(diet)-1)
        recipe.append(diet[index])

    print(json.dumps([ob.__dict__ for ob in recipe]))
    return json.dumps([ob.__dict__ for ob in recipe])

if __name__ == '__main__':
    generateJsonFile()
