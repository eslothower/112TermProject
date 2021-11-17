class Animal(object):

    def __init__(self, offspringRate=0, hunger=0, hungerLevel=0, thirst=0, thirstLevel=0, lifespan=0, age=0, mutationRate=0, mutationStatus=False, nutritionalValue=0, speed=0, count=0, positions=[]):
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

    def __repr__(self):
        return("I am an animal object")