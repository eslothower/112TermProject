#This file is for the Animal class, which which is the parent class for the 
#Wolf and Sheep class (and all other animal classes to follow)

import random

class Animal(object):

    #default values for each animal type
    def __init__(self, offspringRate=0, health=0, hungerLevel=0, thirstLevel=0, lifespan=0, age=0, mutation=0, mutationStatus=None, nutritionalValue=0, speed=0, offspringCounter=0):
        self.offspringRate = offspringRate
        self.health = health
        self.hungerLevel = hungerLevel
        self.thirstLevel = thirstLevel
        self.lifespan = lifespan
        self.age = age
        self.mutation = mutation
        self.mutationStatus = mutationStatus 
        self.nutritionalValue = nutritionalValue
        self.speed = speed
        self.offspringCounter = offspringCounter

        #Random chance for mutation
        if random.randrange(0,3) == random.randrange(0,3):

            self.mutationStatus = True

            self.mutation = random.randrange(1,2)

    def getOffspringCounter(self):
        return self.offspringCounter

    def getOffspringRate(self):
        return self.offspringRate

    def addOneToOffspringCounter(self):
        self.offspringCounter += 1

    def resetOffspringCounter(self):
        self.offspringCounter = 0

    def getMutationType(self):
        return self.mutation

    def getCurrentHealth(self):
        return self.health

    def getCurrentHungerLevel(self):
        return self.hungerLevel

    def getHungrier(self):
        self.hungerLevel += 5

    def loseHealth(self):
        self.health -= 10

    def eatSheep(self):
        if self.hungerLevel - 50 < 0:
            self.hungerLevel = 0
        else:
            self.hungerLevel -= 50

    def eatGrass(self):
        if self.hungerLevel - 4 < 0:
            self.hungerLevel = 0
        else:
            self.hungerLevel -= 4

    



