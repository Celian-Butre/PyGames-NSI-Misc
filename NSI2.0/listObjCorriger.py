# DEFINITION DES LISTES ABSTRAITES

class Cellule :
    def __init__(self, tete, queue) :
        self.car = tete
        self.cdr = queue


class Liste :
    def __init__(self, c) :
        self.cellule = c

    def estVide(self) :
        return self.cellule is None

    def car(self) :
        assert not(self.cellule is None), 'Liste vide'
        return self.cellule.car

    def cdr(self) :
        assert not(self.cellule is None), 'Liste vide'
        return self.cellule.cdr


# CONSTRUCTEUR DE LISTE
def cons(tete, queue) :
    return Liste(Cellule(tete, queue))

# LISTE VIDE
Nil = Liste(None)


def listeElements(L) :  # transforme une liste abstraite en une liste python
    t = []
    while ( not(L.estVide()) ) :
        t.append(L.car())
        L = L.cdr()
    return t

def longueurListe(L) :
    # A IMPLEMENTER EN S INSPIRANT DE LA FONCTION listeElements
    pass

def insert(L, what):
    Ladd = cons(what, L1.cdr().cdr().cdr())
    L1.cdr().cdr() = Ladd
    
# QUELQUES TESTS
print("Longueur de la liste vide : ", longueurListe(Nil))
print("Liste des éléments de la liste vide : ", listeElements(Nil))
try :
    print(Nil.cdr())
except AssertionError :
    print("La liste vide n'a ni queue, ni tête.")

L1 = cons(1, cons(2, cons(4, cons(5, Nil))))
insert(L1, 6)
print("Longueur de L1 : ", longueurListe(L1))
print("Liste des éléments de L1 : ", listeElements(L1))
# On peut egalement construire L1 en utilisant des listes deja construites
L5 = cons(5, Nil)
L4 = cons(4, L5)
L1 = cons(1, cons(2, L4))
print("Longueur de L1 : ", longueurListe(L1))
print("Liste des éléments de L1 : ", listeElements(L1))

# COMPRENDRE L AFFICHAGE DES INSTRUCTIONS SUIVANTES
print()
print(L1)
print(L1.car())
print(L1.cdr())
print(L1.cdr().car())
print(L1.cdr().cdr())
print(L1.cdr().cdr().cdr())
print(L1.cdr().cdr().cdr().car())
print()

# INSERTION D UN ELEMENT 3 ENTRE LES ELEMENTS 2 ET 4
# A COMPLETER
# Indication : nommer chacune des cellules, en L2, L3, L4 et changer le pointeur d une cellule

print(listeElements(L1))    # DOIT AFFICHER : [1, 2, 3, 4, 5]

#listes_abstraites_objet_A_COMPLETER.py
#Displaying listes_abstraites_objet_A_COMPLETER.py