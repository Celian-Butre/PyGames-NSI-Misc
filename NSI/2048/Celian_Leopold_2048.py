#/celian
import time, sys, os, tty, termios
from saisie import*
from regles import*
from mouvements import*
from affichage import*
from apparition import*
from classement import*
import classement
n = 4   
m = 4
obj = 2048
oddsOfSpawn = 20 # en pourcentage

def saisieCaractereEnLigne():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

def changeParameters():
    global n, m, oddsOfSpawn, obj
    inputNotCorrect = True
    while inputNotCorrect == True:#vérifie que la réponse est un int
        inputNotCorrect = False
        putToObj = str(input("Quelle but voulez vous? (la norme est 2048 et cela doit être une puissance de 2)    "))
        if putToObj == "":
            inputNotCorrect = True
        for i in range (len(putToObj)):
            if putToObj[i] != "0" and putToObj[i] != "1" and putToObj[i] != "2" and putToObj[i] != "3" and putToObj[i] != "4" and putToObj[i] != "5" and putToObj[i] != "6" and putToObj[i] != "7" and putToObj[i] != "8" and putToObj[i] != "9":
                inputNotCorrect = True
        numb = 2
        allowed = False
        if inputNotCorrect == False:
            putToObj = int(putToObj)
            while numb <= putToObj:
                if numb == putToObj:
                    allowed = True
                numb *= 2
        if allowed == False:
            inputNotCorrect = True
    obj = int(putToObj)
    
    inputNotCorrect = True
    while inputNotCorrect == True:#vérifie que la réponse est un int
        inputNotCorrect = False
        putToN = str(input("Quelle largeur de grille voulez vous? (la norme est 4)    "))
        if putToN == "":
            inputNotCorrect = True
        for i in range (len(putToN)):
            if putToN[i] != "0" and putToN[i] != "1" and putToN[i] != "2" and putToN[i] != "3" and putToN[i] != "4" and putToN[i] != "5" and putToN[i] != "6" and putToN[i] != "7" and putToN[i] != "8" and putToN[i] != "9":
                inputNotCorrect = True
    n = int(putToN)
    
    inputNotCorrect = True
    while inputNotCorrect == True:#vérifie que la réponse est un int
        inputNotCorrect = False
        putToM = str(input("Quelle hauteur de grille voulez vous? (la norme est 4)    "))
        if putToM == "":
            inputNotCorrect = True
        for i in range (len(putToM)):
            if putToM[i] != "0" and putToM[i] != "1" and putToM[i] != "2" and putToM[i] != "3" and putToM[i] != "4" and putToM[i] != "5" and putToM[i] != "6" and putToM[i] != "7" and putToM[i] != "8" and putToM[i] != "9":
                inputNotCorrect = True
    m = int(putToM)
    
    inputNotCorrect = True
    while inputNotCorrect == True:#vérifie que la réponse est un int
        inputNotCorrect = False
        putToOddsOfSpawn = str(input("Quelle pourcentage d'apparition de 4 voulez vous? (la norme est 20, il faut un nombre entier entre 0 et 100)    "))
        if putToOddsOfSpawn == "":
            inputNotCorrect = True
        for i in range (len(putToOddsOfSpawn)):
            if putToOddsOfSpawn[i] != "0" and putToOddsOfSpawn[i] != "1" and putToOddsOfSpawn[i] != "2" and putToOddsOfSpawn[i] != "3" and putToOddsOfSpawn[i] != "4" and putToOddsOfSpawn[i] != "5" and putToOddsOfSpawn[i] != "6" and putToOddsOfSpawn[i] != "7" and putToOddsOfSpawn[i] != "8" and putToOddsOfSpawn[i] != "9":
                inputNotCorrect = True
        if inputNotCorrect == False:    
            if int(putToOddsOfSpawn) < 0 or int(putToOddsOfSpawn) > 100:
                inputNotCorrect = True
    oddsOfSpawn = int(putToOddsOfSpawn)
    
    print("Merci d'avoir customisé vos paramètres \nretour à l'écran titre")
    time.sleep(2)
    os.system("clear")
    print("Bienvenue au 2048 de Léopold et de Célian \nLes règles de notre jeu sont les mêmes que dans tout 2048 standard \nles touches sont haut, bas, gauche, droite, pour les déplacements; r pour recommencer le jeu \nSi à n'importe quel moment vous voulez arreter le programme appuyez sur a \nSi vous voulez customiser la taille de la grille maintenant, appuyez sur c \nPour démarer le jeu, appuyez sur f \n")

def startGame():
    os.system("clear")
    print("Bienvenue au 2048 de Léopold et de Célian \nLes règles de notre jeu sont les mêmes que dans tout 2048 standard \nles touches sont haut = z, bas = s, gauche = q, droite = d, pour les déplacements; r pour recommencer le jeu \nSi à n'importe quel moment vous voulez arreter le programme appuyez sur a \nSi vous voulez customiser la taille de la grille maintenant, appuyez sur c \nPour démarer le jeu, appuyez sur f \n")
    ready2Start = False
    while ready2Start == False:
        
        key = saisieCaractereEnLigne()

        if key == "f":
            ready2Start = True 
            
        if key == "c":
            changeParameters()
    
def playTurn(n, m, oddsOfSpawn, matrice):
    global done, gameOver
    direction = checkKeyPress()
    while direction == 4:
        direction = checkKeyPress()
    if direction == 5:
        gameOver = True
        done = 3
    #copie de matrice
    matrice2 = []
    for i in range (len(matrice)):
        matrice2.append([])
        for j in range (len(matrice[i])):
            matrice2[i].append(matrice[i][j])
    matrice = mouvement(n, m, matrice, direction, True)
    if matrice != matrice2: #vérifie si changement
        matrice = spawnNumb(oddsOfSpawn, n, m, matrice)
        printEntireScreen(n, m, matrice) 
        matrice3D.append(matrice)
    return (matrice)

def checkContinue():
    correctInput = False
    while correctInput == False:
        continuer = str(input("Voulez vous continuer? (y pour oui et n pour non)"))
        if continuer == "y":
            return (False)
            print("Appuyez n'importe où pour continuer")
        if continuer == "n":
            return (True)
        
def checkSaveScore():
    correctInput = False
    while correctInput == False:
        continuer = str(input("Voulez vous sauvegarder votre score? (y pour oui et n pour non)"))
        if continuer == "y":
            name = str(input("Quel est votre nom?   "))
            correctInput = True
            file = open("highscores.txt", "r")
            recup = recupererScores(file)
            listnames = namestolist(recup, name)
            listscore = scoretolist(recup, score)
            classements(mouvements.score, name, listscore, listnames)
        if continuer == "n":
            correctInput = True

while True:
    file = open("highscores.txt", "r")
    recup = recupererScores(file)
    startGame()
    matrice = []
    for i in range (m):
        matrice.append([])
        for j in range (n):
            matrice[i].append(0) 
    matrice = spawnNumb(oddsOfSpawn, n, m, matrice)
    matrice = spawnNumb(oddsOfSpawn, n, m, matrice)
    printEntireScreen(n, m, matrice)
    gameOver = False
    passed2048 = False
    mouvements.score = 0
    matrice3D = []
    while gameOver == False:
        matrice = playTurn(n, m, oddsOfSpawn, matrice)
        time.sleep(0.25)
        done = testDeFin(n,m,matrice,obj)
        if done == 1:
            gameOver = True
        if done == 2 and passed2048 == False:
            gameOver = checkContinue()
            passed2048 = True
    checkSaveScore()

#\celian