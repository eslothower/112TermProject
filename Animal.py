class Animal(object):

    def __init__(self):
        self.offspringRate = 0
        self.hunger = 0
        self.hungerLevel = 0
        self.thirst = 0
        self.thirstLevel = 0
        self.lifespan = 0
        self.age = 0
        self.mutationRate = 0
        self.mutationStatus = False 
        self.nutritionalValue = 0
        self.speed = 0

    def __repr__(self):
        return("I am an animal object")