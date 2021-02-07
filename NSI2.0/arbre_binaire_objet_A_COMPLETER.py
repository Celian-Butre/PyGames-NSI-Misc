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

def taille(A) :
    if ( A == None ) :
        return 0
    else :
        return 1 + taille(A.fils_gauche) + taille(A.fils_droit)


def hauteur(A) :
    if ( A == None ) :
        return 0
    else :
        return 1 + max(hauteur(A.fils_gauche), hauteur(A.fils_droit))


def afficher_prefixe(A) :
    print(A.racine)
    if ( A.fils_gauche != None ) :
        afficher_prefixe(A.fils_gauche)
    if ( A.fils_droit != None ) :
        afficher_prefixe(A.fils_droit)

def afficher_infixe(A) :
    if ( A.fils_gauche != None ) :
        afficher_infixe(A.fils_gauche)
    print(A.racine)
    if ( A.fils_droit != None ) :
        afficher_infixe(A.fils_droit)

def afficher_postfixe(A) :
    if ( A.fils_gauche != None ) :
        afficher_postfixe(A.fils_gauche)
    if ( A.fils_droit != None ) :
        afficher_postfixe(A.fils_droit)
    print(A.racine)

A = Arbre(1, Arbre(2, Arbre(3, None, None), Arbre(4, None, None)), Arbre(5, Arbre(6, None, None), Arbre(7, None, None)))

# Arbre vide
Nil = Arbre(None, None, None)
print("Est-ce que l'arbreb vide est vide ?", Nil.est_vide())

#A = Arbre(1, Arbre(2, Arbre(3, None), None)

print("Taille :", taille(A))
print("Hauteur :", hauteur(A))
print("Parcours préfixe :")
afficher_prefixe(A)
print("Parcours infixe :")
afficher_infixe(A)
print("Parcours postfixe :")
afficher_postfixe(A)


# Parcours en profondeur (ou "depth-first")
def parcours_prefixe(A) :
    if ( A == None ) :
        return []
    else :
        return [A.racine] + parcours_prefixe(A.fils_gauche) + parcours_prefixe(A.fils_droit)

def parcours_infixe(A) :
    if ( A == None ) :
        return []
    else :
        return parcours_infixe(A.fils_gauche) + [A.racine] + parcours_infixe(A.fils_droit)

def parcours_postfixe(A) :
    if ( A == None ) :
        return []
    else :
        return parcours_postfixe(A.fils_gauche) + parcours_postfixe(A.fils_droit) + [A.racine]

# Parcours en largeur (ou "width-first")
def parcours_largeur(tree1, liste = [], liste2 = []):
    if liste == []:
        liste.append(tree1)
    if tree1.fils_gauche != None:
        liste.append(tree1.fils_gauche)
    if tree1.fils_droit != None:    
        liste.append(tree1.fils_droit)
    liste2.append(liste.pop(0).racine)
    if liste != []:
        parcours_largeur(liste[0], liste, liste2)
    
    return (liste2)

arbreVide = None

# Génération d'un arbre binaire complet de hauteur n
def generer_arbre_complet(level) :
    treeMatrix = []
    treeMatrix.append([])
    for i in range(2**level):
        treeMatrix[0].append(arbreVide)
    for i in range(level):
        numberOfTreesInLevel = 2**(level-i-1)
        firstNumberOnLevel = 2**(level-i-1) - 1
        treeMatrix.append([])
        for j in range(numberOfTreesInLevel):
            treeMatrix[i+1].append(Arbre(firstNumberOnLevel + j, treeMatrix[i][j*2], treeMatrix[i][j*2+1]))
    return(treeMatrix[-1][-1])

# TESTS : a faire
if __name__ == '__main__':

    a = generer_arbre_complet(8)
    print(parcours_prefixe(A))
    print(parcours_infixe(A))
    print(parcours_postfixe(A))
    print(parcours_largeur(a))