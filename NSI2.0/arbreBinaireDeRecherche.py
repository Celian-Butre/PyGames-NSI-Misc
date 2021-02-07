class Arbre :

    def __init__(self, elt, gauche=None, droit=None) :
        self.racine = elt
        self.fils_gauche = gauche
        self.fils_droit = droit

    def est_vide(self) :
        return self.racine == None
    
    def racine(self) :
        return self.racine
    
    def fils_gauche(self) :
        return self.fils_gauche
    
    def fils_droit(self) :
        return self.fils_droit

class ABR(Arbre):
    def testeABR(self):
        if self.fils_gauche == None and self.fils_droit == None:
            return(True)
        if self.fils_droit != None:
            if self.fils_droit.racine < self.racine:
                return(False)
            if self.fils_droit.testeABR() == False:
                return(False)
        if self.fils_gauche != None:
            if self.fils_gauche.racine > self.racine:
                return(False)
            if self.fils_gauche.testeABR() == False:
                return(False)
        return(True)
    
    def rechercheABR(self, recherche):
        if self.racine == recherche:
            return(True)
        if self.fils_gauche == None and self.fils_droit == None and self.racine != recherche:
            return(False)
        if self.racine > recherche and self.fils_gauche == None:
            return(False)
        if self.racine < recherche and self.fils_droit == None:
            return(False)
        if self.racine > recherche:
            return(self.fils_gauche.rechercheABR(recherche))
        if self.racine < recherche:
            return(self.fils_droit.rechercheABR(recherche))
    
    def insertionABR(self, insertion):
        if self.racine > insertion:
            if self.fils_gauche == None:
                self.fils_gauche = ABR(insertion)
                return(True)
            else:
                self.fils_gauche.insertionABR(insertion)
                
        
        if self.racine < insertion:
            if self.fils_droit == None:
                self.fils_droit = ABR(insertion)
                return(True)
            else:
                self.fils_droit.insertionABR(insertion)
            
if __name__ == '__main__':
    
    arbreTotal = ABR(13, ABR(10,ABR(3),ABR(11)),ABR(24,ABR(14),ABR(37,ABR(30),ABR(39))))
    arbreTotalEquilibre = ABR(13, ABR(10,ABR(3),ABR(11)),ABR(24,ABR(14),ABR(37)))
    arbreSchema =  ABR(20,ABR(10,ABR(5),ABR(15)),ABR(30,droit = ABR(40,ABR(35),ABR(45))))
    A = ABR(13, ABR(10, ABR(3, None, None), ABR(11, None, None)), ABR(24, ABR(14, None, None), ABR(37, None, None)))
    feuille = ABR(13)
    feuille2 = ABR(24)
    arbreVrai = ABR(14, feuille, feuille2)
    arbreFaux = ABR(14, feuille2, feuille)
    print(1)
    print(arbreVrai.testeABR())
    print(2)
    print(arbreFaux.testeABR())
    print(3)
    print(arbreTotalEquilibre.testeABR())
    print(4)
    print(A.testeABR())
    print(5)
    print(arbreTotal.testeABR())
    print(arbreTotal.rechercheABR(39))
    print(arbreSchema.testeABR())
    arbreSchema.insertionABR(37)
    print(arbreSchema.testeABR())
    print(7)
    print(arbreSchema.rechercheABR(37))
    print(arbreSchema.fils_droit.fils_droit.fils_gauche.fils_droit.racine)