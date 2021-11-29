#This file is for the Animal class, which which is the parent class for the 
#Wolf and Sheep class (and all other animal classes to follow)

import random

class Animal(object):

    #default values for each animal type
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

        #Random chance for mutation
        if random.randrange(0,3) == random.randrange(0,3):

            self.mutationStatus = True

    def getOffspringCounter(self):
        return self.offspringCounter

    def getOffspringRate(self):
        return self.offspringRate

    def addOneToOffspringCounter(self):
        self.offspringCounter += 1

    def resetOffspringCounter(self):
        self.offspringCounter = 0

    



