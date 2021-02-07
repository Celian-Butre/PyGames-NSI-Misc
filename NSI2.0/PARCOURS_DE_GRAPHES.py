# PARCOURS DE GRAPHES

import random

G1 = [ 
    [1, 2],         # voisins de 0
    [0, 3],         # voisins de 1
    [0, 3, 4],      # voisins de 2
    [1, 2, 4, 7],   # voisins de 3
    [2, 3, 7],      # voisins de 4
    [7],            # voisins de 5
    [7],            # voisins de 6
    [3, 4, 5, 6, 7] # voisins de 7
    ]

G2 = [
    [1, 6, 7],       # voisins de 0
    [0, 2, 4, 5, 6], # voisins de 1
    [1],             # voisins de 2
    [5, 6, 8],       # voisins de 3
    [1],             # voisins de 4
    [1, 3, 6],       # voisins de 5
    [0, 1, 3, 5, 7], # voisins de 6
    [0, 6, 8],       # voisins de 7
    [3, 7],          # voisins de 8
    ]

G3 = [ 
    [1, 3],         # voisins de 0
    [0, 4],         # voisins de 1
    [3, 4],         # voisins de 2
    [0, 2, 4],      # voisins de 3
    [1, 2, 3]       # voisins de 4
    ]

# V Q1) Représenter graphiquement les deux graphes G1 et G2


# V Q2) Implanter une fonction retournant la liste des sommets à partir de la liste d'adjacence (sans tricher, car on sait déjà que la liste des sommets est [0, 1, 2, ...] jusqu'à la taille-1 de la liste d'adjacence)

def Q2(graphe):
    listeDesSommet = []
    for i in range (len(graphe)):
        for j in range (len(graphe[i])):
            alreadyIn = False
            for l in range (len(listeDesSommet)):
                if listeDesSommet[l] == graphe[i][j]:
                    alreadyIn = True
            if alreadyIn == False:
                listeDesSommet.append(graphe[i][j])
    
    return(listeDesSommet)

def parcours_perso (graphe) :
    fullListeSommet = Q2(graphe)
    sommetRestant = fullListeSommet
    foundSommetsNotExplored = [0]
    while sommetRestant != []:
        currentSommet = foundSommetsNotExplored[0] 
        foundSommetsNotExplored.remove(currentSommet)
        for i in range(len(graphe[currentSommet])):
            if isPartOfList(graphe[currentSommet][i], sommetRestant):
                sommetRestant = visiter_sommet(graphe[currentSommet][i], sommetRestant)
                foundSommetsNotExplored.append(graphe[currentSommet][i])

def visiter_sommet(s, sommetRestant) :
    sommetRestant.remove(s)
    print(s, ' il reste a visiter :', sommetRestant, end=" ")
    return sommetRestant        
        
def isPartOfList(a, liste):
    if a in liste:
        return(True)
    else:
        return (False)
print()
print("Parcours perso sur les graphes G1 et G2 : ")
print("Graphe G1 : ", end="")
parcours_perso(G1)
print()
print("Graphe G2 : ", end="")
print()
parcours_perso(G2)


# V Q3) Vérifier que l'exécution des fonctions ci-dessous correspondent bien aux graphes G1 et G2 dessinés en Q1). 

def visiter_sommet(s, sommetRestant) :
    try:
        sommetRestant.remove(s)
    except:
        pass
    print(s, ' il reste a visiter :', sommetRestant, end=" ")
    return sommetRestant

def parcours_bis (graphe) :
    fullListeSommet = Q2(graphe)
    sommetRestant = fullListeSommet
    liste_sommets = []
    restant_a_traiter = []
    restant_a_traiter.append(0)
    while ( len(restant_a_traiter) != 0 ) :
        sommet_en_cours = restant_a_traiter.pop()
        if ( sommet_en_cours in liste_sommets ) :
            pass
        else :
            sommetRestant = visiter_sommet(sommet_en_cours, sommetRestant)
            liste_sommets.append(sommet_en_cours)
            for voisin in graphe[sommet_en_cours] :
                restant_a_traiter.append(voisin)

print()
print("Parcours bis sur les graphes G1 et G2 : ")
print("Graphe G1 : ", end="")
parcours_bis(G1)
print()
print("Graphe G2 : ", end="")
parcours_bis(G2)
print()
print("Graphe G3 : ", end="")
parcours_bis(G3)


#  V Q4) Modifier la fonction parcours_bis pour qu'elle affiche l'évolution pas-à-pas de la liste des sommets à traiter qu'il lui reste à traiter (pour plus de lisibilité, on pourra également la modifier pour qu'elle retourne la liste des sommets au lieu de les afficher avec la fonction visiter())


# Q5)
#  V i)  Exécuter la fonction parcours_bis modifiée sur les graphes G1 et G2.

#  V ii) Implanter une autre graphe G3 et exécuter la fonction parcours_bis dessus.


#  V Q6) Dans quel ordre est effectué le parcours ? (en partant de 0 et explorant les tous les voisins d'un point, puis en répétant avec le premier nouveau point rencontrer) Quel est le type de structure utilisée pour stocker les sommets à traiter ? (une liste) Comparer avec votre fonction parcours_perso. (j'ai fait pareille sans faire exprès, désolé!)


#  V Q7) Quelles sont les différentes méthodes de parcours d'un graphe ? (on peut en faire un qui traverse aléatoirement comme il veut) Implanter et tester la (les) méthodes ne figurant pas dans les fonctions précédentes (on pourra penser à utiliser un autre type de structure pour stocker les sommets à traiter).

def parcours_ter (graphe) :
    fullListeSommet = Q2(graphe)
    sommetRestant = fullListeSommet
    foundSommet = [0]
    sommetRestant.remove(0)
    while sommetRestant != []:
        currentSommet = foundSommet[random.randint(0, len(foundSommet) - 1)]
        sommetVisit = graphe[currentSommet][random.randint(0, len(graphe[currentSommet]) - 1)]
        if isPartOfList(graphe[currentSommet][random.randint(0, len(graphe[currentSommet]) - 1)], sommetRestant):
            sommetRestant = visiter_sommet(sommetVisit, sommetRestant)
            foundSommet.append(sommetVisit)
            
        
# test pour la Q2
#print(Q2(G2))

print()
print("Parcours ter sur les graphes G1 et G2 : ")
print("Graphe G1 : ", end="")
parcours_ter(G1)
print()
print("Graphe G2 : ", end="")
parcours_ter(G2)
print()
print("Graphe G3 : ", end="")
parcours_ter(G2)
print()