import random, copy, pygame

def Commencer_Feu(startCoord_j, startCoord_i, Liste_Cases):             # fonction qui commence un feu a partir de coordonnees
    if Liste_Cases[startCoord_i][startCoord_j]["Biome"] != 2:           # si la case n'est pas de l'eau
        Liste_Cases[startCoord_i][startCoord_j]["Intensite du feu"] = 1 # l'intensite de cette case est egale a 1
        Liste_Cases[startCoord_i][startCoord_j]["etat"] = "Brule"       # l'etat de cette case est "Brule"
    return Liste_Cases

def addFire(Liste_Cases):               # fonction qui permet de commencer un feu en cliquant sur une case
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    mouse = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    if mouse[0] == 1:
        mousepressed = True
    else:
        mousepressed = False
    
    if mousepressed == True and mousepos[0] > 250 and mousepos[0] < 850 and mousepos[1] > 0 and mousepos[1] < 600:
        return(Commencer_Feu((mousepos[0]-250)//6, mousepos[1]//6, Liste_Cases))
    else:
        return(Liste_Cases)
    
def Progression_Braises(Liste_Cases):                       # fonction qui permet la progression de l'intesite du feu des cases
    listeIntensiteMax = [2, 4, 0, 8, 4]                     # intensiteMax : Plaine = 2, Foret = 4, Eau = 0, Maison = 8, Plantation = 4
    for i in range(len(Liste_Cases)):                       # parcours la matrice
        for j in range(len(Liste_Cases)):
            if Liste_Cases[i][j]["Intensite du feu"] > 0:   # si l'intensite de la case est superieur a 0
                if Liste_Cases[i][j]["etat"] == "Brule":    # si la case brule
                    Liste_Cases[i][j]["Intensite du feu"] += 1  # l'intensite augmente de 1
                    if Liste_Cases[i][j]["Intensite du feu"] == listeIntensiteMax[Liste_Cases[i][j]["Biome"]]: # si l'intensite du feu est egal a l'intensite max de son biome
                        Liste_Cases[i][j]["etat"] = "Estompe"   # la case commencera a s'estomper : son etat est "Estompe"
                elif Liste_Cases[i][j]["etat"] == "Estompe":    # sinonsi la case s'estompe
                    Liste_Cases[i][j]["Intensite du feu"] -= 1  # l'intensite du feu de la case diminue de 1
                    if Liste_Cases[i][j]["Intensite du feu"] == 0:  # si l'intensite du feu est egal a 0
                        Liste_Cases[i][j]["etat"] = "Calcinee"  # l'etat devient "Calcinee"
    return Liste_Cases

def checkNeighbourOnFire(coord_i,coord_j, Liste_Cases, Meteo_Extractee, Vent_Extractee): # fonction qui retourne une liste des probabilites des voisins d'une case
    neighboursOnFire = []                                       # initialisation de la liste
    for i in range(-1,2,1):                                     # coordonnees des voisins
        for j in range(-1,2,1):
            while True:                                         # Verification que les voisins existent (voir checkNeighboursExist dans GenerationTerrain.py)
                try:
                    assert(coord_i + i < len(Liste_Cases))
                    assert(coord_i + i >= 0)
                    assert(coord_j + j < len(Liste_Cases))
                    assert(coord_j + j >= 0)
                except AssertionError:
                    neighboursOnFire.append(False)              # s'ils n'existent pas ajouter false "False"
                    break
                if (i != 0) or (j != 0):                        # si ce n'est pas la case en question
                    ListeFacteurTerrain = [0.5, 1, 0, 0.5, 1]   # Liste des facteurs terrains correspond au N du calcul
                    ListeIntensiteMax = [2, 4, 0, 8, 6]         # Liste des intensites Max correspond au intensiteMax du calcul
                    if ((j+i == 0) or (j+i == -2) or (j+i == 2)):   # Si les voisins sont en diagonales
                        FacteurDistance = int(25)               # M = 25
                    else:                                           # Sinon
                        FacteurDistance = int(75)               # M = 75
                    FacteurTerrain = float(ListeFacteurTerrain[Liste_Cases[coord_i+i][coord_j+j]["Biome"]]) # Choix de N en fonction du Biome
                    IntensiteMax = int(ListeIntensiteMax[Liste_Cases[coord_i+i][coord_j+j]["Biome"]])       # Choix de intensiteMax en fonction du Biome
                    IntensiteActuelle = int(Liste_Cases[coord_i+i][coord_j+j]["Intensite du feu"])          # Choix de l'intensite actuelle, k dans le calcul
                    InfluenceMeteo = 0              # Correspond a p dans le calcul, mais est rebaptise m
                    InfluenceVent = 0               # Correspond a v dans le calcul
                    if IntensiteActuelle != 0:      # Si la case est en feu
                        ProbabiliteFeu =round(FacteurTerrain*FacteurDistance*(float(0.75)**(IntensiteMax - IntensiteActuelle)),3) #P = N ∗ M ∗ (0.75)^(intensiteMax−k)
                        if Meteo_Extractee == "Pluie" or Meteo_Extractee == "Foudre":   # s'il pleut
                            InfluenceMeteo = -0.5                                       # m = -0,5
                        elif Meteo_Extractee == "Grand_Soleil":                         # sinons'il y a un grand soleil
                            InfluenceMeteo = 0.25                                       # m = 0,25

                        if Vent_Extractee != "Aucun":                                   # s'il y a du vent
                            listeDirectionsProbabilite = [[[0.25,0.25,0.25],[0,0,0],[-1,-1,-1]], [[-1,0,0.25],[-1,0,0.25],[-1,0,0.25]], [[-1,-1,-1],[0,0,0],[0.25,0.25,0.25]], [[0.25,0,-1],[0.25,0,-1],[0.25,0,-1]]]
                            listeDirectionsPlace = ["Sud", "Ouest", "Nord", "Est"]      # Directions du vent
                            for k in range(len(listeDirectionsPlace)):                  # Transformation du vent en position chiffree
                                if listeDirectionsPlace[k] == Vent_Extractee:
                                    Place = k
                            InfluenceVent = listeDirectionsProbabilite[Place][i+1][j+1] # Selection de v appropriee, en fonction du vent et des coordonnees de la case
                            
                            #       Nord            Est             Sud                 Ouest
                            #[0.25][0.25][0.25] [-1][0][0.25]   [-1][-1][-1]        [0.25][0][-1]     
                            #[0]   [0]   [0]    [-1][0][0.25]   [0][0][0]           [0.25][0][-1]     
                            #[-1]  [-1]  [-1]   [-1][0][0.25]   [0.25][0.25][0.25]  [0.25][0][-1]
                            
                        ProbabiliteFeu = ProbabiliteFeu + ProbabiliteFeu * InfluenceMeteo + ProbabiliteFeu * InfluenceVent      #Proba = P+P*v+P*m
                        neighboursOnFire.append(ProbabiliteFeu)                                                                 # on rajoute a la liste la probabilite
                    else:                           # Si la case n'est pas en feu                        
                        neighboursOnFire.append(0)  # on rajoute 0 a la liste
                    break
                break
    return neighboursOnFire                         # on retourne la liste des probabilites des cases voisines

def La_Propagation_Feu(Liste_Cases, Meteo_Extractee, Vent_Extractee):   # fonction qui permet la propagation du feu
    Liste_Cases_Renfort = copy.deepcopy(Liste_Cases)                    # permet d'eviter que la fonction considere les cases qui se mettent a bruler pdt l'activation de la fonction, seulement ceux qui brulaient deja
    for i in range (len(Liste_Cases)):                                  # parcours la matrice
        for j in range (len(Liste_Cases)):
            if Liste_Cases[i][j]["etat"] == "Vierge" and Liste_Cases[i][j]["Biome"] != 2:                           # si la case est Vierge, et n'est pas un lac
                neighboursOnFire = checkNeighbourOnFire(i, j, Liste_Cases_Renfort, Meteo_Extractee, Vent_Extractee) # verification des probabilites de propagation des voisins
                for k in range(len(neighboursOnFire)):                                  # parcours la liste
                    if (neighboursOnFire[k] != False) and (neighboursOnFire[k] > 0):    # si le voisin existe et sa probabilite est superieure a 0
                        ProbabilityOnFire = (round(random.uniform(0,100),3))            # variable aleatoire
                        if ProbabilityOnFire < neighboursOnFire[k]:                     # si la variable aleatoire est inferieure a la probabilite de propagation du voisin
                            Liste_Cases[i][j]["etat"] = "Brule"                         # la case se met a bruler
                            Liste_Cases[i][j]["Intensite du feu"] = 1
                            break
    return Liste_Cases
