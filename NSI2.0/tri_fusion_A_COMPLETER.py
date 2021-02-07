# TRI FUSION DE LISTES


def scinder_liste(l) :
    """
    Entrée : une liste
    Sortie : deux listes correspondant aux première et deuxième moitiés de la liste d'entrée
    """ 
    return ( l[:len(l)//2] , l[len(l)//2:] )    # une seule ligne, c'est toujours mieux que plein de lignes (et ça reste à peu près lisible ici)


def fusionner_listes_triees (l1, l2) :
    """
    Entrée : deux listes triées
    Sortie : liste triée des éléments de l1 et l2
    """
    # on s'assure que les listes données en entrée sont bien triées (sinon on renvoit un message d'erreur) :
    # print(l1, ' b ', l2) debug
    assert ( l1 == sorted(l1) and l2 == sorted(l2) ), "Les listes données en arguments de la fonction de fusion de listes doivent être données déjà triées"
    # Cas de liste(s) vide(s) :
    if l1 == l2 == [] :
        return []
    if l1 == [] :
        return l2
    if l2 == [] :
        return l1
    # Cas de deux listes non vides :
    finishedList = []
    # A COMPLETER (distinguer les cas l1 épuisée ; l2 épuisée ; et le cas où il reste des éléments non traités dans chacune des listes l1 et l2)
    len1 = len(l1)
    len2 = len(l2)
    place1 = 0
    place2 = 0
    finishedList = []
    while len1 != place1 and len2 != place2:
        if l1[place1] <= l2[place2]:
            finishedList.append(l1[place1])
            place1 += 1
        else:
            finishedList.append(l2[place2])
            place2 += 1
        
    if place1 == len1:
        finishedList+= l2[place2:]
    else:
        finishedList+= l1[place1:]
        
    # print('d ', finishedList)  debug  
    return finishedList


def tri_fusion(l) :
    """
    Entrée : une liste quelconque
    Sortie : une version triée de la liste d'entrée
    Remarque : il ne s'agit donc pas d'un tri en place
    """
    # A COMPLETER
    # Deux étapes : 
    # - cas de base (liste à un élément, mais on peut rajouter dans ce cas le cas de la liste vide, déjà triée)
    if l == [] or len(l) == 1:
        return(l)
    # - cas d'induction : on coupe la liste en deux listes, on les trie récursivement, et on les fusionne grâce à la fonction de fusion de listes triées
    else:
        l1, l2 = scinder_liste(l)
        # print(l1, 'a' , l2) pour debugger a un moment
        if len(l1) != 1 and len(l1) != 0: # != 0 juste pour être sure
            l1 = tri_fusion(l1)
        if len(l2) != 1 and len(l2) != 0: # != 0 juste pour être sure
            l2 = tri_fusion(l2)
            # print('f ', l2) debug
        # print(l1,' c ',l2) debug
        l = fusionner_listes_triees(l1,l2)
    # print('e ', l) debug
    return(l)
    


# TESTS
if __name__ == '__main__' :

    # Tests "à la main" :
    assert tri_fusion([]) == [], "Oubli du cas liste vide dans le tri fusion"
    assert tri_fusion([-6, -8, 5, 0, 0, 10, -10]) == [-10, -8, -6, 0, 0, 5, 10], "Bug dans le tri fusion"

    # Tests générés automatiquement
    import random

    def generer_liste(n=20) :
        l =[]
        for i in range(n) :
            l.append(random.randint(-100, 100))
        return l

    l = generer_liste()

    assert tri_fusion(l) == sorted(l), "Bug dans le tri fusion"
    
    # Affichage 
    print("Liste générée aléatoirement :", l)
    print("Liste triée par un magnifique tri fusion :", tri_fusion(l))
    
    iterations  = 100000
    reussite = 0
    for i in range(iterations):
        l = generer_liste()
        if tri_fusion(l) == sorted(l):
            reussite += 1

    print('fonction testee', iterations,'fois, fonction reussie', reussite, 'fois') #marche statistiquement 100% du temps.