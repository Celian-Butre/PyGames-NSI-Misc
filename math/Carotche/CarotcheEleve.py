import random
import matplotlib.pyplot as plt

# h = hauteur; n = nombres de billes lachées

def simulation_trajectoire(hauteur):
    trajectoire = []
    for etage in range(hauteur):
        trajectoire.append(random.choice(("gauche", "droite")))
    return(trajectoire)

def simul_une_bille(hauteur):
    trajectoire = simulation_trajectoire(hauteur)
    lieuAtterissage = 0
    for etage in range(len(trajectoire)):
        if trajectoire[etage] == "droite":
            lieuAtterissage += 1
    return(lieuAtterissage)

def simul_N_billes(nbBilles, hauteur):
    planche = []
    for i in range(hauteur+1):
        planche.append(0)
    for i in range(nbBilles):
        planche[simul_une_bille(hauteur)] += 1
    return(planche)

def affiche_matplotlib(nbBilles, hauteur):
    plt.bar(range(hauteur+1), simul_N_billes(nbBilles, hauteur))
    plt.show()
    
    
if __name__ == "__main__":
    affiche_matplotlib(500, 6)
    