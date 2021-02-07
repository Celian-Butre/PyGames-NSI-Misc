import random

class Personnage :

    def __init__(self, nom, nbreDeVie, force, protection) :   # EN-TETE DE FONCTION A MODIFIER
        self.vie = nbreDeVie
        self.nom = nom
        self.force = force
        self.protection = protection
        # A COMPLETER

    def donneEtat (self) :
        return self.vie
    
    def perdVie (self, nbPoints) :
        # A COMPLETER (et supprimer pass)
        self.vie -= nbPoints
        
    def decrire(self) :
        # EXEMPLE D UTILISATION DU FORMATTAGE .format
        print("Le personnage {} a {} points de vie. Il a une force de {} et une protection de {}.".format(self.nom, self.vie, self.force, self.protection))

    def attaque(self) :
        # A COMPLETER (et supprimer pass)
        return (random.randint(1, self.force))

    def defense(self) :
        # A COMPLETER (et supprimer pass)
        return (random.randint(1, self.protection))

def fight(p1, p2) :
    """Le joueur 1 attaque, avec un nombre aléatoire entier entre 1 et sa force ; le joueur 2 perd des points de vie correspondant à l'attaque moins un nombre aléatoire entier entre 0 et la valeur de son protection.
  Si le joueur a obtenu plus de points de défense que le joueur n'a obtenu de points d'attaque, il ne se passe rien : le joueur 2 ne perd ni ne gagne de points de vie (on peut utiliser la fonction max, déjà implémentée en Python, pour s'assurer que si le joueur obtient plus en défense qu'en qu'attaque, il ne perd ni ne gagne de points de vie).
  Puis c 'est le tour du joueur 2 d'attaquer et du joueur 1 de se défendre.
  Le combat continue jusqu'à ce que l'un des joueurs soit à 0 points de vie.
    """
    while p1.donneEtat() > 0 and p2.donneEtat() > 0:
        attaque = p1.attaque()
        defense = p2.defense()
        if attaque > defense:
            p2.perdVie(attaque-defense)
        
        
        attaque = p2.attaque()
        defense = p1.defense()
        if attaque > defense:
            p1.perdVie(attaque-defense)
    
    # A COMPLETER
    if p2.donneEtat()<=0 and p1.donneEtat()>0 :
        msg = f"{p1.nom} est vainqueur, il lui reste encore {p1.donneEtat()} points alors que {p2.nom} est mort."
    elif p1.donneEtat()<=0 and p2.donneEtat()>0 :
        msg = f"{p2.nom} est vainqueur, il lui reste encore {p2.donneEtat()} points alors que {p1.nom} est mort."
    else :
        msg = "Les deux combattants sont morts en même temps."
    return msg


if __name__ == '__main__' :
    # LA CONDITION __name__=='__main__' PERMET D'EXECUTER LES INSTRUCTIONS SUIVANTES UNIQUEMENT SI CE FICHIER EST APPELE EN TANT QUE FICHIER PRINCIPAL (main)
    # LES TESTS CI-DESSOUS NE SONT PAS EXECUTES LORSQUE CE FICHIER EST IMPORTE EN TANT QUE MODULE DANS UN AUTRE FICHIER


    # Chaque personnage possède un nom, un nombre de points de vie, une force, et une protection
    bilbo = Personnage("Bilbo", 20, 7, 6)
    gollum = Personnage("Gollum", 25, 10, 5)

    bilbo.decrire()
    gollum.decrire()

    print(fight(bilbo, gollum))
    
    # A COMPLETER  : CREER DEUX AUTRES PERSONNAGES ET UNE NOUVELLE BATAILLE EPIQUE

    # A COMPLETER SI LE TEMPS LE PERMET :
    # - RAJOUTER UN ATTRIBUT AU CHOIX (un facteur chance, magique, une arme, etc) AUX OBJETS DE TYPE PERSONNAGE
    # - RAJOUTER UNE METHODE AU CHOIX AUX OBJETS DE TYPE PERSONNAGE