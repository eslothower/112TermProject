#This file is for the Sheep class, which inherits attributes and methods from 
#the Animal class

from Animal import *

class Sheep(Animal):

    def getMutationStatus(self):
        return(f"This is the sheep's mutation status: {self.mutationStatus}")