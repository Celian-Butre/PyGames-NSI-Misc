# initialisation de tout
import time, pygame, sys, random, copy
from PropagationFeu import *
from GenerationTerrain import *
from Meteo import *

MeteoDuJour = "Grand_Soleil"
Meteo_Passe = []
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


# 0 "plaine", 1 "foret", 2 "eau", 3 "maison", 4 "plantation"
# "Vierge", "Brule", "Estompe", "Calcinee"
# "Grand_Soleil", "Nuages", "Pluie", "Foudre"

#affichage des choses hors simulation
def defaultAffichage(MeteoDuJour):
    #initialisation des variables
    global isPaused, readyToPauseOrPlay
    black = pygame.image.load("images/black.png")
    blackRect = black.get_rect()
    
    black2 = black
    black2Rect = blackRect
    
    forward = pygame.image.load("images/forward.png")
    forwardRect = forward.get_rect()
    
    backward = pygame.image.load("images/backward.png")
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
    
    #verifie si le bouton play/pause est clique
    if mousepressed and (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) <= (37.5*37.5):
        readyToPauseOrPlay = True
    
    if (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) > (37.5*37.5):
        readyToPauseOrPlay = False
        
    if mousepressed  == False and (((mousepos[0] - 937.5) * (mousepos[0] - 937.5)) + ((mousepos[1] - 137.5) * (mousepos[1] - 137.5))) <= (37.5*37.5) and readyToPauseOrPlay == True:
        readyToPauseOrPlay = False
        isPaused = not isPaused
    
    #initialisation du logo pause/play
    if isPaused == False:
        pauseOrPlay = pygame.image.load("images/pause.png")
    else:
        pauseOrPlay = pygame.image.load("images/play.png")
    
    pauseOrPlayRect = pauseOrPlay.get_rect()
    
    #initialisation des logo meteo
    if MeteoDuJour == "Grand_Soleil":
        logoMeteo = pygame.image.load("images/Grand_Soleil.png")
    if MeteoDuJour == "Nuages":
        logoMeteo = pygame.image.load("images/Nuages.png")
    if MeteoDuJour == "Pluie":
        logoMeteo = pygame.image.load("images/Pluie.png")
    if MeteoDuJour == "Foudre":
        logoMeteo = pygame.image.load("images/Foudre.png")
        
    logoMeteoRect = logoMeteo.get_rect()
    
    #emplacement des boutons et des contours et du logo meteo
    blackRect = blackRect.move(225, 0)
    black2Rect = black2Rect.move(850, 0)
    
    backwardRect = backwardRect.move(25, 100)
    forwardRect = forwardRect.move(125, 100)
    
    pauseOrPlayRect = pauseOrPlayRect.move(900, 100)
    
    logoMeteoRect = logoMeteoRect.move(0, 375)
    
    screen.blit(black, blackRect)
    screen.blit(black2, black2Rect)
    
    screen.blit(forward, forwardRect)
    screen.blit(backward, backwardRect)
    
    screen.blit(pauseOrPlay, pauseOrPlayRect)

    screen.blit(logoMeteo, logoMeteoRect)
#affichage du feu par dessu le terrain
def affichageFeu(iterations):
    #initialisation des variables
    feuM1 = pygame.image.load("images/feuMontee1.png")
    feuM1Rect = feuM1.get_rect()
    
    feuM2 = pygame.image.load("images/feuMontee2.png")
    feuM2Rect = feuM2.get_rect()
    
    feuM3 = pygame.image.load("images/feuMontee3.png")
    feuM3Rect = feuM3.get_rect()
    
    feuM4 = pygame.image.load("images/feuMontee4.png")
    feuM4Rect = feuM4.get_rect()
    
    feuM5 = pygame.image.load("images/feuMontee5.png")
    feuM5Rect = feuM5.get_rect()
    
    feuM6 = pygame.image.load("images/feuMontee6.png")
    feuM6Rect = feuM6.get_rect()
    
    feuM7 = pygame.image.load("images/feuMontee7.png")
    feuM7Rect = feuM7.get_rect()
    
    feuM8 = pygame.image.load("images/feuMontee8.png")
    feuM8Rect = feuM8.get_rect()
    
    feuD1 = pygame.image.load("images/feuDescente1.png")
    feuD1Rect = feuD1.get_rect()
    
    feuD2 = pygame.image.load("images/feuDescente2.png")
    feuD2Rect = feuD2.get_rect()
    
    feuD3 = pygame.image.load("images/feuDescente3.png")
    feuD3Rect = feuD3.get_rect()
    
    feuD4 = pygame.image.load("images/feuDescente4.png")
    feuD4Rect = feuD4.get_rect()
    
    feuD5 = pygame.image.load("images/feuDescente5.png")
    feuD5Rect = feuD5.get_rect()
    
    feuD6 = pygame.image.load("images/feuDescente6.png")
    feuD6Rect = feuD6.get_rect()
    
    feuD7 = pygame.image.load("images/feuDescente7.png")
    feuD7Rect = feuD7.get_rect()
    
    feuD8 = pygame.image.load("images/feuDescente8.png")
    feuD8Rect = feuD8.get_rect()
    
    pasFeu = pygame.image.load("images/pasFeu.png")
    pasFeuRect = pasFeu.get_rect()
    
    #creation d'une matrice de listes contenant la photo et le rectangle associe, en fonction du feu
    liste_Cases_Feu_Images = []
    for i in range (iterations):
        liste_Cases_Feu_Images.append([])
        for j in range (iterations):
            liste_Cases_Feu_Images[i].append([])
            #si l'etat est sans feu (et donc toujours l'eau), image du feu transparent
            if Liste_Cases[i][j]["etat"] == "Vierge" or Liste_Cases[i][j]["Biome"] == 2:
                liste_Cases_Feu_Images[i][j].append(pasFeu)
                liste_Cases_Feu_Images[i][j].append(pasFeuRect)
            #si le terrain est calcinee image calcine
            elif Liste_Cases[i][j]["etat"] == "Calcinee":
                liste_Cases_Feu_Images[i][j].append(feuD8)
                liste_Cases_Feu_Images[i][j].append(feuD8Rect)
            else:
                #si le terrain est une plaine
                if Liste_Cases[i][j]["Biome"] == 0:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "Brule":
                        #couleur du feu en fonction de l'intensite
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuM4)
                            liste_Cases_Feu_Images[i][j].append(feuM4Rect)
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "Estompe":
                        #couleur en fonction de l'intensite
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuD4)
                            liste_Cases_Feu_Images[i][j].append(feuD4Rect)
                #si le terrain est une foret ou une plantation
                if Liste_Cases[i][j]["Biome"] == 1 or Liste_Cases[i][j]["Biome"] == 4:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "Brule":
                        #couleur du feu en fonction de l'intensite
                        if Liste_Cases[i][j]["Intensite du feu"] == 1:
                            liste_Cases_Feu_Images[i][j].append(feuM2)
                            liste_Cases_Feu_Images[i][j].append(feuM2Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 2:
                            liste_Cases_Feu_Images[i][j].append(feuM4)
                            liste_Cases_Feu_Images[i][j].append(feuM4Rect)
                        if Liste_Cases[i][j]["Intensite du feu"] == 3:
                            liste_Cases_Feu_Images[i][j].append(feuM6)
                            liste_Cases_Feu_Images[i][j].append(feuM6Rect)
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "Estompe":
                        #couleur en fonction de l'intensite
                        if Liste_Cases[i][j]["Intensite du feu"] == 4:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
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
                if Liste_Cases[i][j]["Biome"] == 3:
                    #si imax pas atteinte
                    if Liste_Cases[i][j]["etat"] == "Brule":
                        #couleur du feu en fonction de l'intensite
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
                    #si imax atteinte
                    if Liste_Cases[i][j]["etat"] == "Estompe":
                        #couleur en fonction de l'intensite
                        if Liste_Cases[i][j]["Intensite du feu"] == 8:
                            liste_Cases_Feu_Images[i][j].append(feuM8)
                            liste_Cases_Feu_Images[i][j].append(feuM8Rect)
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
            #deplacement du rectangle
            if Liste_Cases[i][j]["etat"] == "Calcinee":
                liste_Cases_Feu_Images[i][j][1] = liste_Cases_Feu_Images[i][j][1].move(250+j*6,i*6)
            else:
                liste_Cases_Feu_Images[i][j][1] = liste_Cases_Feu_Images[i][j][1].move(251+j*6,1+i*6)
            # deplacement de l'image sur le rectangle
            screen.blit(liste_Cases_Feu_Images[i][j][0],liste_Cases_Feu_Images[i][j][1])
            
#affichage de la simulation            
def affichage(iterations):
    #initialisation des variables 
    brown = pygame.image.load("images/brown.png")
    brownRect = brown.get_rect()

    green = pygame.image.load("images/green.png")
    greenRect = green.get_rect()

    lime = pygame.image.load("images/lime.png")
    limeRect = lime.get_rect()

    blue = pygame.image.load("images/blue.png")
    blueRect = blue.get_rect()

    grey = pygame.image.load("images/grey.png")
    greyRect = grey.get_rect()
    
    #creation d'une matrice de listes contenant la photo et le rectangle associe, en fonction du biome
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
            #deplacement du rectangle
            liste_Cases_Images[i][j][1] = liste_Cases_Images[i][j][1].move(250+j*6,i*6)
            # deplacement de l'image sur le rectangle
            screen.blit(liste_Cases_Images[i][j][0],liste_Cases_Images[i][j][1])

Remplir_Grille_Initiale(Liste_Cases, iterations, waterDroplets, forestSeeds)
while True:
    #background blanc
    screen.fill (backgroundColor)
    #affichages des choses statiques
    defaultAffichage(MeteoDuJour)
    # delai pour raffraichir la simulation qu'une fois sur 10
    if wait10 >= 10:
        wait10 = 0
    if wait10 == 0 and isPaused == False:
        MeteoDuJour = Meteo_Extraction(Meteo_Sucession(Meteo_Passe))
        Liste_Case = Progression_Braises(Liste_Cases)
        Liste_Cases = La_Propagation_Feu(Liste_Cases, MeteoDuJour)
        Liste_Cases = Gestion_Foudre(MeteoDuJour, Liste_Cases)
    Liste_Cases = addFire(Liste_Cases)
    # affichage de la simulation
    affichage(iterations)
    # affichage du feu
    affichageFeu(iterations)
    pygame.display.flip()
    time.sleep(1/1000)
    wait10 += 5
