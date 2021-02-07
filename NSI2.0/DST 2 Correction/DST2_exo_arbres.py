# DST2 : exo arbre binaire

class AB :
    def __init__(self,r , g = None, d = None) : # objet AB : arbre binaire
        self.racine = r
        self.fils_gauche = g
        self.fils_droit = d


def parcours_prefixe(A) :
    print(A.racine, end=" " )
    if not(A.fils_gauche == None) :
        parcours_prefixe(A.fils_gauche)
    if not(A.fils_droit == None) :
        parcours_prefixe(A.fils_droit)

def parcours_largeur(A) :
    file_noeuds = [A]       # file de noeuds à traiter
    liste_elements = []
    while ( file_noeuds != [] ) :
        noeud_courant = file_noeuds.pop(0)
        print(noeud_courant.racine, end=" ")
        liste_elements.append(noeud_courant.racine)
        if ( noeud_courant.fils_gauche != None ) :
            file_noeuds.append(noeud_courant.fils_gauche)
        if ( noeud_courant.fils_droit != None ) :
            file_noeuds.append(noeud_courant.fils_droit)
    print()
    return liste_elements   # pas utilisé ici

def taille(A) :
    if A == None:
        return 0
    else :
        return 1 + taille(A.fils_gauche) + taille(A.fils_droit)


def hauteur(A) :
    if A == None:
        return 0
    else :
        return 1 + max(hauteur(A.fils_gauche), hauteur(A.fils_droit))


def est_complet(A) :
    if A == None :
        return True
    else :
        return est_complet(A.fils_gauche) and est_complet(A.fils_droit) and hauteur(A.fils_gauche) == hauteur(A.fils_droit)


def est_complet_bis(A) :
    if 2**hauteur(A) - 1 == taille(A) :
        return True
    else :
        return False

# Arbres du DST2
A_DST2_enonce =  AB('A', AB('B', AB('D'), AB('E', AB('H'), AB('I'))), AB('C', AB('F'), AB('G', AB('J'))))
A_DST2_complet_3_niveaux = AB(1, AB(2, AB(4), AB(5)), AB(3, AB(6), AB(7)))

# Autres arbres
A_pas_complet = AB('A', AB('B', AB('D'), AB('E')), AB('C'))
A_complet = AB('A', AB('B', AB('D'), AB('E')), AB('C', AB('F'), AB('G')))

print("\nTests sur les arbres du DST 2 : \n")

print("Parcours en largeur de l'arbre de l'énoncé : ", end="")
parcours_largeur(A_DST2_enonce)
print("Parcours en profondeur préfixe de l'arbre de l'énoncé : ", end="")
parcours_prefixe(A_DST2_enonce)
print()
print("Est-il complet (version récursive Q5)iii)) ?", est_complet(A_DST2_enonce))
print("Est-il complet (version récursion cachée Q5)iv)) ?", est_complet_bis(A_DST2_enonce))

print()
print("Parcours en largeur d'un arbre binaire complet à 3 niveaux : ", end="")
parcours_largeur(A_DST2_complet_3_niveaux)
print("Parcours en profondeur d'un arbre binaire complet à 3 niveaux: ", end="")
parcours_prefixe(A_DST2_complet_3_niveaux)
print()
print("Est-il complet (version récursive Q5)iii)) ?", est_complet(A_DST2_complet_3_niveaux))
print("Est-il complet (version récursion cachée Q5)iv)) ?", est_complet_bis(A_DST2_complet_3_niveaux))


print("\n\nTests sur d'autres arbres : \n")

print("Parcours en largeur : ", end="")
parcours_largeur(A_pas_complet)
print("Parcours en profondeur préfixe : ", end="")
parcours_prefixe(A_pas_complet)
print()
print("Est-il complet (version récursive Q5)iii)) ?", est_complet(A_pas_complet))
print("Est-il complet (version récursion cachée Q5)iv)) ?", est_complet_bis(A_pas_complet))

print()
print("Parcours en largeur : ", end="")
parcours_largeur(A_complet)
print("Parcours en profondeur préfixe : ", end="")
parcours_prefixe(A_complet)
print()
print("Est-il complet (version récursive Q5)iii)) ?", est_complet(A_complet))
print("Est-il complet (version récursion cachée Q5)iv)) ?", est_complet_bis(A_complet))

