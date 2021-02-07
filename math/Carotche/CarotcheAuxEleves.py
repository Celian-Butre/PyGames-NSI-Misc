import random #Module random pour simuler le hasard d’une planche de Galton authentique
import matplotlib.pyplot as plt #Module matplotlib pour représenter l’issue de la planche de Galton appelable avec plt


def simulation_trajectoire(hauteur): #Définition de la fonction (Entrée: hauteur (pas le nombre de billes)) 
    trajectoire = [] #Indication que trajectoire est une liste
    for etage in range(hauteur): #Répété pour chaque étage
        trajectoire.append(random.choice(("gauche", "droite"))) #Rajouter au hasard "gauche" ou "droite" à la fin de la liste trajectoire
    return(trajectoire) #Retourner la liste trajectoire où la fonction a été appelé

def simul_une_bille(hauteur): #Définition de la fonction (Entrée: hauteur (pas le nombre de billes ni la trajectoire qui est calculée à l'intérieur même de la fonction))
    trajectoire = simulation_trajectoire(hauteur) #Génération de la trajectoire avec la fonction précédente
    lieuAtterissage = 0 #Initialisation du lieu d'atterissage au casier tout à gauche
    for etage in range(len(trajectoire)): #Parcours de la liste trajectoire( répétition de longueur taille de trajectoire, faisant varié la variable étage)
        if trajectoire[etage] == "droite": #Test si l'élément de trajectoire en position indiquée par la variable étage est égale à la chaine de caractère "droite"
            lieuAtterissage = lieuAtterissage + 1 #Incrémentation de lieuAtterissage de 1, la position ou la bille va atterrir est un de plus vers la droite.
    return(lieuAtterissage) #Retourner la variable lieuAtterissage où la fonction a été appelé: rend la position où la bille va atterrire

def simul_N_billes(nbBilles, hauteur): #Définition de la fonction (Entrée: hauteur et le nombres de billes) 
    planche = [] #Indication que la planche est une liste
    for i in range(hauteur+1): #Pour chaque casier (hauteur + 1)
        planche.append(0) #Rajouter un 0 à la fin de la liste
    #Ceci produit une liste qui ressemble à [0, 0, 0, 0, 0] autant de 0 que de casiers
    for i in range(nbBilles): #Pour chaque bille qui va tombé
        planche[simul_une_bille(hauteur)] += 1 #Rajouter une bille dans le casier où la bille tombe, lieu d'atterissage déterminé par l'appel de la fonction précédente
    return(planche) #Retourne l'état final de la planche après que toute les billes soient tombées.

def affiche_matplotlib(nbBilles, hauteur): #Définition de la fonction (Entrée: hauteur et nombres de billes) 
    plt.bar(range(hauteur+1), simul_N_billes(nbBilles, hauteur)) #Faire un graphe en bar, de longueur du nombre de casiers = hauteur + 1, déterminé par la quantité de billes dans chaque casier, lui-même déterminé par la fonction précédente
    plt.show() #Afficher le graphe généré ci-dessus