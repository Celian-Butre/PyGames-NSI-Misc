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
                return(1+self.right.giveMaxDepth())
            else:
                return(1+self.left.giveMaxDepth())
        return(1+max(self.left.giveMaxDepth(), self.right.giveMaxDepth()))
    
    def prefixPrint(self):
        if ( A == None ) :
            return []
        else :
            return [A.racine] + parcours_prefixe(A.fils_gauche) + parcours_prefixe(A.fils_droit)
        
    def searchElement(self, item):
        if self.giveRoot() == item:
            return(True)
        if self.isLeaf():
            return(False)
        return(self.giveLeft().searchElement(item) or self.giveRight().searchElement(item))
    
    def estComplet(self):
        if self.isLeaf():
            return(True)
        if self.isBranch()[0] == True:
            return(False)
        return(self.giveLeft().estComplet() and self.giveRight().estComplet() and self.giveLeft().giveMaxDepth() == self.giveRight().giveMaxDepth())
    
    def estComplet2(self):
        if self.isLeaf():
            return(True)
        if not((2**self.giveMaxDepth()) - 1 == self.giveLength()):
            return(False)
        elif self.isBranch()[0] == False:
            return(self.giveRight().estComplet2() and self.giveLeft().estComplet2())
        else:
            return(False)

if __name__ == '__main__':
    A = ARBRE(7, ARBRE(31,ARBRE(14),ARBRE(16)), ARBRE(13,ARBRE(41),ARBRE(61)))
    print(A.estComplet2())