from Animal import *

class Wolf(Animal):

    def __repr__(self):        
        return(f'I am a wolf and my offspring rate is {self.offspringRate}')

    def getMutationStatus(self):
        return(f"This is the wolf's mutation status {self.mutationStatus}")
    
