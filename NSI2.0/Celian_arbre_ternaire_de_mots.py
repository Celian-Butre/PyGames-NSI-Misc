# CLASSE ARBRE TERNAIRE DE DECOMPOSITION IMPARFAITE DE MOTS


# Fonctions auxiliaires de tests de sous-mots
def prefixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un préfixe strict du mot m2
        """
        return ( ( 0 < len(m1) < len(m2) ) and m1 == m2[:len(m1)] )

def infixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un sous-mot strict du mot m2, sans la première et dernière lettre
        """
        return ( ( len(m1) < len(m2) - 1 ) and m1 in m2[1:len(m2)] )

def suffixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un suffixe strict du mot m2
        """
        return ( 0 < len(m1) < len(m2) and m1 == m2[-len(m1):] )


# class Arbre_Ternaire_de_Decompositions_Imparfaites_de_Mots
class ATDIM :

    def __init__(self, elt, gauche=None, milieu=None, droit=None) :
        self.racine = elt
        self.fils_aine = gauche
        self.fils_cadet = milieu
        self.fils_benjamin = droit


    def est_vide(self):
        return self.racine == None
    
    def taille(self):
        if self.fils_aine == None:
            return (1)
        else:
            return (1 + self.fils_aine.taille() + self.fils_benjamin.taille() + self.fils_cadet.taille())
    
    def hauteur(self):
        if self.fils_aine == None:
            return (1)
        else:
            return (1 + max(self.fils_aine.hauteur(), self.fils_benjamin.hauteur(), self.fils_cadet.hauteur()))
    
    def est_ATDIM(self) :
        if self == None or (self.fils_aine == self.fils_cadet == self.fils_benjamin == None ) :    # l'arbre vide ou une feuille est un ATDIM
            return True
        elif ( self.fils_aine == None or self.fils_cadet == None or self.fils_benjamin == None ) :  # un ATDMI doit être complet (une racine doit avoir 0 fils, ou alors tous ses trois fils)
            return False
        else :      # on vérife que les fils vérifient les conditions de sous-mots de la racine du père
            return ( prefixe_strict(self.fils_aine.racine, self.racine) and infixe_strict(self.fils_cadet.racine, self.racine) and suffixe_strict(self.fils_benjamin.racine, self.racine) and self.fils_aine.est_ATDIM() and self.fils_cadet.est_ATDIM() and self.fils_benjamin.est_ATDIM() )

    # Parcours en profondeur (avec type d'ordre en argument optionnel) :
    def parcours_profondeur(self, ordre="préfixe") :    # ordre : préfixe, infixe 1, infixe 2, postfixe
        liste_elements_aine = []
        liste_elements_cadet = []
        liste_elements_benjamin = []
        if ( self.fils_aine != None ) :
            liste_elements_aine = self.fils_aine.parcours_profondeur(ordre)
        if ( self.fils_cadet != None ) :
            liste_elements_cadet = self.fils_cadet.parcours_profondeur(ordre)
        if ( self.fils_benjamin != None ) :
            liste_elements_benjamin = self.fils_benjamin.parcours_profondeur(ordre)
        if ( ordre == "préfixe" ) :
            return [self.racine] + liste_elements_aine + liste_elements_cadet + liste_elements_benjamin
        elif ( ordre == "infixe 1" ) :
            return  liste_elements_aine + [self.racine] + liste_elements_cadet + liste_elements_benjamin
        elif ( ordre == "infixe 2" ) :
            return liste_elements_aine + liste_elements_cadet + [self.racine] + liste_elements_benjamin
        elif ( ordre == "postfixe" ) :
            return liste_elements_aine + liste_elements_cadet + liste_elements_benjamin + [self.racine]


    # Parcours en largeur (ou "width-first")
    def parcours_largeur(self) :
        file_noeuds = [self]
        liste_elements = []
        while ( file_noeuds != [] ) :
            noeud_courant = file_noeuds.pop(0)
            liste_elements.append(noeud_courant.racine)
            if ( noeud_courant.fils_aine != None ) :
                file_noeuds.append(noeud_courant.fils_aine)
            if ( noeud_courant.fils_cadet != None ) :
                file_noeuds.append(noeud_courant.fils_cadet)
            if ( noeud_courant.fils_benjamin != None ) :
                file_noeuds.append(noeud_courant.fils_benjamin)
        return liste_elements


    # Pour l'affichage
    def __str__(self) :
        s = ''
        for i in self.parcours_largeur() :
#        for i in self.parcours_profondeur() :   # argument optionnel : infixe 1, infixe 2, postfixe
            s = s + str(i) + '\n'
        return s


# TESTS

VIDE = ATDIM(None)
assert VIDE.est_ATDIM() == True

ARBRE_FEUILLE = ATDIM ('a')
assert ARBRE_FEUILLE.est_ATDIM() == True

UNE_SEULE_LETTRE_QUI_DEVRAIT_ETRE_UN_ARBRE_FEUILLE = ATDIM ('a', ATDIM('a'), None, None)
assert UNE_SEULE_LETTRE_QUI_DEVRAIT_ETRE_UN_ARBRE_FEUILLE.est_ATDIM() == False

DEUX_LETTRES_OK = ATDIM ('ab', ATDIM('a'), ATDIM(''), ATDIM('b'))
assert DEUX_LETTRES_OK.est_ATDIM() == True

DEUX_LETTRES_KO = ATDIM ('ab', ATDIM('a'), ATDIM(''), ATDIM(''))
assert DEUX_LETTRES_KO.est_ATDIM() == False

A1 = ATDIM('abcde', ATDIM('ab', ATDIM('a'), ATDIM(''), ATDIM('b')), ATDIM('bcd', ATDIM('b'), ATDIM('c'), ATDIM('d')), ATDIM('de', ATDIM('d'), ATDIM(''), ATDIM('e')))
assert A1.est_ATDIM() == True

A2 = ATDIM('Tle_NSI', ATDIM('T'), ATDIM('le_NS', ATDIM('e'), ATDIM('le', ATDIM('l'), ATDIM(''), ATDIM('e')), ATDIM('_NS', ATDIM('_'), ATDIM('N'), ATDIM('S'))), ATDIM('I'))
assert A2.est_ATDIM() == False

print("\nParcours en profondeur (préfixe) :")
print(A1.parcours_profondeur("préfixe"))
print("\nParcours en profondeur (infixe 1) :")
print(A1.parcours_profondeur("infixe 1"))
print("\nParcours en profondeur (infixe 2) :")
print(A1.parcours_profondeur("infixe 2"))
print("\nParcours en profondeur (postfixe) :")
print(A1.parcours_profondeur("postfixe"))
print("\nParcours en largeur :")
print(A1.parcours_largeur())
print("\nListe des étiquettes (en largeur) :")

print(A1)
print("\nEst-ce un arbre ternaire de décompositions imparfaites de mots ?", A1.est_ATDIM())

print("\n\nUn autre arbre ternaire : ")
print("\nParcours en profondeur:")
print(A2.parcours_profondeur())
print("\nParcours en largeur :")
print(A2.parcours_largeur())
print("\nEst-ce un arbre ternaire de décompositions imparfaites de mots ?", A2.est_ATDIM())

print("largeur A2 ", A2.taille())
print("hauteur A1 ", A1.hauteur())