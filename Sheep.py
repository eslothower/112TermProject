from Animal import *

class Sheep(Animal):

    def getMutationStatus(self):
        return(f"This is the sheep's mutation status: {self.mutationStatus}")