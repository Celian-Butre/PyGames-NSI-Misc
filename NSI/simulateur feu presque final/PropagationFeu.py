import random, copy, pygame

def Commencer_Feu(startCoord_j, startCoord_i, Liste_Cases):
    if Liste_Cases[startCoord_i][startCoord_j]["Biome"] != 2:
        Liste_Cases[startCoord_i][startCoord_j]["Intensite du feu"] = 1
        Liste_Cases[startCoord_i][startCoord_j]["etat"] = "Brule"
    return Liste_Cases

def addFire(Liste_Cases):
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
    
def Progression_Braises(Liste_Cases):                   
    listeIntensiteMax = [2, 4, 0, 8, 4]                     #intensiteMax : Plaine = 2, Foret = 4, Eau = 0, Maison = 8, Plantation = 4
    for i in range(len(Liste_Cases)):
        for j in range(len(Liste_Cases)):
            if Liste_Cases[i][j]["Intensite du feu"] > 0:
                if Liste_Cases[i][j]["etat"] == "Brule":
                    Liste_Cases[i][j]["Intensite du feu"] += 1
                    if Liste_Cases[i][j]["Intensite du feu"] == listeIntensiteMax[Liste_Cases[i][j]["Biome"]]:
                        Liste_Cases[i][j]["etat"] = "Estompe"
                elif Liste_Cases[i][j]["etat"] == "Estompe":
                    Liste_Cases[i][j]["Intensite du feu"] -= 1
                    if Liste_Cases[i][j]["Intensite du feu"] == 0:
                        Liste_Cases[i][j]["etat"] = "Calcinee"
    return Liste_Cases

def checkNeighbourOnFire(coord_i,coord_j, Liste_Cases, Meteo_Extractee, Vent_Extractee):
    neighboursOnFire = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            while True:
                try:
                    assert(coord_i + i < len(Liste_Cases))
                    assert(coord_i + i >= 0)
                    assert(coord_j + j < len(Liste_Cases))
                    assert(coord_j + j >= 0)
                except AssertionError:
                    neighboursOnFire.append(False)
                    break
                if (i != 1) or (j != 1):
                    ListeFacteurTerrain = [0.5, 1, 0, 0.5, 1]
                    ListeIntensiteMax = [2, 4, 0, 8, 6]
                    if ((j+i == 0) or (j+i == -2) or (j+i == 2)):
                        FacteurDistance = int(25)
                    else:
                        FacteurDistance = int(75)
                    FacteurTerrain = float(ListeFacteurTerrain[Liste_Cases[coord_i+i][coord_j+j]["Biome"]])
                    IntensiteMax = int(ListeIntensiteMax[Liste_Cases[coord_i+i][coord_j+j]["Biome"]])
                    IntensiteActuelle = int(Liste_Cases[coord_i+i][coord_j+j]["Intensite du feu"])
                    InfluenceMeteo = 0
                    InfluenceVent = 0
                    if IntensiteActuelle != 0:
                        ProbabiliteFeu =round(FacteurTerrain*FacteurDistance*(float(0.75)**(IntensiteMax - IntensiteActuelle)),3) #P = N ∗ M ∗ (0.75)^(intensiteMax−k)
                        if Meteo_Extractee == "Pluie" or Meteo_Extractee == "Foudre":
                            InfluenceMeteo = 0.25
                        elif Meteo_Extractee == "Grand_Soleil":
                            InfluenceMeteo = -0.25
                        if Vent_Extractee != "Aucun":
                            listeDirectionsProbabilite = [[[0.25,0.25,0.25],[0,0,0],[-1,-1,-1]], [[-1,0,0.25],[-1,0,0.25],[-1,0,0.25]], [[-1,-1,-1],[0,0,0],[0.25,0.25,0.25]], [[0.25,0,-1],[0.25,0,-1],[0.25,0,-1]]]
                            listeDirectionsPlace = ["Sud", "Ouest", "Nord", "Est"]
                            for k in range(len(listeDirectionsPlace)):
                                if listeDirectionsPlace[k] == Vent_Extractee:
                                    Place = k
                            InfluenceVent = listeDirectionsProbabilite[Place][i+1][j+1]
                            #       Nord            Est             Sud                 Ouest
                            #[0.25][0.25][0.25] [-1][0][0.25]   [-1][-1][-1]        [0.25][0][-1]     
                            #[0]   [0]   [0]    [-1][0][0.25]   [0][0][0]           [0.25][0][-1]     
                            #[-1]  [-1]  [-1]   [-1][0][0.25]   [0.25][0.25][0.25]  [0.25][0][-1]   
                        ProbabiliteFeu = ProbabiliteFeu - ProbabiliteFeu * InfluenceMeteo + ProbabiliteFeu * InfluenceVent      #Proba = P-P*v+P*m
                        neighboursOnFire.append(ProbabiliteFeu)
                    else:
                        neighboursOnFire.append(0)
                    break
                break
    return neighboursOnFire

def La_Propagation_Feu(Liste_Cases, Meteo_Extractee, Vent_Extractee):
    Liste_Cases_Renfort = copy.deepcopy(Liste_Cases)
    for i in range (len(Liste_Cases)):
        for j in range (len(Liste_Cases)):
            if Liste_Cases[i][j]["etat"] == "Vierge" and Liste_Cases[i][j]["Biome"] != 2:
                neighboursOnFire = checkNeighbourOnFire(i, j, Liste_Cases_Renfort, Meteo_Extractee, Vent_Extractee)
                for k in range(len(neighboursOnFire)):
                    if (neighboursOnFire[k] != False) and (neighboursOnFire[k] > 0):
                        ProbabilityOnFire = (round(random.uniform(0,100),3))
                        if ProbabilityOnFire < neighboursOnFire[k]:
                            Liste_Cases[i][j]["etat"] = "Brule"
                            Liste_Cases[i][j]["Intensite du feu"] = 1
                            break
    return Liste_Cases
