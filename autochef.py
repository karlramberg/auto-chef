# karl ramberg, paul ramberg, trenton morgan
# pickhacks 2019 - 3/1/19
def getFood(path):
    return open(path).read().splitlines()

meats = getFood("food/meats.txt")
carbs = getFood("food/carbs.txt")
vegetables = getFood("food/vegetables.txt")
fruits = getFood("food/fruits.txt")
spices = getFood("food/spices.txt")

print(meats)
print(carbs)
print(vegetables)
print(fruits)
print(spices)



