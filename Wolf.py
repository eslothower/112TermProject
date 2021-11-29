#This file is for the Wolf class, which inherits attributes and methods from 
#the Animal class

from Animal import *

class Wolf(Animal):

    def getMutationStatus(self):
        return(f"This is the wolf's mutation status {self.mutationStatus}")
    
