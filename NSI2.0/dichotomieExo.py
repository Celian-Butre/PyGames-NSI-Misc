import random

l = []
for i in range(1000000) :
    l.append(random.randint(0,100))

def dichotomie (l, x) :
    try : 
        assert l == sorted(l), "Le premier argument doit être une liste triée"
    except AssertionError :
        return "Liste non triée : il faut fournir une liste déjà triée"
    gauche = 0
    droite = len(l)-1
    milieu = ( gauche + droite ) // 2
    while ( gauche <= droite ) :
        if ( l[milieu] == x ) :
            return True
        elif ( l[milieu] > x ) :
            droite = milieu - 1
            milieu = ( gauche + droite ) // 2
        elif ( l[milieu] < x ) :
            gauche = milieu + 1
            milieu = ( gauche + droite ) // 2
    return False

# Test avec une liste non triée :
print(l)
print(dichotomie(l, 5))

# On trie la liste et on recommence
l.sort()
print(l)
print(dichotomie(l, 5))

# EXO : COMPARAISON DES COMPLEXITES DES RECHERCHES DICHOTOMIQUE ET NAIVE
# On ne considère que des listes triées
# Q1 ) Implanter la recherche : on parcourt la liste dans l'ordre, jusqu'à trouver l'élément ou arriver à la fin

def recherche_naive (l, x) :
    pass


# Q2 ) Définir une liste de taille 100 telle que la recherche naive effectue le maximum d'opérations. Combien effectue-t-elle d'opérations ? Implanter un compteur comptant le nombre de tour de boucles effectués, et afficher sa valeur.


# Q3) Définir une liste de taille 100 telle que la recherche dichotomique effectue le maximum d'opérations. Implanter un compteur comptant le nombre de tour de boucles effectués, et afficher sa valeur.


# Q4) (Théorie uniquement) Comparaison des complexités dans le pire des cas. Idem avec des listes initiales de taille n :
# i) Combien d'opérations sont effectuées dans le pire des cas pour la recherche naïve sur une liste de taille n ?
# ii) Combien d'opérations sont effectuées dans le pire des cas pour la recherche dichotomique sur une liste de taille n ?

# Q5) Faire un tour sur la doc officielle python et utiliser le module time pour faire des tests de comparaisons des deux recherches (naïve et dichotomique)