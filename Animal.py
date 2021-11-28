import random

class Animal(object):

    def __init__(self, offspringRate=0, hunger=0, hungerLevel=0, thirst=0, thirstLevel=0, lifespan=0, age=0, mutationRate=0, mutationStatus=None, nutritionalValue=0, speed=0, offspringCounter=0):
        self.offspringRate = offspringRate
        self.hunger = hunger
        self.hungerLevel = hungerLevel
        self.thirst = thirst
        self.thirstLevel = thirstLevel
        self.lifespan = lifespan
        self.age = age
        self.mutationRate = mutationRate
        self.mutationStatus = mutationStatus 
        self.nutritionalValue = nutritionalValue
        self.speed = speed
        self.offspringCounter = offspringCounter


        if random.randrange(0,3) == random.randrange(0,3):

            self.mutationStatus = True

    def __repr__(self):
        return("I am an animal object")

    def getOffspringCounter(self):
        return self.offspringCounter

    def getOffspringRate(self):
        return self.offspringRate

    def addOneToOffspringCounter(self):
        self.offspringCounter += 1

    def resetOffspringCounter(self):
        self.offspringCounter = 0

    



