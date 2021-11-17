import random
from Wolf import *

WolfNames = []


animalCount = {'Wolf': 3}


def initializeAnimals():
    for key in animalCount:
        for i in range(animalCount[key]):
            number = random.randrange(1000000000000)
            globals()['Wolf%s' % number] = Wolf()
            print(globals()['Wolf%s' % number])

initializeAnimals()