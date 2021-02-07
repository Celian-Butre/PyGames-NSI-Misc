import random

l = []
for i in range(50) :
    l.append(random.randint(0,100))

def recherche_par_dichotomie (l, x) :
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
print(recherche_par_dichotomie(l, 5))

# On trie la liste et on recommence
l.sort()
print(l)
print(recherche_par_dichotomie(l, 5))

# EXO : COMPARAISON DES COMPLEXITES DES RECHERCHES DICHOTOMIQUE ET NAIVE
# On ne considère que des listes triées
# Q1) Implanter la recherche : on parcourt la liste dans l'ordre, jusqu'à trouver l'élément ou arriver à la fin

def recherche_naive (l, x) :
    i = 0
    while ( i < len(l) ) :
        if ( l[i] == x ) :
            return True
        elif ( x < l[i] ) :
            return False
        i = i + 1
    return False

# Q2) Définir une liste de taille 100 telle que la recherche naive effectue le maximum d'opérations. Combien effectue-t-elle d'opérations ? Implanter un compteur comptant le nombre de tour de boucles effectués, et afficher sa valeur.

val_max = 1000
liste_test = [ i for i in range(val_max) ]
element_absent = val_max + 1

print(recherche_naive(liste_test, element_absent))

# Q3) Définir une liste de taille 100 telle que la recherche dichotomique effectue le maximum d'opérations. Implanter un compteur comptant le nombre de tour de boucles effectués, et afficher sa valeur.

def recherche_naive_compteur (l, x) :
    i = 0
    while ( i < len(l) ) :
        if ( l[i] == x ) :
            return (True, i)
        elif ( x < l[i] ) :
            return (False, i)
        i = i + 1
    return (False, i)

def recherche_par_dichotomie_compteur (l, x) :
    try :
        assert l == sorted(l), "Le premier argument doit être une liste triée"
    except AssertionError :
        return "Liste non triée : il faut fournir une liste déjà triée"
    gauche = 0
    droite = len(l)-1
    milieu = ( gauche + droite ) // 2
    nb_tours = 0
    while ( gauche <= droite ) :
        nb_tours = nb_tours + 1
        if ( l[milieu] == x ) :
            return (True, nb_tours)
        elif ( l[milieu] > x ) :
            droite = milieu - 1
            milieu = ( gauche + droite ) // 2
        elif ( l[milieu] < x ) :
            gauche = milieu + 1
            milieu = ( gauche + droite ) // 2
    return (False, nb_tours)


print("Résultat recherche naïve :", recherche_naive_compteur(liste_test, element_absent))

print("Résultat recherche par dichotomie :", recherche_par_dichotomie_compteur(liste_test, element_absent))


# Q4) (Théorie uniquement) Comparaison des complexités dans le pire des cas. Idem avec des listes initiales de taille n :
# i) Combien d'opérations sont effectuées dans le pire des cas pour la recherche naïve sur une liste de taille n ?
# ii) Combien d'opérations sont effectuées dans le pire des cas pour la recherche dichotomique sur une liste de taille n ?

# Q5) Faire un tour sur la doc officielle python et utiliser le module time pour faire des tests de comparaisons des deux recherches (naïve et dichotomique)

import time

val_max = 10000000
liste_test = [ i for i in range(val_max) ]
element_absent = val_max + 1

t_0 = time.time()
recherche_naive_compteur(liste_test, element_absent)
t_1 = time.time()
temps_execution = t_1 - t_0
print("Temps d'exécution de la recherche naïve dans le pire des cas pour une liste de taille", val_max, ":", temps_execution, "sec")

t_0 = time.time()
recherche_par_dichotomie_compteur(liste_test, element_absent)
t_1 = time.time()
temps_execution = t_1 - t_0
print("Temps d'exécution de la recherche par dichotomie dans le pire des cas pour une liste de taille", val_max, ":", temps_execution, "sec")
