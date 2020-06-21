import time, pygame, sys, random
pygame.init()
width, height = 700, 700
backgroundColor = 255, 255, 255
dvdLogoSpeed = [1,  1]  
white = 255, 255, 255
black = 0, 0, 0

screen = pygame. display.set_mode((width, height))

despourRelancer = [0, 0, 0, 0, 0]
listedeDes = [1, 1, 1, 1, 1]

contrat = []

queue1 = False
queue2 = False
queue3 = False
queue4 = False
queue5 = False

queuethrow = False
queueskipthrow = False
queuedone = False

border1 = False
border2 = False
border3 = False
border4 = False
border5 = False

firstthrow = False

redrectangle2 = pygame.image.load("redrectangle2.png")
redrectangle2Rect = redrectangle2.get_rect()
redrectangle2Rect = redrectangle2Rect.move(0, 90)

bluerectangle = pygame.image.load("bluerectangle.png")
bluerectangleRect = bluerectangle.get_rect()
bluerectangleRect = bluerectangleRect.move(100, 150)

greenrectangle = pygame.image.load("greenrectangle.png")
greenrectangleRect = greenrectangle.get_rect()
greenrectangleRect = greenrectangleRect.move(400, 150)


font = pygame.font.Font('freesansbold.ttf', 35)  
textjoueur1 = font.render('1 player', True, black)
textou = font.render('or', True, black)
textjoueur2 = font.render('2 players', True, black)

textjoueur1Rect = textjoueur1.get_rect()
textouRect = textou.get_rect()
textjoueur2Rect = textjoueur2.get_rect()

textjoueur1Rect = textjoueur1Rect.move(115, 330)
textouRect = textouRect.move(325, 390)
textjoueur2Rect = textjoueur2Rect.move(415, 330)

dice1Red = pygame.image.load("redrectangle.png")
dice2Red = pygame.image.load("redrectangle.png")
dice3Red = pygame.image.load("redrectangle.png")
dice4Red = pygame.image.load("redrectangle.png")
dice5Red = pygame.image.load("redrectangle.png")

dice1 = pygame.image.load("dice1.png")
dice2 = pygame.image.load("dice2.png")
dice3 = pygame.image.load("dice3.png")
dice4 = pygame.image.load("dice4.png")
dice5 = pygame.image.load("dice5.png")

scoresheet = pygame.image.load("scoresheet.png")

bluecircle = pygame.image.load("bluecircle.png")
redcircle = pygame.image.load("redcircle.png")
greencircle = pygame.image.load("greencircle.png")



dice1RedRect = dice1Red.get_rect()
dice2RedRect = dice2Red.get_rect()
dice3RedRect = dice3Red.get_rect()
dice4RedRect = dice4Red.get_rect()
dice5RedRect = dice5Red.get_rect()


dice1Rect = dice1.get_rect()
dice2Rect = dice2.get_rect()
dice3Rect = dice3.get_rect()
dice4Rect = dice4.get_rect()
dice5Rect = dice5.get_rect()

scoresheetRect = scoresheet.get_rect()

bluecircleRect = bluecircle.get_rect()
redcircleRect = redcircle.get_rect()
greencircleRect = greencircle.get_rect()

dice1RedRect = dice1RedRect.move(495, 165)
dice2RedRect = dice2RedRect.move(395, 240)
dice3RedRect = dice3RedRect.move(495, 315)
dice4RedRect = dice4RedRect.move(395, 390)
dice5RedRect = dice5RedRect.move(495, 465)

dice1Rect = dice1Rect.move(500, 170)
dice2Rect = dice2Rect.move(400, 245)
dice3Rect = dice3Rect.move(500, 320)
dice4Rect = dice4Rect.move(400, 395)
dice5Rect = dice5Rect.move(500, 470)

scoresheetRect = scoresheetRect.move(5, 95)

bluecircleRect = bluecircleRect.move(100, 0)
redcircleRect = redcircleRect.move(310, 0)
greencircleRect = greencircleRect.move(520, 0)

font = pygame.font.Font('freesansbold.ttf', 22)  
text1 = font.render('done', True, black) 
text2 = font.render('skip', True, black)
text2_5 = font.render('throws', True, black)
text3 = font.render('throw', True, black) 

text1Rect = text1.get_rect()  
text2Rect = text2.get_rect()  
text2_5Rect = text2_5.get_rect()
text3Rect = text3.get_rect()  

text1Rect = text1Rect.move(115, 29)
text2Rect = text2Rect.move(325, 14)
text2_5Rect = text2_5Rect.move(315, 38)
text3Rect = text3Rect.move(530, 29)

def startprogram():
    global joueurs
    playerschosen = False
    screen.fill(backgroundColor)    
    screen.blit(bluerectangle, bluerectangleRect)
    screen.blit(greenrectangle, greenrectangleRect)
    screen.blit(textjoueur1, textjoueur1Rect)
    screen.blit(textou, textouRect)
    screen.blit(textjoueur2, textjoueur2Rect)
    pygame.display.flip()
    time.sleep(1000/1000)
    while playerschosen == False:
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
        screen.fill(backgroundColor)    
        screen.blit(bluerectangle, bluerectangleRect)
        screen.blit(greenrectangle, greenrectangleRect)
        screen.blit(textjoueur1, textjoueur1Rect)
        screen.blit(textou, textouRect)
        screen.blit(textjoueur2, textjoueur2Rect)
        pygame.display.flip()
        
        if mousepos[0] >= 100 and mousepos[0] <= 300 and mousepressed == True and mousepos[1] >= 150 and mousepos[1] <= 550:
            joueurs = 1
            playerschosen = True
        if mousepos[0] >= 400 and mousepos[0] <= 600 and mousepressed == True and mousepos[1] >= 150 and mousepos[1] <= 550:
            joueurs = 2
            playerschosen = True

def sommeValeur(val):
    global listedeDes
    total = 0
    for i in range(5):
        if listedeDes[i] == val:
            total += val
    return (total)

def somme():
    global listedeDes
    total = 0
    for i in range(5):
        total += listedeDes[i]
    return(total)



#verifie si les dés forment un brelan
def estBrelan():
    global listedeDes
    Brelan = False
    for i in range(1,7):
        totaldeceDes = 0
        for j in range (5):
            if listedeDes[j] == i:
                totaldeceDes += 1
                if totaldeceDes == 3:
                    Brelan = True
    return (Brelan)

#verifie si les dés forment un carre
def estCarre():
    global listedeDes
    Carre = False
    for i in range(1,7):
        totaldeceDes = 0
        for j in range (5):
            if listedeDes[j] == i:
                totaldeceDes += 1
                if totaldeceDes == 4:
                    Carre = True
    return (Carre)

#verifie si les dés forment un full
def estFull():
    global listedeDes
    Brelan = False
    listedetriple = []
    for i in range(1,7):
        totaldeceDes = 0
        posdutriple = []
        for j in range (5):
            if listedeDes[j] == i:
                posdutriple.append(j)
                totaldeceDes += 1
                if totaldeceDes == 3:
                    Brelan = True
                    tripleDes = i
                    for l in range (3):
                        listedetriple.append(posdutriple[l]+1)
    pospasdutriple = []
    if Brelan == True:
        for i in range (1, 6):
            if i != listedetriple[0] and i != listedetriple[1] and i != listedetriple[2]:
                pospasdutriple.append(i)
        if listedeDes[pospasdutriple[0]-1] == listedeDes[pospasdutriple[1]-1] and listedeDes[pospasdutriple[0]-1] != listedeDes[listedetriple[0]-1]:
            Full = True
        else:
            Full = False
    else:
        Full = False
    return (Full)

#verifie si les dés forment un Yams
def estYams():
    global listedeDes
    Yams = False
    for i in range(1,7):
        totaldeceDes = 0
        for j in range (5):
            if listedeDes[j] == i:
                totaldeceDes += 1
                if totaldeceDes == 5:
                    Yams = True
    return (Yams)





#verifie si les dés forment une petite suite
def estPetiteSuite():
    global listedeDes
    listenplus = []
    if (listedeDes[0] == 1 and listedeDes[1] == 2 and listedeDes[2] == 3 and listedeDes[3] == 4) or (listedeDes[1] == 3 and listedeDes[2] == 4 and listedeDes[3] == 5 and listedeDes[4] == 6):
        return (True)
    last = 0
    for i in range(5):
        if listedeDes[i] != last:
            listenplus.append(listedeDes[i])
            last = listedeDes[i]
    if len(listenplus) < 4:
        return(False)
    petiteSuite = True
    for i in range(3):
        if listenplus[i] != listenplus[i+1] - 1:
            petiteSuite = False
    return(petiteSuite)

#verifie si les dés forment une grande suite
def estGrandeSuite():
    global listedeDes
    grandeSuite = True
    for i in range(4):
        if listedeDes[i] != listedeDes[i+1] - 1:
            grandeSuite = False
    return(grandeSuite)

def trierDes(trierl):
    for i in range(len(trierl)):
        for j in range(len(trierl)-i-1):
            if trierl[j] > trierl[j+1]:
                save = trierl[j]
                trierl[j] = trierl[j+1]
                trierl[j+1] = save
    return(trierl)

def creerGrille(player):
    global contrat
    contrat = []
    for i in range(player):
        contrat.append([ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
        
def afficherContrat(doflip):
    global contrat, joueur
    listeText = []
    listeTextRect = []
    font = pygame.font.Font('freesansbold.ttf', 22)   
    for i in range(13):
        listeText.append(font.render(str((contrat[joueur-1][i])), True, black))
        listeTextRect.append(listeText[i].get_rect())
        if i < 6:
            listeTextRect[i] = listeTextRect[i].move(227, (150 + (i) * 28))
        if i >= 6:
            listeTextRect[i] = listeTextRect[i].move(227, (425 + (i-6) * 27))
    toptotal = 0
    for i in range(6):
        if contrat[joueur-1][i] != -1:
            toptotal += contrat[joueur-1][i]
    toptotalText = font.render(str(toptotal), True, black)
    toptotalTextRect = toptotalText.get_rect()
    toptotalTextRect = toptotalTextRect.move(220, 318)
    screen.blit(toptotalText, toptotalTextRect)
    
    topbonusText = font.render('35', True, black)
    topbonusTextRect = topbonusText.get_rect()
    topbonusTextRect = topbonusTextRect.move(220, 340)
    
    topbonus = 0
    if toptotal >= 63:
        screen.blit(topbonusText,topbonusTextRect)
        topbonus = 35
        
    
    toptotaltotalText = font.render(str(toptotal + topbonus), True, black)
    toptotaltotalTextRect = toptotaltotalText.get_rect()
    toptotaltotalTextRect = toptotaltotalTextRect.move(220, 365)
    screen.blit(toptotaltotalText, toptotaltotalTextRect)
    
    bottomtotal = 0
    for i in range(7):
        if contrat[joueur-1][i+6] != -1:
            bottomtotal += contrat[joueur-1][i+6]
    
    bottomtotalText = font.render(str(bottomtotal), True, black)
    bottomtotalTextRect = bottomtotalText.get_rect()
    bottomtotalTextRect = bottomtotalTextRect.move(220, 616)
    screen.blit(bottomtotalText, bottomtotalTextRect)
        
    toptotaltotal2Text = font.render(str(toptotal + topbonus), True, black)
    toptotaltotal2TextRect = toptotaltotal2Text.get_rect()
    toptotaltotal2TextRect = toptotaltotal2TextRect.move(220, 644)
    screen.blit(toptotaltotal2Text,toptotaltotal2TextRect)
    
    totalText = font.render(str(toptotal + bottomtotal), True, black)
    totalTextRect = totalText.get_rect()
    totalTextRect = totalTextRect.move(220, 670)
    screen.blit(totalText, totalTextRect)
                
    for i in range(13):
        if contrat[joueur-1][i] != -1:
            screen.blit(listeText[i], listeTextRect[i])
    if doflip == True:
        pygame.display.flip()
            
            
    
def choisirContrat():
    global done, mousepressed, mousepos, listedeDes, joueur, contrat, border1, border2, border3, border4, border5
    listedeDes = trierDes(listedeDes)
    finished = False
    entered = False
    border1 = False
    border2 = False
    border3 = False
    border4 = False
    border5 = False
    doborders()
    while finished == False:
        done = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        contratnumber = -1
        for i in range (6):
            if mousepos[1] > (145 + i * 28) and mousepos[1] <= (145 + (i+1) * 28) and mousepos[0] > 210 and mousepos[0] <= 260:
                contratnumber = i+1
        for i in range(7):
            if mousepos[1] > (420 + i * 27) and mousepos[1] <= (420 + (i+1) * 27) and mousepos[0] > 210 and mousepos[0] <= 260:
                contratnumber = i+7
            
        checkdone()
        
        if done == True and entered == True:
            finished = True
        
        screen.blit(dice1Red, dice1RedRect)
        screen.blit(dice2Red, dice2RedRect)
        screen.blit(dice3Red, dice3RedRect)
        screen.blit(dice4Red, dice4RedRect)
        screen.blit(dice5Red, dice5RedRect)    

        screen.blit(dice1, dice1Rect)
        screen.blit(dice2, dice2Rect)
        screen.blit(dice3, dice3Rect)
        screen.blit(dice4, dice4Rect)
        screen.blit(dice5, dice5Rect)
        
        screen.blit(redrectangle2, redrectangle2Rect)
        screen.blit(scoresheet, scoresheetRect)
    
        screen.blit(bluecircle, bluecircleRect)
        screen.blit(redcircle, redcircleRect)
        screen.blit(greencircle, greencircleRect)
    
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(text2_5, text2_5Rect)
        screen.blit(text3, text3Rect)
        screen.blit(textplayernumb, textplayernumbRect)
        
        inOne = True
        if contratnumber > 0 and contratnumber < 7 and contrat[joueur-1][contratnumber-1] == -1:
            points = sommeValeur(contratnumber) 
            font = pygame.font.Font('freesansbold.ttf', 22)   
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (150 + (contratnumber-1) * 28))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 7 and contrat[joueur-1][contratnumber-1] == -1:
            brelan = estBrelan()
            if brelan == True:
                points = somme()
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 8 and contrat[joueur-1][contratnumber-1] == -1:
            carre = estCarre()
            if carre == True:
                points = somme()      
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect) 
        elif contratnumber == 9 and contrat[joueur-1][contratnumber-1] == -1:
            full = estFull()
            if full == True:
                points = 25      
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 10 and contrat[joueur-1][contratnumber-1] == -1:
            petitesuite = estPetiteSuite()
            if petitesuite == True:
                points = 30      
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 11 and contrat[joueur-1][contratnumber-1] == -1:
            grandesuite = estGrandeSuite()
            if grandesuite == True:
                points = 40      
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 12 and contrat[joueur-1][contratnumber-1] == -1:
            Yams = estYams()
            if Yams == True:
                points = 50      
            else:
                points = 0
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        elif contratnumber == 13 and contrat[joueur-1][contratnumber-1] == -1:
            points = somme()
            font = pygame.font.Font('freesansbold.ttf', 22) 
            tempText = font.render(str(points), True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(227, (425 + (contratnumber-7) * 27))
            screen.blit(tempText, tempTextRect)
        else:
            font = pygame.font.Font('freesansbold.ttf', 22)   
            tempText = font.render("0", True, black)
            tempTextRect = tempText.get_rect()  
            tempTextRect = tempTextRect.move(-100, -100)
            screen.blit(tempText, tempTextRect)
            inOne = False
        
        
        if inOne == True and mouse[0] == 1 and entered == False and contrat[joueur-1][contratnumber-1] == -1:
            contrat[joueur-1][contratnumber-1] = points
            entered = True
        
        afficherContrat(True)
            
        
        
        
        
        pygame.display.flip()
        
        

def jouerTour():
    global skip, listedeDes, despourRelancer, firstthrow, throwexecuted, mousepressed, mousepos, mouse
    skip = False
    screen.blit(dice1Red, dice1RedRect)
    screen.blit(dice2Red, dice2RedRect)
    screen.blit(dice3Red, dice3RedRect)
    screen.blit(dice4Red, dice4RedRect)
    screen.blit(dice5Red, dice5RedRect)    

    screen.blit(dice1, dice1Rect)
    screen.blit(dice2, dice2Rect)
    screen.blit(dice3, dice3Rect)
    screen.blit(dice4, dice4Rect)
    screen.blit(dice5, dice5Rect)
    
    screen.blit(scoresheet, scoresheetRect)
    
    screen.blit(bluecircle, bluecircleRect)
    screen.blit(redcircle, redcircleRect)
    screen.blit(greencircle, greencircleRect)
    
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.blit(text2_5, text2_5Rect)
    screen.blit(text3, text3Rect)
    screen.blit(textplayernumb, textplayernumbRect)
    
    afficherContrat(True)
    time.sleep(2000/1000)
    despourRelancer = [1, 1, 1, 1, 1]
    firstthrow = True
    afficherContrat(True)
    checkthrow()
    firstthrow = False
    despourRelancer = [0, 0, 0, 0, 0]
    throwexecuted = False
    while skip == False and throwexecuted == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        if mouse[0] == 1:
            mousepressed = True
        else:
            mousepressed = False
        
        doborders()
        checkthrow()
        checkskipthrow()
    
        screen.blit(dice1Red, dice1RedRect)
        screen.blit(dice2Red, dice2RedRect)
        screen.blit(dice3Red, dice3RedRect)
        screen.blit(dice4Red, dice4RedRect)
        screen.blit(dice5Red, dice5RedRect)    

        screen.blit(dice1, dice1Rect)
        screen.blit(dice2, dice2Rect)
        screen.blit(dice3, dice3Rect)
        screen.blit(dice4, dice4Rect)
        screen.blit(dice5, dice5Rect)
    
        screen.blit(scoresheet, scoresheetRect)
    
        screen.blit(bluecircle, bluecircleRect)
        screen.blit(redcircle, redcircleRect)
        screen.blit(greencircle, greencircleRect)
    
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(text2_5, text2_5Rect)
        screen.blit(text3, text3Rect)
        screen.blit(textplayernumb, textplayernumbRect)
        
        afficherContrat(True)
        
        pygame.display.flip()
        time.sleep(50 / 1000)
        
    throwexecuted = False
    while skip == False and throwexecuted == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        if mouse[0] == 1:
            mousepressed = True
        else:
            mousepressed = False
        
        doborders()
        checkthrow()
        checkskipthrow()
    
        screen.blit(dice1Red, dice1RedRect)
        screen.blit(dice2Red, dice2RedRect)
        screen.blit(dice3Red, dice3RedRect)
        screen.blit(dice4Red, dice4RedRect)
        screen.blit(dice5Red, dice5RedRect)    

        screen.blit(dice1, dice1Rect)
        screen.blit(dice2, dice2Rect)
        screen.blit(dice3, dice3Rect)
        screen.blit(dice4, dice4Rect)
        screen.blit(dice5, dice5Rect)
    
        screen.blit(scoresheet, scoresheetRect)
    
        screen.blit(bluecircle, bluecircleRect)
        screen.blit(redcircle, redcircleRect)
        screen.blit(greencircle, greencircleRect)
    
        screen.blit(text1, text1Rect)
        screen.blit(text2, text2Rect)
        screen.blit(text2_5, text2_5Rect)
        screen.blit(text3, text3Rect)
        screen.blit(textplayernumb, textplayernumbRect)
        
        afficherContrat(True)
        
        pygame.display.flip()
        time.sleep(50 / 1000)
    choisirContrat()

def doborders():
    global dice1Red, dice2Red, dice3Red, dice4Red, dice5Red, queue1, queue2, queue3, queue4, queue5, queue6, border1, border2, border3, border4, border5, despourRelancer, mousepressed
    
    #first Dice
    if mousepressed and mousepos[0] >= 500 and mousepos[0] <= 560 and mousepos[1] >= 170 and mousepos[1] <= 230:
        queue1 = True
        
    if mousepressed == False and queue1 == True:   
        queue1 = False
        if border1 == True:
            border1 = False
        else:
            border1 = True
        
    if border1 == False:
        dice1Red = pygame.image.load("whiterectangle.png")
        despourRelancer[0] = 0
    else:
        dice1Red = pygame.image.load("redrectangle.png")
        despourRelancer[0] = 1
    
    #second Dice
    
    if mousepressed and mousepos[0] >= 400 and mousepos[0] <= 460 and mousepos[1] >= 245 and mousepos[1] <= 305:
        queue2 = True
        
    if mousepressed == False and queue2 == True:   
        queue2 = False
        if border2 == True:
            border2 = False
        else:
            border2 = True
        
    if border2 == False:
        dice2Red = pygame.image.load("whiterectangle.png")
        despourRelancer[1] = 0
    else:
        dice2Red = pygame.image.load("redrectangle.png")
        despourRelancer[1] = 1
        
    #third Dice
    
    if mousepressed and mousepos[0] >= 500 and mousepos[0] <= 560 and mousepos[1] >= 320 and mousepos[1] <= 380:
        queue3 = True
        
    if mousepressed == False and queue3 == True:   
        queue3 = False
        if border3 == True:
            border3 = False
        else:
            border3 = True
        
    if border3 == False:
        dice3Red = pygame.image.load("whiterectangle.png")
        despourRelancer[2] = 0
    else:
        dice3Red = pygame.image.load("redrectangle.png")
        despourRelancer[2] = 1
        
    #fourth Dice
    
    if mousepressed and mousepos[0] >= 400 and mousepos[0] <= 460 and mousepos[1] >= 395 and mousepos[1] <= 455:
        queue4 = True
        
    if mousepressed == False and queue4 == True:   
        queue4 = False
        if border4 == True:
            border4 = False
        else:
            border4 = True
        
    if border4 == False:
        dice4Red = pygame.image.load("whiterectangle.png")
        despourRelancer[3] = 0
    else:
        dice4Red = pygame.image.load("redrectangle.png")
        despourRelancer[3] = 1
    
    #fifth Dice
    
    if mousepressed and mousepos[0] >= 500 and mousepos[0] <= 560 and mousepos[1] >= 470 and mousepos[1] <= 530:
        queue5 = True
        
    if mousepressed == False and queue5 == True:   
        queue5 = False
        if border5 == True:
            border5 = False
        else:
            border5 = True
        
    if border5 == False:
        dice5Red = pygame.image.load("whiterectangle.png")
        despourRelancer[4] = 0
    else:
        dice5Red = pygame.image.load("redrectangle.png")
        despourRelancer[4] = 1
        
def checkthrow():
    global mousepressed, mousepos, dice1, dice2, dice3, dice4, dice5, border1, border2, border3, border4, border5, dice1Red, dice2Red, dice3Red, dice4Red, dice5Red, firstthrow, listdeDes, throwexecuted
    
    
    if mousepressed == 1 and (mousepos[0]-560)**2 + (mousepos[1]-40)**2 < 1600 and despourRelancer != [0, 0, 0, 0, 0] or firstthrow == True:
        throwexecuted = True
        for i in range(random.randint(4,8)):
            if despourRelancer[0] == 1:
                val = random.randint(1,6)
                if val == 1:
                    dice1 = pygame.image.load("dice1.png")
                    listedeDes[0] = 1 
                if val == 2:
                    dice1 = pygame.image.load("dice2.png")
                    listedeDes[0] = 2
                if val == 3:
                    dice1 = pygame.image.load("dice3.png")
                    listedeDes[0] = 3
                if val == 4:
                    dice1 = pygame.image.load("dice4.png")
                    listedeDes[0] = 4
                if val == 5:
                    dice1 = pygame.image.load("dice5.png")
                    listedeDes[0] = 5
                if val == 6:
                    dice1 = pygame.image.load("dice6.png")
                    listedeDes[0] = 6

            if despourRelancer[1] == 1:
                val = random.randint(1,6)
                if val == 1:
                    dice2 = pygame.image.load("dice1.png") 
                    listedeDes[1] = 1
                if val == 2:
                    dice2 = pygame.image.load("dice2.png")
                    listedeDes[1] = 2
                if val == 3:
                    dice2 = pygame.image.load("dice3.png")
                    listedeDes[1] = 3
                if val == 4:
                    dice2 = pygame.image.load("dice4.png")
                    listedeDes[1] = 4
                if val == 5:
                    dice2 = pygame.image.load("dice5.png")  
                    listedeDes[1] = 5
                if val == 6:
                    dice2 = pygame.image.load("dice6.png")
                    listedeDes[1] = 6

            if despourRelancer[2] == 1:
                val = random.randint(1,6)
                if val == 1:
                    dice3 = pygame.image.load("dice1.png") 
                    listedeDes[2] = 1
                if val == 2:
                    dice3 = pygame.image.load("dice2.png")
                    listedeDes[2] = 2
                if val == 3:
                    dice3 = pygame.image.load("dice3.png")
                    listedeDes[2] = 3
                if val == 4:
                    dice3 = pygame.image.load("dice4.png")
                    listedeDes[2] = 4
                if val == 5:
                    dice3 = pygame.image.load("dice5.png")
                    listedeDes[2] = 5
                if val == 6:
                    dice3 = pygame.image.load("dice6.png")
                    listedeDes[2] = 6

            if despourRelancer[3] == 1:
                val = random.randint(1,6)
                if val == 1:
                    dice4 = pygame.image.load("dice1.png") 
                    listedeDes[3] = 1
                if val == 2:
                    dice4 = pygame.image.load("dice2.png")
                    listedeDes[3] = 2
                if val == 3:
                    dice4 = pygame.image.load("dice3.png")
                    listedeDes[3] = 3
                if val == 4:
                    dice4 = pygame.image.load("dice4.png")
                    listedeDes[3] = 4
                if val == 5:
                    dice4 = pygame.image.load("dice5.png")
                    listedeDes[3] = 5
                if val == 6:
                    dice4 = pygame.image.load("dice6.png")
                    listedeDes[3] = 6

            if despourRelancer[4] == 1:
                val = random.randint(1,6)
                if val == 1:
                    dice5 = pygame.image.load("dice1.png") 
                    listedeDes[4] = 1
                if val == 2:
                    dice5 = pygame.image.load("dice2.png")
                    listedeDes[4] = 2
                if val == 3:
                    dice5 = pygame.image.load("dice3.png")
                    listedeDes[4] = 3
                if val == 4:
                    dice5 = pygame.image.load("dice4.png")
                    listedeDes[4] = 4
                if val == 5:
                    dice5 = pygame.image.load("dice5.png")
                    listedeDes[4] = 5
                if val == 6:
                    dice5 = pygame.image.load("dice6.png") 
                    listedeDes[4] = 6
                
            screen.blit(dice1Red, dice1RedRect)
            screen.blit(dice2Red, dice2RedRect)
            screen.blit(dice3Red, dice3RedRect)
            screen.blit(dice4Red, dice4RedRect)
            screen.blit(dice5Red, dice5RedRect)    
    
            screen.blit(dice1, dice1Rect)
            screen.blit(dice2, dice2Rect)
            screen.blit(dice3, dice3Rect)
            screen.blit(dice4, dice4Rect)
            screen.blit(dice5, dice5Rect)
    
            screen.blit(scoresheet, scoresheetRect)
    
            screen.blit(bluecircle, bluecircleRect)
            screen.blit(redcircle, redcircleRect)
            screen.blit(greencircle, greencircleRect)
    
            screen.blit(text1, text1Rect)
            screen.blit(text2, text2Rect)
            screen.blit(text2_5, text2_5Rect)
            screen.blit(text3, text3Rect)
            
            afficherContrat(True)
            
            pygame.display.flip()
        
            time.sleep(200/1000)
            
        despourRelancer[0] = 0 
        despourRelancer[1] = 0
        despourRelancer[2] = 0
        despourRelancer[3] = 0
        despourRelancer[4] = 0
        
        border1 = False
        dice1Red = pygame.image.load("whiterectangle.png")
            
        border2 = False
        dice2Red = pygame.image.load("whiterectangle.png")
          
        border3 = False
        dice3Red = pygame.image.load("whiterectangle.png")
            
        border4 = False
        dice4Red = pygame.image.load("whiterectangle.png")
            
        border5 = False
        dice5Red = pygame.image.load("whiterectangle.png")    

def checkskipthrow():
    global mousepressed, mousepos, skip, queueskipthrow
    if mousepressed == True and (mousepos[0]-350)**2 + (mousepos[1]-40)**2 < 1600:
        queueskipthrow = True
    if mousepressed == False and queueskipthrow == True:
        skip = True
        queueskipthrow = False
        
def checkdone():
    global mousepressed, mousepos, done, queuedone
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    mouse = pygame.mouse.get_pressed()
    mousepos = pygame.mouse.get_pos()
    if mouse[0] == 1:
        mousepressed = True
    else:
        mousepressed = False
    if mousepressed == True and (mousepos[0]-140)**2 + (mousepos[1]-40)**2 < 1600:
        queuedone = True
    if mousepressed == False and queuedone == True:
        done = True
        queuedone = False
        
def checkbuttons():
    global mousepressed
    checkthrow()
    checkskipthrow()
    checkdone()   
    
def endprogram():
    global joueur
    playagain = False
    while playagain != True:
        screen.fill(backgroundColor)
        screen.blit(scoresheet, scoresheetRect)
        joueur = 1
        afficherContrat(False)
        playagain = pygame.image.load("playagainrectangle.png")
        playagainRect = playagain.get_rect()
        playagainRect = playagainRect.move(280, 350)
        screen.blit(playagain, playagainRect)
        
        strjoueur = "player 1"
        font = pygame.font.Font('freesansbold.ttf', 35)  
        textplayernumb = font.render(strjoueur, True, black)
        textplayernumbRect = textplayernumb.get_rect()
        textplayernumbRect = textplayernumbRect.move(50, 40)
        screen.blit(textplayernumb, textplayernumbRect)
        
        font = pygame.font.Font('freesansbold.ttf', 22)  
        textplayagain = font.render("Play again", True, black)
        textplayagainRect = textplayagain.get_rect()
        textplayagainRect = textplayagainRect.move(300, 365)
        screen.blit(textplayagain, textplayagainRect)
        
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
        
        if mousepressed == True and mousepos[0] >= 270 and mousepos[0] <= 420 and mousepos[1] >= 350 and mousepos[1] <= 400:
            playagain = True
        
        if joueurs == 2:
            strjoueur2 = "player 2"
            font = pygame.font.Font('freesansbold.ttf', 35)  
            textplayernumb2 = font.render(strjoueur2, True, black)
            textplayernumb2Rect = textplayernumb.get_rect()
            textplayernumb2Rect = textplayernumbRect.move(400,10)
            screen.blit(textplayernumb2, textplayernumb2Rect)
            
            scoresheet2 = pygame.image.load("scoresheet.png")
            scoresheet2Rect = scoresheet2.get_rect()
            scoresheet2Rect = scoresheet2Rect.move(435, 95)
            screen.blit(scoresheet2, scoresheet2Rect)
            
            
            listeText2 = []
            listeTextRect2 = []
            joueur = 2
            font = pygame.font.Font('freesansbold.ttf', 22)   
            for i in range(13):
                listeText2.append(font.render(str((contrat[joueur-1][i])), True, black))
                listeTextRect2.append(listeText2[i].get_rect())
                if i < 6:
                    listeTextRect2[i] = listeTextRect2[i].move(657, (150 + (i) * 28))
                if i >= 6:
                    listeTextRect2[i] = listeTextRect2[i].move(657, (425 + (i-6) * 27))
            toptotal2 = 0
            for i in range(6):
                if contrat[joueur-1][i] != -1:
                    toptotal2 += contrat[joueur-1][i]
            toptotalText2 = font.render(str(toptotal2), True, black)
            toptotalTextRect2 = toptotalText2.get_rect()
            toptotalTextRect2 = toptotalTextRect2.move(650, 318)
            screen.blit(toptotalText2, toptotalTextRect2)

            topbonusText2 = font.render('35', True, black)
            topbonusTextRect2 = topbonusText2.get_rect()
            topbonusTextRect2 = topbonusTextRect2.move(650, 340)

            topbonus2 = 0
            if toptotal2 >= 63:
                screen.blit(topbonusText2,topbonusTextRect2)
                topbonus2 = 35


            toptotaltotalText2 = font.render(str(toptotal2 + topbonus2), True, black)
            toptotaltotalTextRect2 = toptotaltotalText2.get_rect()
            toptotaltotalTextRect2 = toptotaltotalTextRect2.move(650, 365)
            screen.blit(toptotaltotalText2, toptotaltotalTextRect2)

            bottomtotal2 = 0
            for i in range(7):
                if contrat[joueur-1][i+6] != -1:
                    bottomtotal2 += contrat[joueur-1][i+6]

            bottomtotalText2 = font.render(str(bottomtotal2), True, black)
            bottomtotalTextRect2 = bottomtotalText2.get_rect()
            bottomtotalTextRect2 = bottomtotalTextRect2.move(650, 616)
            screen.blit(bottomtotalText2, bottomtotalTextRect2)

            toptotaltotal2Text2 = font.render(str(toptotal2 + topbonus2), True, black)
            toptotaltotal2TextRect2 = toptotaltotal2Text2.get_rect()
            toptotaltotal2TextRect2 = toptotaltotal2TextRect2.move(650, 644)
            screen.blit(toptotaltotal2Text2,toptotaltotal2TextRect2)

            totalText2 = font.render(str(toptotal2 + bottomtotal2), True, black)
            totalTextRect2 = totalText2.get_rect()
            totalTextRect2 = totalTextRect2.move(650, 670)
            screen.blit(totalText2, totalTextRect2)

            for i in range(13):
                if contrat[joueur-1][i] != -1:
                    screen.blit(listeText2[i], listeTextRect2[i])
            
            
            
        
        pygame.display.flip()
        
while True:
    listcomplet = False
    #boucle pour une partie
    tourAQui = 0
    startprogram()
    creerGrille(joueurs) 
    while listcomplet == False:
        tourAQui += 1
        if tourAQui % 2 == 0 and joueurs == 2:
            joueur = 2
            strjoueur = "player 2"
        else:
            joueur = 1
            strjoueur = "player 1"
        screen.fill (backgroundColor)
        
        font = pygame.font.Font('freesansbold.ttf', 35)  
        textplayernumb = font.render(strjoueur, True, black)
        textplayernumbRect = textplayernumb.get_rect()
        textplayernumbRect = textplayernumbRect.move(400,600)
        
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
        
        listcomplet = True

        doborders()
        screen.blit(textplayernumb, textplayernumbRect)
    
        pygame.display.flip()
        time.sleep(50 / 1000)
    
        jouerTour()

        for i in range(joueurs):
            for j in range(0, 13):
                if contrat[i][j] == -1:
                    listcomplet = False


    endprogram()

    