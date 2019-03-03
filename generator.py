# karl ramberg, paul ramberg, trenton morgan, isaih slater
# pickhacks 2019 - 3/1/19
import json
import random
import itertools
from Food import Food
from pprint import PrettyPrinter
pp = PrettyPrinter()

diet = []
pairs = []

def getTokens(path):
    return open(path).read().splitlines()

def setDiet():

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
                weight = 0.35
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

    return diet

def newRecipe():
    recipe = []
    totalWeight = 0.0
    while totalWeight < 1.0 or len(recipe) < 3:
        foodIndex = random.randint(0, len(diet)-1)
        if(diet[foodIndex].probability > random.uniform(0.0, 1.0)):
            recipe.append(diet[foodIndex])
            totalWeight += diet[foodIndex].weight

    return json.dumps([ob.__dict__ for ob in recipe])

def addPairs(ingredients):
    names = []
    for ingredient in ingredients:
        names.append(ingredient["name"])
    pairs.append(list(itertools.combinations(names, 2)))
    print(pairs)

if __name__ == '__main__':
    generateJsonFile()
