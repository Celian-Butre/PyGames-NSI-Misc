class PileVide(Exception):
    pass

class Pile():
    def __init__(self, pile = []):
        self.pile = pile
        self.setLength(len(pile))
        
    def isVide(self):
        if self.pile == []:
            return(True)
        else:
            return(False)
        
    def push(self, push):
        self.pile.append(push)
        self.addLength()
        
    def pop(self):
        if self.isVide() == True:
            pass
            #raise PileVide
        else:
            self.subLength()
            pop = self.pile[-1]
            pile = []
            for i in range (self.giveLength()):
                pile.append(self.pile[i])
            self.pile = pile
            return (pop)
            
    def giveLength(self):
        return self.length
    
    def addLength(self):
        self.length += 1
    
    def subLength(self):
        self.length -= 1
    
    def emptyLength(self):
        self.length = 0
        
    def setLength(self, length):
        self.length = length
    
    def top(self):
        return (self.pile[-1])
    
    def videPile(self):
        self.pile = []
        self.emptyLength()
        
    def __str__(self):
        return (str(self.pile))
    