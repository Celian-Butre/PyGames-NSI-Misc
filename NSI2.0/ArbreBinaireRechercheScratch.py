class ABR:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
        
    def rechercheABR(self, recherche):
        if self.item == recherche:
            return(True)
        if self.item > recherche and self.left != None:
            return(self.left.rechercheABR(recherche))
        if self.item < recherche and self.right != None:
            return(self.right.rechercheABR(recherche))       
        return(False)
    
    def insertionABR(self, insertion, recherche = True):
        if recherche == True:
            if self.rechercheABR(insertion) == True:
                print("il ne faut pas mettre un objet deja dans l'arbre")
                return(None)
            recherche = False
        if self.item > insertion:
            if self.left == None:
                self.left = ABR(insertion)
            else:
                self.left.insertionABR(insertion, False)
        else:
            if self.right == None:
                self.right = ABR(insertion)
            else:
                self.right.insertionABR(insertion, False)
    
if __name__ == '__main__':
    arbre = ABR(17,ABR(10,ABR(5),ABR(11)),ABR(24,ABR(18),ABR(29,ABR(25))))
    
    #tests recherche all true
    print('True from now on')
    print(arbre.rechercheABR(17))
    print(arbre.rechercheABR(10))
    print(arbre.rechercheABR(5))
    print(arbre.rechercheABR(11))
    print(arbre.rechercheABR(24))
    print(arbre.rechercheABR(18))
    print(arbre.rechercheABR(29))
    print(arbre.rechercheABR(25))
    
    #tests recherche all False
    print('False from now on')
    print(arbre.rechercheABR(4))
    print(arbre.rechercheABR(6))
    print(arbre.rechercheABR(12))
    print(arbre.rechercheABR(19))
    print(arbre.rechercheABR(30))
    print(arbre.rechercheABR(26))
    
    #test insertion all True
    print('True from now on')
    arbre.insertionABR(4)
    print(arbre.rechercheABR(4))
    arbre.insertionABR(6)
    print(arbre.rechercheABR(6))
    arbre.insertionABR(12)
    print(arbre.rechercheABR(12))
    arbre.insertionABR(19)
    print(arbre.rechercheABR(19))
    arbre.insertionABR(30)
    print(arbre.rechercheABR(30))
    arbre.insertionABR(26)
    print(arbre.rechercheABR(26))
    
    #test exception insertion all exception
    print('8 exceptions from now on')
    arbre.insertionABR(17)
    arbre.insertionABR(10)
    arbre.insertionABR(5)
    arbre.insertionABR(11)
    arbre.insertionABR(24)
    arbre.insertionABR(18)
    arbre.insertionABR(29)
    arbre.insertionABR(25)