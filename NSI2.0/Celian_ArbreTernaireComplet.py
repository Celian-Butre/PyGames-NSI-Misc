# CLASSE ARBRE TERNAIRE DE DECOMPOSITION IMPARFAITE DE MOTS


# Fonctions auxiliaires de tests de sous-mots
def prefixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un préfixe strict du mot m2
        """
        return(m2[:len(m1)] == m1 and len(m1) < len(m2) and len(m1) != 0)

def infixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un sous-mot strict du mot m2, sans la première et dernière lettre
        """
        return(m1 in m2[1:-1])

def suffixe_strict(m1, m2) :
        """
        Retourne True si le mot m1 est un suffixe strict du mot m2
        """
        return(m2[len(m2) - len(m1):] == m1 and len(m1) < len(m2) and len(m1) != 0)

class ATDIM :

    def __init__(self, elt, gauche=None, milieu=None, droit=None) :
        self.racine = elt
        self.fils_aine = gauche
        self.fils_cadet = milieu
        self.fils_benjamin = droit


    def parcours_profondeur(self,l_elements):
        """
        nécessite 1 liste vide en entrée
        """
        l_elements += [self.racine]
        if (self.fils_aine != None) :
            self.fils_aine.parcours_profondeur(l_elements)
        if (self.fils_cadet != None) :
            self.fils_cadet.parcours_profondeur(l_elements)
        if (self.fils_benjamin != None) :
            self.fils_benjamin.parcours_profondeur(l_elements)
        return l_elements

    def parcours_largeur(self,l_elements, elements_traitable) :
        """
        nécessite 2 liste vide en entrée
        """
        if elements_traitable == []:
            elements_traitable.append(self)
        if self.fils_aine != None:
            elements_traitable.append(self.fils_aine)
        if self.fils_cadet != None:    
            elements_traitable.append(self.fils_cadet)
        if self.fils_benjamin != None:    
            elements_traitable.append(self.fils_benjamin)
        l_elements.append(elements_traitable.pop(0).racine)
        if elements_traitable != []:
            elements_traitable[0].parcours_largeur(l_elements, elements_traitable)
        return l_elements


    def est_ATDIM(self) :
        """
        on suppose que l'arbre est complet 3 branches sur chaque branche
        """ 
        if self.fils_aine == None and self.fils_cadet == None and self.fils_benjamin == None:
            return(True)
        if (self.fils_aine != None and self.fils_cadet != None and self.fils_benjamin != None):
            return(self.fils_aine.est_ATDIM() and self.fils_cadet.est_ATDIM() and self.fils_benjamin.est_ATDIM() and prefixe_strict(self.fils_aine.racine, self.racine) and infixe_strict(self.fils_cadet.racine, self.racine) and suffixe_strict(self.fils_benjamin.racine, self.racine))
        return(False)

# TESTS
A2 = ATDIM('Tle_NSI', ATDIM('T'), ATDIM('le_NS', ATDIM('e'), ATDIM('le', ATDIM('l'), ATDIM(''), ATDIM('e')), ATDIM('_NS', ATDIM('_'), ATDIM('N'), ATDIM('S'))), ATDIM('I'))

print("\n\nUn autre arbre ternaire : ")
print("\nParcours en profondeur:")
print(A2.parcours_profondeur([]))
print("\nParcours en largeur :")
print(A2.parcours_largeur([],[]))
print("\nEst-ce un arbre ternaire de décompositions imparfaites de mots ?", A2.est_ATDIM())

A3 = ATDIM('Tle_NSI', ATDIM('T'), ATDIM('le_NS', ATDIM('le', ATDIM('l'), ATDIM(''), ATDIM('e')), ATDIM('e'), ATDIM('_NS', ATDIM('_'), ATDIM('N'), ATDIM('S'))), ATDIM('I'))

print("\n\nUn autre arbre ternaire : ")
print("\nParcours en profondeur:")
print(A3.parcours_profondeur([]))
print("\nParcours en largeur :")
print(A3.parcours_largeur([],[]))
print("\nEst-ce un arbre ternaire de décompositions imparfaites de mots ?", A3.est_ATDIM())

A1 = ATDIM('abcde', ATDIM('ab', ATDIM('a'), ATDIM(''), ATDIM('b')), ATDIM('bcd', ATDIM('b'), ATDIM('c'), ATDIM('d')), ATDIM('de', ATDIM('d'), ATDIM(''), ATDIM('e')))

print("\nParcours en profondeur:")
print(A1.parcours_profondeur([]))
print("\nParcours en largeur :")
print(A1.parcours_largeur([],[]))
print("\nEst-ce un arbre ternaire de décompositions imparfaites de mots ?", A1.est_ATDIM())




if __name__ == '__main__':
    print('HERE BEGINS CUSTOM TESTS')
    print('-------------------------------------------------------------')
    print('prefixe_strict')
    print(True, prefixe_strict('1234', '1234675'))
    print(False, prefixe_strict('1234675342', '1234675'))
    print(False, prefixe_strict('12342', '1234675'))
    print(True, prefixe_strict('', 'a'))
    print('')
    print('suffixe_strict')
    print(True, suffixe_strict('1234', '01234'))
    print(False, suffixe_strict('1234', '1234'))
    print(False, suffixe_strict('00001234', '1234'))
    print(False, suffixe_strict('1234', '0122334'))
    print(True, suffixe_strict('', 'a'))
    print('')
    print('infixe_strict')
    print(True, infixe_strict('', '01234'))
    print(True, infixe_strict('123', '01234'))
    print(False, infixe_strict('1234', '1234'))
    print(False, infixe_strict('00001234', '1234'))
    print(False, infixe_strict('01234', '1234'))
    print(False, infixe_strict('1234', '1234123'))
    print(True, infixe_strict('', 'a'))
    print(True, infixe_strict('', 'a2')) 
    
    
    
    
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