from cmu_112_graphics import *
from Animal import *
import random

class Wolf(Animal):

    # def __init__(self, offspringRate=10, hunger=0, hungerLevel=0, thirst=0, thirstLevel=0, lifespan=0, age=0, mutationRate=0, mutationStatus=False, nutritionalValue=0, speed=0, count=0, positions=[]):

    #     self.offspringRate = 10 #wolf/cycle
    #     self.count = 3
    #     self.imagePath = 'assets/Modified/black_wolf.png'

        
    #     if random.randrange(0,11) == random.randrange(0,11):

    #         self.mutationStatus = True

    def __repr__(self):
        return(f'I am a wolf and my offspring rate is {self.offspringRate}')