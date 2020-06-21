import time, pygame, sys, random, math
pygame.init()
# min 960 640
width, height = 960, 640
backgroundColor = 255, 255, 255
white = 255, 255, 255
black = 0, 0, 0
widthadjustment = (width - 640)//2
heightadjustment = (height - 640)//2

screen = pygame. display.set_mode((width, height))

board = pygame.image.load("board.png")
boardRect = board.get_rect()
boardRect = boardRect.move(0 + widthadjustment, 0 + heightadjustment)

def startGame():
    global whitePieces, blackPieces, whitesRemoved, blacksRemoved
    #set variables
    whitesRemoved = 0
    blacksRemoved = 0
    # import des pièces:
    whitePawn = pygame.image.load("whitePawn.png")
    blackPawn = pygame.image.load("blackPawn.png")

    #   whitePieces = [Images][Rect][square][hasbeenmovedbefore][movedthePREVIOUSturn]
    #   blackPieces = [Images][Rect][square][hasbeenmovedbefore]

    #   [Rect] = pawn 1-8, rook, knight, bishop, rook, knight, bishop, queen, king
    #   [square] = width, height starting at 0 from top left

    whitePieces = [[],[],[],[],[]]
    blackPieces = [[],[],[],[],[]]

    for i in range (8):
        whitePieces[0].append(pygame.image.load("whitePawn.png"))
        blackPieces[0].append(pygame.image.load("blackPawn.png"))
        whitePieces[1].append(whitePieces[0][i].get_rect())
        whitePieces[2].append([i,6])
        blackPieces[1].append(blackPieces[0][i].get_rect())
        blackPieces[2].append([i,1])
        whitePieces[3].append([False])
        blackPieces[3].append([False])
        whitePieces[4].append([False])
        blackPieces[4].append([False])

    for i in range(2):
        #rooks
        whitePieces[0].append(pygame.image.load("whiteRook.png"))
        blackPieces[0].append(pygame.image.load("blackRook.png"))
        whitePieces[1].append(whitePieces[0][i*3+8].get_rect())
        whitePieces[2].append([i * 7, 7])
        blackPieces[1].append(blackPieces[0][i*3+8].get_rect())
        blackPieces[2].append([i * 7, 0])
        whitePieces[3].append([False])
        blackPieces[3].append([False])
        whitePieces[4].append([False])
        blackPieces[4].append([False])
        
        #knights
        whitePieces[0].append(pygame.image.load("whiteKnight.png"))
        blackPieces[0].append(pygame.image.load("blackKnight.png"))
        whitePieces[1].append(whitePieces[0][i*3+9].get_rect())
        whitePieces[2].append([i * 5 + 1, 7])
        blackPieces[1].append(blackPieces[0][i*3+9].get_rect())
        blackPieces[2].append([i * 5 + 1, 0])
        whitePieces[3].append([False])
        blackPieces[3].append([False])
        whitePieces[4].append([False])
        blackPieces[4].append([False])
        
        #bishop
        whitePieces[0].append(pygame.image.load("whiteBishop.png"))
        blackPieces[0].append(pygame.image.load("blackBishop.png"))
        whitePieces[1].append(whitePieces[0][i*3+10].get_rect())
        whitePieces[2].append([i * 3 + 2, 7])
        blackPieces[1].append(blackPieces[0][i*3+10].get_rect())
        blackPieces[2].append([i * 3 + 2, 0])
        whitePieces[3].append([False])
        blackPieces[3].append([False])
        whitePieces[4].append([False])
        blackPieces[4].append([False])
        

    #queens
    whitePieces[0].append(pygame.image.load("whiteQueen.png"))
    blackPieces[0].append(pygame.image.load("blackQueen.png"))
    whitePieces[1].append(whitePieces[0][14].get_rect())
    whitePieces[2].append([3, 7])
    blackPieces[1].append(blackPieces[0][14].get_rect())
    blackPieces[2].append([3, 0])
    whitePieces[3].append([False])
    blackPieces[3].append([False]) 
    whitePieces[4].append([False])
    blackPieces[4].append([False])

    #kings
    whitePieces[0].append(pygame.image.load("whiteKing.png"))
    blackPieces[0].append(pygame.image.load("blackKing.png"))
    whitePieces[1].append(whitePieces[0][15].get_rect())
    whitePieces[2].append([4, 7])
    blackPieces[1].append(blackPieces[0][15].get_rect())
    blackPieces[2].append([4, 0])
    whitePieces[3].append([False])
    blackPieces[3].append([False])
    whitePieces[4].append([False])
    blackPieces[4].append([False])

def playATurn():
    global pieceToPlay, PieceMoved
    PieceMoved = False
    pieceToPlay = None
    PlacePieces()
    while PieceMoved == False:
        pieceToPlay = checkselectpieces()
        moveSelectedPiece()
    
def PlacePieces():  
    #blit background
    screen.fill(backgroundColor)
    screen.blit(board, boardRect)
    #Blit pawns
    for i in range(len(whitePieces[0])):
        whitePieces[1][i] = whitePieces[1][i].move(80*whitePieces[2][i][0]+widthadjustment+15, 80*whitePieces[2][i][1]+heightadjustment+10)
        blackPieces[1][i] = blackPieces[1][i].move(80*blackPieces[2][i][0]+widthadjustment+15, 80*blackPieces[2][i][1]+heightadjustment+10)  
        screen.blit(whitePieces[0][i], whitePieces[1][i])
        screen.blit(blackPieces[0][i], blackPieces[1][i])
        whitePieces[1][i] = whitePieces[1][i].move(-(80*whitePieces[2][i][0]+widthadjustment+15), -(80*whitePieces[2][i][1]+heightadjustment+10))
        blackPieces[1][i] = blackPieces[1][i].move(-(80*blackPieces[2][i][0]+widthadjustment+15), -(80*blackPieces[2][i][1]+heightadjustment+10)) 
    #blitdots
    pygame.display.flip()
    
def checkPawn(coordsnew, coordsold):
    global mousepos, whiteTurn, whitePieces, blackPieces
    if whiteTurn == True:
        if coordsnew[0] == coordsold[0]:
            #initial double jump
            if coordsold[1] == 6 and coordsnew[1] == 4:
                allowed = [True]
                for i in range(16):
                    if blackPieces[2][i] == coordsnew or (blackPieces[2][i][0] == coordsnew[0] and blackPieces[2][i][1] == coordsnew[1] + 1):
                        allowed = [False]
                if allowed == [True]:
                    whitePieces[4][coordsold[0]] = [True]
                return (allowed)
            #single jump
            if coordsold[1] == coordsnew[1] + 1:
                allowed = [True]
                for i in range(16):
                    if blackPieces[2][i] == coordsnew:
                        allowed = [False]
                return(allowed)
            return([False])
        #eating pieces
        elif coordsnew[0] == coordsold[0] - 1 or coordsnew[0] == coordsold[0] + 1:
            if coordsold[1] == coordsnew[1] + 1:
                eating = False
                enPassant = False
                for i in range(16):
                    if coordsnew == blackPieces[2][i]:
                        eating = True
                #en passant
                if coordsold[1] == 3:
                    if blackPieces[4][coordsnew[0]] == [True]:
                        enPassant = True
                if eating == True:
                    return([True])
                elif enPassant == True:
                    return([True,coordsnew[0],3])
                else:
                    return([False])
            else:
                return([False])
        else:
            return ([False])
    else:
        if coordsnew[0] == coordsold[0]:
            #initial double jump
            if coordsold[1] == 1 and coordsnew[1] == 3:
                allowed = [True]
                for i in range(16):
                    if whitePieces[2][i] == coordsnew or (whitePieces[2][i][0] == coordsnew[0] and whitePieces[2][i][1] == coordsnew[1] - 1):
                        allowed = [False]
                if allowed == [True]:
                    blackPieces[4][coordsold[0]] = [True]
                return(allowed)
            #single jump
            if coordsold[1] == coordsnew[1] - 1:
                allowed = [True]
                for i in range(16):
                    if whitePieces[2][i] == coordsnew:
                        allowed = [False]
                return(allowed)
            return([False])
        #eating pieces
        if coordsnew[0] == coordsold[0] - 1 or coordsnew[0] == coordsold[0] + 1:
            if coordsold[1] == coordsnew[1] - 1:
                eating = False
                enPassant = False
                for i in range(16):
                    if coordsnew == whitePieces[2][i]:
                        eating = True
                #en passant
                if coordsold[1] == 4:
                    if whitePieces[4][coordsnew[0]] == [True]:
                        enPassant = True
                if eating == True:
                    return([True])
                elif enPassant == True:
                    return([True,coordsnew[0],4])
                else:
                    return([False])
            else:
                return ([False])
        else:
            return ([False])
        
def checkBishop(coordsnew, coordsold):
    global whitePieces, blackPieces
    x = coordsold[0] - 1
    y = coordsold[1] - 1
    allowed = False
    while x >= 0 and y >= 0 and allowed == False:
        if coordsnew == [x, y]:
            allowed = True   
            ligne = [-1, -1]
        x -= 1
        y -= 1
    x = coordsold[0] + 1
    y = coordsold[1] + 1
    while x <= 7 and y <= 7 and allowed == False:
        if coordsnew == [x, y]:
            allowed = True 
            ligne = [1, 1]
        x += 1
        y += 1
    x = coordsold[0] - 1
    y = coordsold[1] + 1
    while x >= 0 and y <= 7 and allowed == False:
        if coordsnew == [x, y]:
            allowed = True 
            ligne = [-1, 1]
        x -= 1
        y += 1
    x = coordsold[0] + 1
    y = coordsold[1] - 1
    while x <= 7 and y >= 0 and allowed == False:
        if coordsnew == [x, y]:
            allowed = True 
            ligne = [1, -1]
        x += 1
        y -= 1
    x = coordsold[0]
    y = coordsold[1]
    if allowed == True:
        while x + ligne[0] != coordsnew[0] and y + ligne[1] != coordsnew[1] and allowed == True:
            x += ligne[0]
            y += ligne[1]
            for i in range (16):
                if whitePieces[2][i] == [x, y] or blackPieces[2][i] == [x, y]:
                    allowed = False
    return(allowed)

def checkKnight(coordsnew, coordsold):
    if abs(coordsnew[0] - coordsold[0]) + abs(coordsnew[1] - coordsold[1]) == 3 and abs(coordsnew[0] - coordsold[0]) != 0 and abs(coordsnew[1] - coordsold[1]) != 0:
        return(True)
    return(False)

def checkRook(coordsnew, coordsold):
    allowed = False
    if coordsnew[0] == coordsold[0]:
        allowed = True
        columnorrow = [0, 1]
        if coordsnew[1] > coordsold[1]:
            increment = [1, 0]
        else:
            increment = [-1, 0]
    if coordsnew[1] == coordsold[1]:
        allowed = True
        columnorrow = [1, 0]
        if coordsnew[0] > coordsold[0]:
            increment = [0, 1]
        else:
            increment = [0, -1]
    if allowed == True:
        x = coordsold[0] + (increment[1] * columnorrow[0])
        y = coordsold[1] + (increment[0] * columnorrow[1])
        while x != coordsnew[0] or y != coordsnew[1]:
            for i in range(16):
                if whitePieces[2][i] == [x, y] or blackPieces[2][i] == [x, y]:
                    allowed = False
            x += increment[1]
            y += increment[0]
    return(allowed)

def checkQueen(coordsnew, coordsold):
    allowed1 = checkRook(coordsnew, coordsold)
    allowed2 = checkBishop(coordsnew, coordsold)
    if allowed1 == True or allowed2 == True:
        return(True)
    return(False)

def checkKingInDanger(coordsnew, coordsold):
    global whiteTurn, isallowed, allowed
    if True:
        storekingpos = coordsold
        for i in range (15):
            if whiteTurn == True:
                coordsold = blackPieces[2][i]
                whitePieces[2][15] = coordsnew
                #correct assignement
            else:
                coordsold = whitePieces[2][i]
                blackPieces[2][15] = coordsnew
            if i >= 0 and i <= 7:
                
                whiteTurn = not(whiteTurn)
                
                allowed = checkPawn(coordsnew, coordsold)
                
                whiteTurn = not(whiteTurn)
            
            if i == 10 or i == 13:
                allowed = checkBishop(coordsnew, coordsold)   
            if i == 9 or i == 12:
                allowed = checkKnight(coordsnew, coordsold)   
            if i == 8 or i == 11:
                allowed = checkRook(coordsnew, coordsold)   
            if i == 14:
                allowed = checkQueen(coordsnew, coordsold)
            
            if allowed == True: 
                if whiteTurn == True:
                    whitePieces[2][15] = storekingpos
                else:
                    blackPieces[2][15] = storekingpos
                return (False)
            
        if whiteTurn == True:
            coordsking = blackPieces[2][15]
        else:
            coordsking = whitePieces[2][15]
        
        if whiteTurn == True:
            whitePieces[2][15] = storekingpos
        else:
            blackPieces[2][15] = storekingpos  
            
        if (abs(coordsnew[0] - coordsking[0]) == 1 or abs(coordsnew[0] - coordsking[0]) == 0) and (abs(coordsnew[1] - coordsking[1]) == 1 or abs(coordsnew[1] - coordsking[1]) == 0):
            return (False)
        
    return (True)

def checkKing(coordsnew, coordsold):
    global whiteTurn
    allowed = False
    if abs(coordsnew[0] - coordsold[0]) + abs(coordsnew[1] - coordsold[1]) == 1 or abs(coordsnew[0] - coordsold[0]) + abs(coordsnew[1] - coordsold[1]) == 0 or abs(coordsnew[0] - coordsold[0]) == 1 and abs(coordsnew[1] - coordsold[1]) == 1:
        allowed = True
        isallowed = True
    if allowed == True:
        allowed = checkKingInDanger(coordsnew, coordsold)
    if whiteTurn == True:
        if whitePieces[3][15] == [False]:
            if coordsnew == [6, 7]:
                if whitePieces[3][11] == [False]:
                    emptyHallway = True
                    for i in range (16):
                        if whitePieces[2][i] == [5, 7] or whitePieces[2][i] == [6,7] or blackPieces[2][i] == [5,7] or blackPieces[2][i] == [6,7]:
                            emptyHallway = False
                    allowed1 = checkKingInDanger([6,7], coordsold)
                    allowed2 = checkKingInDanger([5,7], coordsold)
                    allowed3 = checkKingInDanger([4,7], coordsold)
                    if allowed1 == False or allowed2 == False or allowed3 == False:
                        emptyHallway = False
                    if emptyHallway == True:
                        allowed = True
                        whitePieces[2][11] = [5, 7]
            if coordsnew == [2, 7]:
                if whitePieces[3][8] == [False]:
                    emptyHallway = True
                    for i in range (16):
                        if whitePieces[2][i] == [1, 7] or whitePieces[2][i] == [2,7] or whitePieces[2][i] == [3,7] or blackPieces[2][i] == [1,7] or blackPieces[2][i] == [2,7] or blackPieces[2][i] == [3,7]:
                            emptyHallway = False
                    allowed1 = checkKingInDanger([2,7], coordsold)
                    allowed2 = checkKingInDanger([3,7], coordsold)
                    allowed3 = checkKingInDanger([4,7], coordsold)
                    if allowed1 == False or allowed2 == False or allowed3 == False:
                        emptyHallway = False
                    if emptyHallway == True:
                        allowed = True
                        whitePieces[2][8] = [3, 7]
    else:
        if blackPieces[3][15] == [False]:
            if coordsnew == [6, 0]:
                if blackPieces[3][11] == [False]:
                    emptyHallway = True
                    for i in range (16):
                        if whitePieces[2][i] == [5, 0] or whitePieces[2][i] == [6,0] or blackPieces[2][i] == [5,0] or blackPieces[2][i] == [6,0]:
                            emptyHallway = False
                    allowed1 = checkKingInDanger([6,0], coordsold)
                    allowed2 = checkKingInDanger([5,0], coordsold)
                    allowed3 = checkKingInDanger([4,0], coordsold)
                    if allowed1 == False or allowed2 == False or allowed3 == False:
                        emptyHallway = False
                    if emptyHallway == True:
                        allowed = True
                        blackPieces[2][11] = [5, 0]
            if coordsnew == [2, 0]:
                if blackPieces[3][8] == [False]:
                    emptyHallway = True
                    for i in range (16):
                        if whitePieces[2][i] == [1,0] or whitePieces[2][i] == [2,0] or whitePieces[2][i] == [3,0] or blackPieces[2][i] == [1,0] or blackPieces[2][i] == [2,0] or blackPieces[2][i] == [3,0]:
                            emptyHallway = False
                    allowed1 = checkKingInDanger([2,0], coordsold)
                    allowed2 = checkKingInDanger([3,0], coordsold)
                    allowed3 = checkKingInDanger([4,0], coordsold)
                    if allowed1 == False or allowed2 == False or allowed3 == False:
                        emptyHallway = False
                    if emptyHallway == True:
                        allowed = True
                        blackPieces[2][8] = [3, 0]
    return(allowed)
 
def mouseStats():
    global mousepressed, mousepos
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()

        mouse = pygame.mouse.get_pressed()
        mousepos = pygame.mouse.get_pos()
        if mouse[0] == 1:
            mousepressed = True
        else:
            mousepressed = False
            
def removePiece(coords):
    global whiteTurn, whitesRemoved, blacksRemoved
    for i in range(16): 
        if whiteTurn == False:
            if coords == whitePieces[2][i]:
                whitesRemoved += 1
                whitePieces[2][i] = [-(widthadjustment//80) + (whitesRemoved + 1) %2,-(heightadjustment//80) + (whitesRemoved-1)//2]
                return(i)
        else:
            if coords == blackPieces[2][i]:
                blacksRemoved += 1
                blackPieces[2][i] = [-(widthadjustment//80) + 10 + (blacksRemoved + 1) %2,-(heightadjustment//80) + (blacksRemoved-1)//2]
                return(i)
    return (-1)

def unremovePiece(coords, piece):
    global whiteTurn, whitesRemoved, blacksRemoved 
    if whiteTurn == False:
        whitePieces[2][piece] = coords
        whitesRemoved -= 1
    else:
        blackPieces[2][piece] = coords
        blacksRemoved -= 1
        
def moveSelectedPiece():  
    global mousepos, mousepressed, pieceToPlay, whiteTurn, PieceMoved
    mouseStats()
    wrongPiece = False
    for i in range(16):
        if mousepressed == True:
            if whiteTurn == True:
                if (mousepos[0] - widthadjustment)//80 == whitePieces[2][i][0] and (mousepos[1] - heightadjustment)//80 == whitePieces[2][i][1]:
                    pieceToPlay = i
                    wrongPiece = True
            if whiteTurn == False:
                if (mousepos[0] - widthadjustment)//80 == blackPieces[2][i][0] and (mousepos[1] - heightadjustment)//80 == blackPieces[2][i][1]:
                    pieceToPlay = i
                    wrongPiece = True
        if (mousepos[0] - widthadjustment)//80 < 0 or (mousepos[0] - widthadjustment)//80 > 7 or (mousepos[1] - heightadjustment)//80 < 0 or (mousepos[1] - heightadjustment)//80 > 7:
            wrongPiece = True
    if wrongPiece == False and pieceToPlay != None:
        if mousepressed == True:
            if pieceToPlay >= 0 and pieceToPlay <= 7:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkPawn(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed[0] == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        if len(allowed) == 3:
                            pieceRemoved = removePiece([allowed[1],allowed[2]])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            if len(allowed) == 3:
                                unremovePiece([allowed[1],allowed[2]], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkPawn(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed[0] == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        if len(allowed) == 3:
                            pieceRemoved = removePiece([allowed[1],allowed[2]])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(blackPieces[2][pieceToPlay], pieceRemoved)
                            if len(allowed) == 3:
                                unremovePiece([allowed[1],allowed[2]], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False
            elif pieceToPlay == 10 or pieceToPlay == 13:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkBishop(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkBishop(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False
            elif pieceToPlay == 9 or pieceToPlay == 12:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkKnight(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkKnight(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False
            elif pieceToPlay == 8 or pieceToPlay == 11:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkRook(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        whitePieces[3][pieceToPlay] = True
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkRook(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        blackPieces[3][pieceToPlay] = True
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False
            elif pieceToPlay == 14:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkQueen(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkQueen(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False
            elif pieceToPlay == 15:
                if whiteTurn == True:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkKing(coordsnew, whitePieces[2][pieceToPlay])
                    if allowed == True:
                        saveWhitePieces = [whitePieces[2][pieceToPlay][0],whitePieces[2][pieceToPlay][1]]
                        whitePieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        whitePieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        whitePieces[3][pieceToPlay] = True
                        PieceMoved = True
                        pieceRemoved = removePiece(whitePieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(whitePieces[2][15], whitePieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            whitePieces[2][pieceToPlay] = saveWhitePieces
                            PieceMoved = False
                else:
                    coordsnew = [(mousepos[0] - widthadjustment)//80, (mousepos[1] - heightadjustment)//80]
                    allowed = checkKing(coordsnew, blackPieces[2][pieceToPlay])
                    if allowed == True:
                        saveBlackPieces = [blackPieces[2][pieceToPlay][0],blackPieces[2][pieceToPlay][1]]
                        blackPieces[2][pieceToPlay][0] = (mousepos[0] - widthadjustment)//80
                        blackPieces[2][pieceToPlay][1] = (mousepos[1] - heightadjustment)//80
                        blackPieces[3][pieceToPlay] = True
                        PieceMoved = True
                        pieceRemoved = removePiece(blackPieces[2][pieceToPlay])
                        isKingInDanger = not(checkKingInDanger(blackPieces[2][15], blackPieces[2][15]))
                        if isKingInDanger == True:
                            if pieceRemoved != -1:
                                unremovePiece(whitePieces[2][pieceToPlay], pieceRemoved)
                            blackPieces[2][pieceToPlay] = saveBlackPieces
                            PieceMoved = False

def checkselectpieces():
    global whiteTurn, mousepos, mousepressed, pieceToPlay
    mouseStats()
    if mousepressed == True:
        for i in range (16):
            if whiteTurn == True:
                if (mousepos[0] - widthadjustment)//80 == whitePieces[2][i][0] and (mousepos[1] - heightadjustment)//80 == whitePieces[2][i][1]:
                    return(i)
            else:
                if (mousepos[0] - widthadjustment)//80 == blackPieces[2][i][0] and (mousepos[1] - heightadjustment)//80 == blackPieces[2][i][1]:
                    return(i)
    return(pieceToPlay)
                    
while True:
    startGame()
    gameover = False
    whiteTurn = False
    changeTurn = False
    while gameover == False:
        if whiteTurn == True:
            whiteTurn = False
            for i in range(16):
                blackPieces[4][i] = [False]
        else:
            whiteTurn = True
            for i in range(16):
                whitePieces[4][i] = [False]
        playATurn()