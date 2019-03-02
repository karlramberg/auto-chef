# karl ramberg, paul ramberg, trenton morgan
# pickhacks 2019 - 3/1/19

class Food:
    def __init__(self, name, category, weight, probability):
        self.name = name
        self.category = category
        self.weight = weight
        self.probability = probability

    def changeWeight(self, newWeight):
        self.weight = newWeight
