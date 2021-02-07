class ARBRE:
    def __init__(self, root, left = None, right = None):#element, fils gauche, fils droit
        self.root = root
        self.left = left
        self.right = right
        
    def giveRoot(self):
        return(self.root)
    
    def giveLeft(self):
        return(self.left)
    
    def giveRight(self):
        return(self.right)
    
    def isLeaf(self):
        return(self.left == None and self.right == None)
    
    def isBranch(self): #returns if it is a branch and if so which side is the branch on
        if self.isLeaf() == True or (self.left != None and self.right != None):
            return(False, None)
        if self.left == None:
            return(True, 'right')
        return(True, 'left')
    
    def giveLength(self):
        if self.isLeaf():
            return(1)
        if self.isBranch()[0]:
            if self.isBranch()[1] == 'right':
                return(1+self.right.giveLength())
            else:
                return(1+self.left.giveLength())
        return(1+self.left.giveLength()+self.right.giveLength())
    
    def printKnot(self):
        if self.left == None:
            left = None
        else:
            left = self.left.root
        if self.right == None:
            right = None
        else:
            right = self.right.root
        return(str(self.root)+ ' : '+ str(left)+ ' ; '+ str(right))
    
    def giveMaxDepth(self):
        if self.isLeaf():
            return(1)
        if self.isBranch()[0]:
            if self.isBranch()[1] == 'right':
                return(1+self.right.giveLength())
            else:
                return(1+self.left.giveLength())
        return(1+max(self.left.giveLength()+self.right.giveLength()))
    
    def prefixPrint(self,A):
        if ( A == None ) :
            return []
        else :
            return [A.giveRoot()] + self.prefixPrint(A.giveLeft()) + self.prefixPrint(A.giveRight())
        
    def isItemIn(self,A, item):
        return(item in self.prefixPrint(A))
            
if __name__ == '__main__':
    A = ARBRE(31,ARBRE(14),ARBRE(16))
    print(A.printKnot())
    print(A.giveRight().giveRoot())