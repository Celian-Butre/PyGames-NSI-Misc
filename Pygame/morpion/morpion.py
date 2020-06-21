import time, pygame, sys, random
pygame.init()
width, height = 700, 700
backgroundColor = 255, 255, 255
dvdLogoSpeed = [1,  1]  
white = 255, 255, 255
black = 0, 0, 0

screen = pygame. display.set_mode((width, height))

board = pygame.image.load("board.png")
boardRect = board.get_rect()
boardRect = boardRect.move(100, 100)

def testDraw():
    global winner, turnover, gameover, draw
    draw = True
    for i in range(3):
        for j in range(3):
            if boardlist[i][j] == -1:
                draw = False
    if draw == True:
        turnover = True
        gameover = True

def checkwin():
    global winner, turnover, gameover
    for i in range(3):
        if boardlist[i][0] == boardlist[i][1] and boardlist[i][1] == boardlist[i][2] and boardlist[i][0] != -1:
            gameover = True
            if boardlist[i][0] == 0:
                winner = 1
                turnover = True
            else:
                winner = 2
                turnover = True

    for i in range(3):
        if boardlist[0][i] == boardlist[1][i] and boardlist[1][i] == boardlist[2][i] and boardlist[0][i] != -1:
            gameover = True
            if boardlist[0][i] == 0:
                winner = 1
                turnover = True
            else:
                winner = 2
                turnover = True
    if boardlist[0][0] == boardlist[1][1] and boardlist[1][1] == boardlist[2][2] and boardlist[0][0] != -1:
        gameover = True
        if boardlist[0][0] == 0:
            winner = 1
            turnover = True
        else:
            winner = 2
            turnover = True

    if boardlist[0][2] == boardlist[1][1] and boardlist[1][1] == boardlist[2][0] and boardlist[0][2] != -1:
        gameover = True
        if boardlist[0][2] == 0:
            winner = 1
            turnover = True
        else:
            winner = 2
            turnover = True

def detectclick():
    global joueur, turnover
    turnover = False
    winner = 1
    while turnover == False:
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

        if  mousepressed == True:
            if mousepos[0] > 100 and mousepos[0] < 250 and mousepos[1] > 100 and mousepos[1] < 250:
                if boardlist[0][0] == -1:
                    boardlist[0][0] = joueur - 1
                    turnover = True
            if mousepos[0] > 290 and mousepos[0] < 410 and mousepos[1] > 100 and mousepos[1] < 250:
                if boardlist[1][0] == -1:
                    boardlist[1][0] = joueur - 1
                    turnover = True
            if mousepos[0] > 450 and mousepos[0] < 600 and mousepos[1] > 100 and mousepos[1] < 250:
                if boardlist[2][0] == -1:
                    boardlist[2][0] = joueur - 1
                    turnover = True
            if mousepos[0] > 100 and mousepos[0] < 250 and mousepos[1] > 280 and mousepos[1] < 420:
                if boardlist[0][1] == -1:
                    boardlist[0][1] = joueur - 1
                    turnover = True
            if mousepos[0] > 290 and mousepos[0] < 410 and mousepos[1] > 280 and mousepos[1] < 420:
                if boardlist[1][1] == -1:
                    boardlist[1][1] = joueur - 1
                    turnover = True
            if mousepos[0] > 450 and mousepos[0] < 600 and mousepos[1] > 280 and mousepos[1] < 420:
                if boardlist[2][1] == -1:
                    boardlist[2][1] = joueur - 1
                    turnover = True
            if mousepos[0] > 100 and mousepos[0] < 250 and mousepos[1] > 450 and mousepos[1] < 600:
                if boardlist[0][2] == -1:
                    boardlist[0][2] = joueur - 1
                    turnover = True
            if mousepos[0] > 290 and mousepos[0] < 410 and mousepos[1] > 450 and mousepos[1] < 600:
                if boardlist[1][2] == -1:
                    boardlist[1][2] = joueur - 1
                    turnover = True
            if mousepos[0] > 450 and mousepos[0] < 600 and mousepos[1] > 450 and mousepos[1] < 600:
                if boardlist[2][2] == -1:
                    boardlist[2][2] = joueur - 1
                    turnover = True
        checkwin()
        testDraw()
        showboard(True)
        
            
        
def showboard(doflip):
    listdecase = [[],[]]
    screen.fill(backgroundColor)
    for i in range(3):
        for j in range(3):
            if boardlist[i][j] == -1:
                listdecase[0].append(pygame.image.load("white.png"))
            if boardlist[i][j] == 0:
                listdecase[0].append(pygame.image.load("cross.png"))
            if boardlist[i][j] == 1:
                listdecase[0].append(pygame.image.load("circle.png"))
            listdecase[1].append(listdecase[0][3*i + j].get_rect())
            listdecase[1][3*i + j] = listdecase[1][3*i + j].move(100+i*189, 100+j*189)
    for i in range(9):
        screen.blit(listdecase[0][i], listdecase[1][i])
    screen.blit(board, boardRect)
    if doflip == True:
        pygame.display.flip()
            

while True:
    gameover = False
    boardlist = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    tourAQui = 0
    winner = 0
    while gameover == False: 
        tourAQui += 1
        if tourAQui % 2 == 0:
            joueur = 2
            strjoueur = "player 2"
        else:
            joueur = 1
            strjoueur = "player 1"
        screen.fill(backgroundColor)
        screen.blit(board, boardRect)
        
        detectclick()
        pygame.display.flip()
    playagain1 = False
    while playagain1 == False:
        showboard(False)
        if winner == 1:
            strwinner = "joueur 1 wins"
        elif winner == 2:
            strwinner = "joueur 2 wins"
        else:
            strwinner = "draw"
        playagain = pygame.image.load("playagainrectangle.png")
        playagainRect = playagain.get_rect()
        playagainRect = playagainRect.move(290, 620)
        screen.blit(playagain, playagainRect)
        
        font = pygame.font.Font('freesansbold.ttf', 22)  
        textplayagain = font.render("Play again", True, black)
        textplayagainRect = textplayagain.get_rect()
        textplayagainRect = textplayagainRect.move(310, 635)
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
        
        if mousepressed == True and mousepos[0] >= 290 and mousepos[0] <= 440 and mousepos[1] >= 620 and mousepos[1] <= 670:
            playagain1 = True
        
        font = pygame.font.Font('freesansbold.ttf', 35)  
        textwinner = font.render(strwinner, True, black)
        textwinnerRect = textwinner.get_rect()
        textwinnerRect = textwinnerRect.move(300,50)
        screen.blit(textwinner, textwinnerRect)
        pygame.display.flip()
        