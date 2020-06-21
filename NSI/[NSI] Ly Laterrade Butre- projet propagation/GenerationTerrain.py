import random, copy
def Creer_Grille (Liste_Cases, iterations):     # Fonction qui permet de creer une matrice de la taille demandee
    for i in range (iterations):                # autant de fois que demande
        Liste_Cases.append([])                  # rajouter une liste dans la liste

def Creer_Case (iterations_2, biome_case, intensite_case, etat_case, Liste_Cases):              # Fonction qui cree chaque case
    dictionary = {"Biome" : biome_case, "Intensite du feu" : intensite_case, "etat" : etat_case}# Chaque case est un dictionnaire, defini par son biome son intensite et son etat
    Liste_Cases[iterations_2].append(dictionary)                                                # rajoute a la matrice

def checkNeighboursExist(coord_i,coord_j, Choixbiome):      # Fonction qui verifie si les cases autour d'une case existe (Pour gerer les bords/coins)
    neighboursExist = []                                    # Creation d'une liste qui dira si oui ou non la case existe
    for i in range(-1,2,1):                                 # i et j vont donc etre egal a -1, 0, 1, pour verifier toutes les cases autour de celles dont on a les coordonnees
        for j in range(-1,2,1):
            while True:
                try:
                    assert(coord_i + i < len(Choixbiome))   # on ajoute i a coord_i pour verifier si ceci est superieur a 0 et inferieur a la longueur de la matrice
                    assert(coord_i + i >= 0)
                    assert(coord_j + j < len(Choixbiome))   # on ajoute j a coord_j pour verifier si ceci est superieur a 0 et inferieur a la longueur de la matrice
                    assert(coord_i + i >= 0)
                except AssertionError:
                    neighboursExist.append(0)               # si cette addition n'est pas verifiee, alors on en deduit que la case n'existe pas : on met 0 dans la liste
                    break
                neighboursExist.append(1)                   # puisque la case existe : on met 1 dans la liste
                break
    return neighboursExist                                  # on retourne la liste qui nous dit si elle existe ou no

def seedToForest(Choixbiome, iterations, forestSeeds, pourcentage_foret):   # fonction qui permet de faire evoluer une foret a partir d'un seul point foret
    cptForet = 0                                                            # compteur qui compte le nombre de cases de forets present
    for i in range (forestSeeds):                                           # repetera le nombre de forets demandees ( nombre de forets != nombre de cases de forets)
        Choixbiome[random.randint(0,iterations-1)][random.randint(0,iterations-1)]= 1   # Une case aleatoire dans la matrice Choixbiome deviendra foret
        cptForet += 1                                                       # compteur augmente de 1
    while cptForet < ((pourcentage_foret)*iterations*iterations):           # tant que le nombre de cases de forets est inferieur au pourcentage voulu de la surface totale
        forestStorage = copy.deepcopy(Choixbiome)                           # permet d'eviter que les forets qui viennent d'etre rajouter soient prises en compte ce tour-ci
        for i in range(iterations):                                         # parcours la matrice
            for j in range(iterations):
                if forestStorage[i][j] == 1:                                # si la case est une foret
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)  # verifie que les cases autour existent
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]    # positions que peuvent occuper les voisins (en fonction des coordonnees de la case)
                    for k in range(len(neighboursExist)):                   # parcours la liste
                        randomNumberChoice = random.randint(1,10)           # ajoute une variable aleatoire
                        if (randomNumberChoice > 6 and neighboursExist[k] == 1):                    # si la variable aleatoire est superieure a 6 et la case voisine existe
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] == 0: # et si cette case voisine est une plaine (note qu'il n'y a que des plaines et des forets a ce stade)
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 1  # cette case voisine devient une foret
                                cptForet += 1                               # on rajoute 1 au compteur
    return Choixbiome

def dropToLake(Choixbiome, iterations, waterDroplets, pourcentage_lac): # fonction identique a au dessus, mais pour l'eau et verifiant que les cases choisies ne sont pas des forets
    cptLac = 0
    for i in range (waterDroplets):
        randomNumber1 = random.randint(0,iterations-1)                  # Coordonnees aleatoires pour la premiere "goutte"
        randomNumber2 = random.randint(0,iterations-1)
        while True:
            try:
                assert(Choixbiome[randomNumber1][randomNumber2] != 1)   # assert que ces coordonnees ne sont pas celles d'une case foret
                break
            except AssertionError:                                      # si cette assertion est fausse
                randomNumber1 = random.randint(0,iterations-1)          # de nouvelles coordonnees aleatoires sont donnees pour cette "goutte"
                randomNumber2 = random.randint(0,iterations-1)
        Choixbiome[randomNumber1][randomNumber2] = 2                    # la case avec ces coordonnees est maintenant une case eau
        cptLac += 1                                                     # augmente le compteur
    while cptLac < ((pourcentage_lac)*iterations*iterations):           # identique a au dessus mais avec des variables "lac"
        lakeStorage = copy.deepcopy(Choixbiome)
        for i in range(iterations):
            for j in range(iterations):
                if lakeStorage[i][j] == 2:
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    for k in range(len(neighboursExist)):
                        randomNumberChoice = random.randint(1,10)
                        if (randomNumberChoice > 6) and (neighboursExist[k] == 1):
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] == 0: # Verifie que la case est une plaine (est non une foret ou deja un lac)
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 2
                                cptLac += 1
    return Choixbiome

def makeSomeHouses(Choixbiome, iterations, howManyHouses):          # fonction qui cree des maisons
    for i in range (howManyHouses):                                 # repete autant de fois que l'on a demande de maisons
        randomNumber1 = random.randint(0,iterations-1)              # coordonnees aleatoires
        randomNumber2 = random.randint(0,iterations-1)
        while True:
            try:
                assert(Choixbiome[randomNumber1][randomNumber2] != 2)   # s'assure que la maison n'est pas dans un lac
                break
            except AssertionError:
                randomNumber1 = random.randint(0,iterations-1)          # si l'assertion est fausse, de nouvelles coordonnees sont generees
                randomNumber2 = random.randint(0,iterations-1)
        Choixbiome[randomNumber1][randomNumber2] = 3                    # la case devient une maison
    return Choixbiome

def housesHavePlantations(Choixbiome, iterations, pourcentage_plantation):          # fonction qui cree des plantations, autour des maisons (idem que fonctions seedToForest et dropToLake)
    cptPlantation = 0
    while cptPlantation < ((pourcentage_plantation)*iterations*iterations):
        plantationStorage = copy.deepcopy(Choixbiome)
        for i in range(iterations):
            for j in range(iterations):
                if plantationStorage[i][j] == 3 or plantationStorage[i][j] == 4:    # si la case est une maison ou une plantation
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    for k in range(len(neighboursExist)):
                        randomNumberChoice = random.randint(1,10)
                        if (randomNumberChoice > 6 and neighboursExist[k] == 1):
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] != 3: # si la case n'est pas une maison (plantation a priorite sur tout sauf les maisons)
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 4  # la case devient une plantation
                                cptPlantation += 1
    return Choixbiome
    
def Choixbiome(iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation):  # fonction qui genere la grille de generation de terrain
    Choixbiome=[]                           # Liste cree pour le choix du biome
    for i in range (iterations):            # la taille de la matrice est implantee ici
        Choixbiome.append([])               # la liste devient une liste de liste
        for j in range (iterations):        # le nombre de cases est implante ici, de meme taille que la matrice
            Choixbiome[i].append(0)         # chaque case est egale a 0, elles sont tous des plaines
    Choixbiome = seedToForest(Choixbiome, iterations, forestSeeds, pourcentage_foret)   # on y implante les forets
    Choixbiome = dropToLake(Choixbiome, iterations, waterDroplets, pourcentage_lac)     # puis les lacs
    Choixbiome = makeSomeHouses(Choixbiome, iterations, howManyHouses)                  # puis les maisons
    Choixbiome = housesHavePlantations(Choixbiome, iterations, pourcentage_plantation)  # puis les plantations
    return Choixbiome                       # on retourne une matrice avec un biome par case, genere de maniere intelligente

def Remplir_Grille_Initiale(Liste_Cases, iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation):
    Creer_Grille(Liste_Cases, iterations)                               # on genere la matrice vide
    choix_Biome = Choixbiome(iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation)     # on genere une autre matrice avec tous les choix de biomes
    for j in range(iterations):                                         # on parcourt la matrice
        for i in range(iterations):
            Creer_Case (j,choix_Biome[i][j], 0, "Vierge", Liste_Cases)  # le biome vient de la matrice choix_Biome, ils ont tous une intensite initiale de 0, et commencent tous dans l'etat "Vierge"
