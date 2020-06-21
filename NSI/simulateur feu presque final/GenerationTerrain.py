import random, copy
def Creer_Grille (Liste_Cases, iterations):
    for i in range (iterations):
        Liste_Cases.append([])

def Creer_Case (iterations_2, biome_case, intensite_case, etat_case, Liste_Cases):
    dictionary = {"Biome" : biome_case, "Intensite du feu" : intensite_case, "etat" : etat_case}
    Liste_Cases[iterations_2].append(dictionary)

def checkNeighboursExist(coord_i,coord_j, Choixbiome):
    neighboursExist = []
    for i in range(-1,2,1):
        for j in range(-1,2,1):
            while True:
                try:
                    assert(coord_i + i < len(Choixbiome))
                    assert(coord_i + i >= 0)
                    assert(coord_j + j < len(Choixbiome))
                    assert(coord_i + i >= 0)
                except AssertionError:
                    neighboursExist.append(0)
                    break
                neighboursExist.append(1)
                break
    return neighboursExist

def seedToForest(Choixbiome, iterations, forestSeeds, pourcentage_foret):
    cptForet = 0
    for i in range (forestSeeds):
        Choixbiome[random.randint(0,iterations-1)][random.randint(0,iterations-1)]= 1
        cptForet += 1
    while cptForet < ((pourcentage_foret)*iterations*iterations):
        forestStorage = copy.deepcopy(Choixbiome)
        for i in range(iterations):
            for j in range(iterations):
                if forestStorage[i][j] == 1:
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    for k in range(len(neighboursExist)):
                        randomNumberChoice = random.randint(1,10)
                        if (randomNumberChoice > 6 and neighboursExist[k] == 1):
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] == 0:
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 1
                                cptForet += 1
    return Choixbiome

def dropToLake(Choixbiome, iterations, waterDroplets, pourcentage_lac):
    cptLac = 0
    for i in range (waterDroplets):
        randomNumber1 = random.randint(0,iterations-1)
        randomNumber2 = random.randint(0,iterations-1)
        try:
            assert(Choixbiome[randomNumber1][randomNumber2] != 1)
        except AssertionError:
            randomNumber1 = random.randint(0,iterations-1)
            randomNumber2 = random.randint(0,iterations-1)
        Choixbiome[randomNumber1][randomNumber2] = 2
        cptLac += 1
    while cptLac < ((pourcentage_lac)*iterations*iterations):
        lakeStorage = copy.deepcopy(Choixbiome)
        for i in range(iterations):
            for j in range(iterations):
                if lakeStorage[i][j] == 2:
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    for k in range(len(neighboursExist)):
                        randomNumberChoice = random.randint(1,10)
                        if (randomNumberChoice > 6) and (neighboursExist[k] == 1):
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] == 0:
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 2
                                cptLac += 1
    return Choixbiome

def makeSomeHouses(Choixbiome, iterations, howManyHouses):
    for i in range (howManyHouses):
        randomNumber1 = random.randint(0,iterations-1)
        randomNumber2 = random.randint(0,iterations-1)
        try:
            assert(Choixbiome[randomNumber1][randomNumber2] != 2)
        except AssertionError:
            randomNumber1 = random.randint(0,iterations-1)
            randomNumber2 = random.randint(0,iterations-1)
        Choixbiome[randomNumber1][randomNumber2] = 3
    return Choixbiome

def housesHavePlantations(Choixbiome, iterations, pourcentage_plantation):
    cptPlantation = 0
    while cptPlantation < ((pourcentage_plantation)*iterations*iterations):
        plantationStorage = copy.deepcopy(Choixbiome)
        for i in range(iterations):
            for j in range(iterations):
                if plantationStorage[i][j] == 3 or plantationStorage[i][j] == 4:
                    neighboursExist = checkNeighboursExist(i,j,Choixbiome)
                    neighbourPositions = [[i-1,j-1],[i-1,j],[i-1,j+1],[i,j-1],[i,j],[i,j+1],[i+1,j-1],[i+1,j],[i+1,j+1]]
                    for k in range(len(neighboursExist)):
                        randomNumberChoice = random.randint(1,10)
                        if (randomNumberChoice > 6 and neighboursExist[k] == 1):
                            if Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] != 3:
                                Choixbiome[neighbourPositions[k][0]][neighbourPositions[k][1]] = 4
                                cptPlantation += 1
    return Choixbiome
    
def Choixbiome(iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation):
    Choixbiome=[] 
    for i in range (iterations):
        Choixbiome.append([])
        for j in range (iterations):
            Choixbiome[i].append(0)
    Choixbiome = seedToForest(Choixbiome, iterations, forestSeeds, pourcentage_foret)
    Choixbiome = dropToLake(Choixbiome, iterations, waterDroplets, pourcentage_lac)
    Choixbiome = makeSomeHouses(Choixbiome, iterations, howManyHouses)
    Choixbiome = housesHavePlantations(Choixbiome, iterations, pourcentage_plantation)
    return Choixbiome

def Remplir_Grille_Initiale(Liste_Cases, iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation):
    Creer_Grille(Liste_Cases, iterations)
    choix_Biome = Choixbiome(iterations, waterDroplets, forestSeeds, pourcentage_foret, pourcentage_lac, howManyHouses, pourcentage_plantation)
    for j in range(iterations):
        for i in range(iterations):
            Creer_Case (j,choix_Biome[i][j], 0, "Vierge", Liste_Cases)
