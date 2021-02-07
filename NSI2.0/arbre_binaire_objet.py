class Arbre :

    def __init__(self, elt, gauche=None, droit=None) :
        self.racine = elt
        self.fils_gauche = gauche
        self.fils_droit = droit

    def est_vide(self) :
        return self.racine == None

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


# Arbre vide
Nil = Arbre(None, None, None)
print("L'arbre vide est-il vide ?", Nil.est_vide())

A1 = Arbre(1, Arbre(2, Arbre(3, None, None), Arbre(4, None, None)), Arbre(5, Arbre(6, None, None), Arbre(7, None, None)))

print("Taille :", taille(A1))
print("Hauteur :", hauteur(A1))
print("Parcours préfixe :")
afficher_prefixe(A1)
print("Parcours infixe :")
afficher_infixe(A1)
print("Parcours postfixe :")
afficher_postfixe(A1)

# Génération d'un arbre binaire complet de profondeur n
def generer_arbre_complet_recursif(n, valeur_depart = 0) :
    arbre = Arbre(None)
    valeur = valeur_depart
    if ( n == 0 ) :
        return None
    else :
        return Arbre(valeur, generer_arbre_complet_recursif(n-1, valeur+1), generer_arbre_complet_recursif(n-1, valeur+2**(n-1)))


def generer_arbre_complet_iteratif(n) :
    return arbre

print()
A2 = generer_arbre_complet_recursif(5)
afficher_prefixe(A2)


# Parcours en profondeur (ou "depth-first")
def parcours_prefixe(A) :
    liste_elements_gauche = []
    liste_elements_droite = []
    if ( A.fils_gauche != None ) :
        liste_elements_gauche = parcours_prefixe(A.fils_gauche)
    if ( A.fils_droit != None ) :
        liste_elements_droite = parcours_prefixe(A.fils_droit)
    return [A.racine] + liste_elements_gauche + liste_elements_droite

print()
print("Liste des noeuds par parcours préfixe :", parcours_prefixe(A2))

def parcours_infixe(A) :
    liste_elements_gauche = []
    liste_elements_droite = []
    if ( A.fils_gauche != None ) :
        liste_elements_gauche = parcours_infixe(A.fils_gauche)
    if ( A.fils_droit != None ) :
        liste_elements_droite = parcours_infixe(A.fils_droit)
    return liste_elements_gauche + [A.racine] + liste_elements_droite

print()
print("Liste des noeuds par parcours infixe :", parcours_infixe(A2))

def parcours_postfixe(A) :
    liste_elements_gauche = []
    liste_elements_droite = []
    if ( A.fils_gauche != None ) :
        liste_elements_gauche = parcours_postfixe(A.fils_gauche)
    if ( A.fils_droit != None ) :
        liste_elements_droite = parcours_postfixe(A.fils_droit)
    return liste_elements_gauche + liste_elements_droite + [A.racine]

print()
print("Liste des noeuds par parcours postfixe :", parcours_postfixe(A2))

# Parcours en largeur (ou "width-first")
def parcours_largeur(A) :
    file_noeuds = [A]
    liste_elements = []
    while ( file_noeuds != [] ) :
        noeud_courant = file_noeuds.pop(0)
        liste_elements.append(noeud_courant.racine)
        if ( noeud_courant.fils_gauche != None ) :
            file_noeuds.append(noeud_courant.fils_gauche)
        if ( noeud_courant.fils_droit != None ) :
            file_noeuds.append(noeud_courant.fils_droit)
    return liste_elements

# print()
# print("Liste des noeuds par parcours en largeur :", parcours_largeur(A1))

print()
print("Liste des noeuds par parcours en largeur :", parcours_largeur(A2))


