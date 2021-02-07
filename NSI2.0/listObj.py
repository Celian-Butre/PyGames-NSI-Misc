listeVide = None

class Cellule:
    def __init__(self, car, cdr):
        self.car = car
        self.cdr = cdr
    
    def __str__(self):
        if self.cdr != None:
            return str(str(self.car) + str(self.cdr))
        else:
            return str(self.car)

class Liste:
    def __init__(self, add, liste = listeVide):
        if liste == listeVide:
            self.length = 0
        else:
            self.length = liste.length
        self.length += 1
        self.liste = Cellule(add, liste)
        
    def __str__(self, a = ' --> '):
        if self.length != 0:
            a += str(str(self.giveListe()))
        return(a)
    
    def giveListe(self):
        return(self.liste)
        
def constructeur(car, liste):
    liste = Liste(car, liste)
    return (liste)
    
liste = constructeur(5, listeVide) 
liste = constructeur(6, liste)
liste = constructeur(7, liste)
print(liste)