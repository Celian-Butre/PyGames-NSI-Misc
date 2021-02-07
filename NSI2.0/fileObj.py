from pileObj import *

class File():
    
    def __init__(self, file = []):
        self.file1 = Pile(file)
        self.file2 = Pile()
        
    def isVide(self):
        if self.file1.isVide() == True and self.file2.isVide() == True:
            return(True)
        else:
            return(False)
            
    def push(self, push):
        self.file2.push(push)
        
    def switch(self):
        for i in range(self.file2.giveLength()):
            pop = self.file2.pop()
            self.file1.push(pop)
            
    def pop(self):
        if self.file1.isVide() == True:
            if self.file2.isVide() == False:
                self.switch()
                return (self.pop())
            else:
                pass
                #raise PileVide
        else:
            pop = self.file1.pop()
            return (pop)
            
    def giveLength(self):
        return (self.file1.giveLength() + self.file2.giveLength())
    
    def top(self):
        if self.file1.giveLength() == 0:
            self.switch()
        return (self.file1.top())
    
    def videPile(self):
        self.file1.videPile()
        self.file2.videPile()
        
    def __str__(self):
        return str(str(self.file2)+ str(self.file1))