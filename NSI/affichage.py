# initialisation de tout
import time, pygame, sys, random, copy
pygame.init
width, height = 1100, 600
backgroundColor = 255, 255, 255
pygame.display.set_caption("simulateur_feu")

screen = pygame.display.set_mode((width, height))

wait10 = 0
iterations = 100
Liste_Cases = []
waterDroplets = iterations//3
forestSeeds = iterations//7
isPaused = True
readyToPauseOrPlay = False

def Creer_Grille (iterations):
    for i in range (iterations):
        Liste_Cases.append([])

def Creer_Case (iterations_2, biome_case, intensite_case, etat_case):
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

def seedToForest(Choixbiome, iterations, forestSeeds):
    cptForet = 0
    for i in range (forestSeeds):
        Choixbiome[random.randint(0,iterations-1)][random.randint(0,iterations-1)]= 1
        cptForet += 1
    while cptForet < ((50/100)*iterations*iterations):
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

def dropToLake(Choixbiome, iterations, waterDroplets):
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
    while cptLac < ((25/100)*iterations*iterations):
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

def housesHavePlantations(Choixbiome, iterations):
    cptPlantation = 0
    while cptPlantation < ((5/100)*iterations*iterations):
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

#def checkFinalGeneration(iterations, Choixbiome):
    
def Choixbiome(iterations, waterDroplets, forestSeeds):
    Choixbiome=[] 
    for i in range (iterations):
        Choixbiome.append([])
        for j in range (iterations):
            Choixbiome[i].append(0)
    Choixbiome = seedToForest(Choixbiome, iterations, forestSeeds)
    Choixbiome = dropToLake(Choixbiome, iterations, waterDroplets)
    Choixbiome = makeSomeHouses(Choixbiome, iterations, 10)
    Choixbiome = housesHavePlantations(Choixbiome, iterations)
    return Choixbiome

def Remplir_Grille_Initiale(iterations, waterDroplets, forestSeeds):
    Creer_Grille(iterations)
    choix_Biome = Choixbiome(iterations, waterDroplets, forestSeeds )
    for j in range(iterations):
        for i in range(iterations):
            Creer_Case (j,choix_Biome[i][j], 0, "c trkl")



# 0 "plaine", 1 "foret", 2 "plantation", 3 "eau", 4 "maison"
# "c trkl", "chauffe", "refroidi", "brulé"

#affichage des choses hors simulation
def defaultAffichage():
    #initialisation des variables
    global isPaused, readyToPauseOrPlay
    black = pygame.image.load("black.png")
    blackRect = black.get_rect()
    
    black2 = black
    black2Rect = blackRect
    
    forward = pygame.image.load("forward.png")
    forwardRect = forward.get_rect()
    
    backward = pygame.image.load("backward.png")
    backwardRect = backward.get_rect()
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
    
    #vérifie si le bouton play/pause est cliqué
    if mousepressed and (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) <= (37.5*37.5):
        readyToPauseOrPlay = True
    
    if (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) > (37.5*37.5):
        readyToPauseOrPlay = False
        
    if mousepressed  == False and (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) <= (37.5*37.5) and readyToPauseOrPlay == True:
        readyToPauseOrPlay = False
        isPaused = not isPaused
    
    #initialisation du logo pause/play
    if isPaused == False:
        pauseOrPlay = pygame.image.load("pause.png")
    else:
        pauseOrPlay = pygame.image.load("play.png")
    
    pauseOrPlayRect = pauseOrPlay.get_rect()
    
    #emplacement des boutons et des contours
    blackRect = blackRect.move(225, 0)
    black2Rect = black2Rect.move(850, 0)
    
    backwardRect = backwardRect.move(25, 100)
    forwardRect = forwardRect.move(125, 100)
    
    pauseOrPlayRect = pauseOrPlayRect.move(900, 100)
    
    screen.blit(black, blackRect)
    screen.blit(black2, black2Rect)
    
    screen.blit(forward, forwardRect)
    screen.blit(backward, backwardRect)
    
    screen.blit(pauseOrPlay, pauseOrPlayRect)

#affichage du feu par dessu le terrain
def affichageFeu(iterations):
    #initialisation des variables
    feuM1 = pygame.image.load("feuMontée1.png")
    feuM1Rect = feuM1.get_rect()
    
    feuM2 = pygame.image.load("feuMontée2.png")
    feuM2Rect = feuM2.get_rect()
    
    feuM3 = pygame.image.load("feuMontée3.png")
    feuM3Rect = feuM3.get_rect()
    
    feuM4 = pygame.image.load("feuMontée4.png")
    feuM4Rect = feuM4.get_rect()
    
    feuM5 = pygame.image.load("feuMontée5.png")
    feuM5Rect = feuM5.get_rect()
    
    feuM6 = pygame.image.load("feuMontée6.png")
    feuM6Rect = feuM6.get_rect()
    
    feuM7 = pygame.image.load("feuMontée7.png")
    feuM7Rect = feuM7.get_rect()
    
    feuM8 = pygame.image.load("feuMontée8.png")
    feuM8Rect = feuM8.get_rect()
    
    feuD1 = pygame.image.load("feuDescente1.png")
    feuD1Rect = feuD1.get_rect()
    
    feuD2 = pygame.image.load("feuDescente2.png")
    feuD2Rect = feuD2.get_rect()
    
    feuD3 = pygame.image.load("feuDescente3.png")
    feuD3Rect = feuD3.get_rect()
    
    feuD4 = pygame.image.load("feuDescente4.png")
    feuD4Rect = feuD4.get_rect()
    
    feuD5 = pygame.image.load("feuDescente5.png")
    feuD5Rect = feuD5.get_rect()
    
    feuD6 = pygame.image.load("feuDescente6.png")
    feuD6Rect = feuD6.get_rect()
    
    feuD7 = pygame.image.load("feuDescente7.png")
    feuD7Rect = feuD7.get_rect()
    
    feuD8 = pygame.image.load("feuDescente8.png")
    feuD8Rect = feuD8.get_rect()
    
    pasFeu = pygame.image.load("pasFeu.png")
    pasFeuRect = pasFeu.get_rect()
    
    #création d'une matrice de listes contenant la photo et le rectangle associé, en fonction du feu
    liste_Cases_Feu_Images = []
    for i in range (iterations):
        liste_Cases_Feu_Images.append([])
        for j in range (iterations):
            liste_Cases_Feu_Images[i].append([])
            #si l'état est sans feu (et donc toujours l'eau), image du feu transparent
            if Liste_Cases[i][j]["etat"] == "c trkl":
                liste_Cases_Feu_Images[i][j].append(pasFeu)
                liste_Cases_Feu_Images[i][j].append(pasFeuRect)
            #si le terrain est brulé image brulé
            elif Liste_Cases[i][j]["etat"] == "brulé":
                liste_Cases_Feu_Images[i][j].append(feuD8)
                liste_Cases_Feu_Images[i][j].append(feuD8Rect)
            else:
                #si le terrain est une plaine
                if Liste_Cases[i][j]["Biome"] == 0:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "chauffe":
                        #couleur du feu en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuM4)
                            liste_Cases_Feu_Images[i][j].append(feuM4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "refroidi":
                        #couleur en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuD4)
                            liste_Cases_Feu_Images[i][j].append(feuD4Rect)
                #si le terrain est une foret ou une plantation
                if Liste_Cases[i][j]["Biome"] == 1 or Liste_Cases[i][j]["Biome"] == 2:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "chauffe":
                        #couleur du feu en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuM2)
                            liste_Cases_Feu_Images[i][j].append(feuM2Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuM4)
                            liste_Cases_Feu_Images[i][j].append(feuM4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 3:
                            liste_Cases_Feu_Images[i][j].append(feuM6)
                            liste_Cases_Feu_Images[i][j].append(feuM6Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 4:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "refroidi":
                        #couleur en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 3:
                            liste_Cases_Feu_Images[i][j].append(feuD2)
                            liste_Cases_Feu_Images[i][j].append(feuD2Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuD4)
                            liste_Cases_Feu_Images[i][j].append(feuD4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuD6)
                            liste_Cases_Feu_Images[i][j].append(feuD6Rect)
                #si le terrain est une maison
                if Liste_Cases[i][j]["Biome"] == 4:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "chauffe":
                        #couleur du feu en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuM1)
                            liste_Cases_Feu_Images[i][j].append(feuM1Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuM2)
                            liste_Cases_Feu_Images[i][j].append(feuM2Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 3:
                            liste_Cases_Feu_Images[i][j].append(feuM3)
                            liste_Cases_Feu_Images[i][j].append(feuM3Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 4:
                            liste_Cases_Feu_Images[i][j].append(feuM4)
                            liste_Cases_Feu_Images[i][j].append(feuM4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 5:
                            liste_Cases_Feu_Images[i][j].append(feuM5)
                            liste_Cases_Feu_Images[i][j].append(feuM5Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 6:
                            liste_Cases_Feu_Images[i][j].append(feuM6)
                            liste_Cases_Feu_Images[i][j].append(feuM6Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 7:
                            liste_Cases_Feu_Images[i][j].append(feuM7)
                            liste_Cases_Feu_Images[i][j].append(feuM7Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 8:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "refroidi":
                        #couleur en fonction de l'intensité
                        if Liste_Cases[i][j]["Intensite du feu"] == 7:
                            liste_Cases_Feu_Images[i][j].append(feuD1)
                            liste_Cases_Feu_Images[i][j].append(feuD1Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 6:
                            liste_Cases_Feu_Images[i][j].append(feuD2)
                            liste_Cases_Feu_Images[i][j].append(feuD2Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 5:
                            liste_Cases_Feu_Images[i][j].append(feuD3)
                            liste_Cases_Feu_Images[i][j].append(feuD3Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 4:
                            liste_Cases_Feu_Images[i][j].append(feuD4)
                            liste_Cases_Feu_Images[i][j].append(feuD4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 3:
                            liste_Cases_Feu_Images[i][j].append(feuD5)
                            liste_Cases_Feu_Images[i][j].append(feuD5Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuD6)
                            liste_Cases_Feu_Images[i][j].append(feuD6Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuD7)
                            liste_Cases_Feu_Images[i][j].append(feuD7Rect)
            #déplacement du rectangle
            liste_Cases_Feu_Images[i][j][1] = liste_Cases_Feu_Images[i][j][1].move(252+j*6,2+i*6)
            # déplacement de l'image sur le rectangle
            screen.blit(liste_Cases_Feu_Images[i][j][0],liste_Cases_Feu_Images[i][j][1])
            
#affichage de la simulation            
def affichage(iterations):
    #initialisation des variables 
    brown = pygame.image.load("brown.png")
    brownRect = brown.get_rect()

    green = pygame.image.load("green.png")
    greenRect = green.get_rect()

    lime = pygame.image.load("lime.png")
    limeRect = lime.get_rect()

    blue = pygame.image.load("blue.png")
    blueRect = blue.get_rect()

    grey = pygame.image.load("grey.png")
    greyRect = grey.get_rect()
    
    #création d'une matrice de listes contenant la photo et le rectangle associé, en fonction du biome
    liste_Cases_Images = []
    for i in range (iterations):
        liste_Cases_Images.append([])
        for j in range (iterations):
            liste_Cases_Images[i].append([])
            if Liste_Cases[i][j]["Biome"] == 0:
                liste_Cases_Images[i][j].append(brown)
                liste_Cases_Images[i][j].append(brownRect)
            if Liste_Cases[i][j]["Biome"] == 1:
                liste_Cases_Images[i][j].append(green)
                liste_Cases_Images[i][j].append(greenRect)
            if Liste_Cases[i][j]["Biome"] == 2:
                liste_Cases_Images[i][j].append(blue)
                liste_Cases_Images[i][j].append(blueRect)
            if Liste_Cases[i][j]["Biome"] == 3:
                liste_Cases_Images[i][j].append(grey)
                liste_Cases_Images[i][j].append(greyRect)
            if Liste_Cases[i][j]["Biome"] == 4:
                liste_Cases_Images[i][j].append(lime)
                liste_Cases_Images[i][j].append(limeRect)
            #déplacement du rectangle
            liste_Cases_Images[i][j][1] = liste_Cases_Images[i][j][1].move(250+j*6,i*6)
            # déplacement de l'image sur le rectangle
            screen.blit(liste_Cases_Images[i][j][0],liste_Cases_Images[i][j][1])

Remplir_Grille_Initiale(iterations, waterDroplets, forestSeeds)
while True:
    #background blanc
    screen.fill (backgroundColor)
    #affichages des choses statiques
    defaultAffichage()
    # délai pour raffraichir la simulation qu'une fois sur 10
    if wait10 >= 10:
        wait10 = 0
    if wait10 == 0 and isPaused == False:
        Liste_Cases = []
        Remplir_Grille_Initiale(iterations, waterDroplets, forestSeeds)
    # affichage de la simulation
    affichage(iterations)
    # affichage du feu
    affichageFeu(iterations)
    pygame.display.flip()
    time.sleep(1/1000)
    wait10 += 1