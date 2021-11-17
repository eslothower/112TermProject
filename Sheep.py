from Animal import *

class Sheep(Animal):

    def __repr__(self):
        return(f'I am a sheep and my offspring rate is {self.offspringRate}')