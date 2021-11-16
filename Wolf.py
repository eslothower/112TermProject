from Animal import *
import random

class Wolf(Animal):

    def __init__(self):

        self.offspringRate = 10 #wolf/cycle
        #self.hunger = 
        
        if random.randrange(0,11) == random.randrange(0,11):

            self.mutationStatus = True