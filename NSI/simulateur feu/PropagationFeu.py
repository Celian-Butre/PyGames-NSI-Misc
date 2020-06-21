import random,copy

def Commencer_Feu(startCoord_j, startCoord_i, Liste_Cases): # A refaire, avec une saisie en cliquant/qui verifie que la tuile n'est pas de leau
    if Liste_Cases[startCoord_i][startCoord_j]["Biome"] != 2:
        Liste_Cases[startCoord_i][startCoord_j]["Intensite du feu"] = 1
        Liste_Cases[startCoord_i][startCoord_j]["etat"] = "Brule"
    return Liste_Cases

def Progression_Braises(Liste_Cases):                   #intensiteMax : Plaine = 2, Foret = 4, Eau = 0, Maison = 8, Plantation = 4
    listeIntensiteMax = [2, 4, 0, 8, 4]
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

def checkNeighbourOnFire(coord_i,coord_j, Liste_Cases):
    neighboursOnFire = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            while True:
                try:
                    assert(coord_i + i < len(Liste_Cases))
                    assert(coord_i + i >= 0)
                    assert(coord_j + j < len(Liste_Cases))
                    assert(coord_i + i >= 0)
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
                    if IntensiteActuelle != 0:
                        neighboursOnFire.append(round(FacteurTerrain*FacteurDistance*(float(0.75)**(IntensiteMax - IntensiteActuelle)),3)) #P = N ∗ M ∗ (0.75)^(intensiteMax−k)
                    else:
                        neighboursOnFire.append(0)
                    break
                break
    return neighboursOnFire

def La_Propagation_Feu(Liste_Cases):
    Liste_Cases_Renfort = copy.deepcopy(Liste_Cases)
    for i in range (len(Liste_Cases)):
        for j in range (len(Liste_Cases)):
            if Liste_Cases[i][j]["etat"] == "Vierge" and Liste_Cases[i][j]["Biome"] != 2:
                neighboursOnFire = checkNeighbourOnFire(i, j, Liste_Cases_Renfort)
                for k in range(len(neighboursOnFire)):
                    if (neighboursOnFire[k] != False) and (neighboursOnFire[k] > 0):
                        ProbabilityOnFire = (round(random.uniform(0,100),3))
                        if ProbabilityOnFire < neighboursOnFire[k]:
                            Liste_Cases[i][j]["etat"] = "Brule"
                            Liste_Cases[i][j]["Intensite du feu"] = 1
                            break
    return Liste_Cases