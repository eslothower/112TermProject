from cmu_112_graphics import *
from Animal import *
import random

class Wolf(Animal):

    def __init__(self):

        if random.randrange(0,11) == random.randrange(0,11):

            self.mutationStatus = True

    def __repr__(self):
        
        return(f'I am a wolf and my offspring rate is {self.offspringRate}')