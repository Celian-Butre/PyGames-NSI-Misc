import random

#début du jeu, explication de l'interface
def start():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("Bienvenue au Yam's online, vous devrez choisir le nombre de joueurs, si vous choisissez 2 les joueurs joueront chacun leur tour.")
    print("Pour choisir quels des relancer il faut mettre une chaine de 5 chiffres: 0 ou 1, le 1 correspond a un des a relancer et le 0 a un des a preserver.") 

#le contrat[[],[]] = contrat[joueur1, joueur2]
def creerGrille(player):
    contrat = []
    for i in range(player):
        contrat.append(["void", -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
    return (contrat)

#affiche la grille
def afficherGrille(joueur, contrat):
    for i in range (1,14):
        if contrat[joueur][i] == -1:
            contrat[joueur][i] = ""
    print ("contrat numéro 1  (les 1)        : ", contrat[joueur][1])
    print ("contrat numéro 2  (les 2)        : ", contrat[joueur][2])
    print ("contrat numéro 3  (les 3)        : ", contrat[joueur][3])
    print ("contrat numéro 4  (les 4)        : ", contrat[joueur][4])
    print ("contrat numéro 5  (les 5)        : ", contrat[joueur][5])
    print ("contrat numéro 6  (les 6)        : ", contrat[joueur][6])
    print ("contrat numéro 7  (brelan)       : ", contrat[joueur][7])
    print ("contrat numéro 8  (carre)        : ", contrat[joueur][8])
    print ("contrat numéro 9  (full)         : ", contrat[joueur][9])
    print ("contrat numéro 10 (petite suite) : ", contrat[joueur][10])
    print ("contrat numéro 11 (grande suite) : ", contrat[joueur][11])
    print ("contrat numéro 12 (Yams)         : ", contrat[joueur][12])
    print ("contrat numéro 13 (Chance)       : ", contrat[joueur][13])
    for i in range (1,14):
        if contrat[joueur][i] == "":
            contrat[joueur][i] = -1
    
def choisirContrat(contrat, joueur, listedeDes):
    sure = False
    while sure == False:
        contratcorrecte = False
        Valider = False
        message = ("Quelle contrat choisissez vous?    ")
        while contratcorrecte == False:
            contratchoisie = str(input(message))
            for i in range (1, 14):
                if str(i) == contratchoisie and contrat[joueur][int(contratchoisie)] == -1:
                    contratcorrecte = True
            message = ("Il faut entrez un contrat qui existe et qui est vide!   ")
        sure = validerContrat(contratchoisie, contrat, joueur, listedeDes)
            

def validerContrat(contratchoisie, contrat, joueur, listedeDes):
    global sure
    if contratchoisie == "1":
        points = sommeValeur(1, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "2":
        points = sommeValeur(2, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "3":
        points = sommeValeur(3, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "4":
        points = sommeValeur(4, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "5":
        points = sommeValeur(5, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "6":
        points = sommeValeur(6, listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "7":
        Brelan = estBrelan(listedeDes)
        if Brelan == True:
            points = somme(listedeDes)
        if Brelan == False:
            points = 0
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "8":
        carre = estCarre(listedeDes)
        if carre == True:
            points = somme(listedeDes)
        if carre == False:
            points = 0
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "9":
        Full = estFull(listedeDes)
        if Full == True:
            points = 25
        if Full == False:
            points = 0
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "10":
        petitesuite = estPetiteSuite(listedeDes)
        if petitesuite == True:
            points = 30
        if petitesuite == False:
            points = 0
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "11":
        grandesuite = estGrandeSuite(listedeDes)
        if grandesuite == True:
            points = 40
        if grandesuite == False:
            points = 0 
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "12":
        Yams = estYams(listedeDes)
        if Yams == True:
            points = 50
        if Yams == False:
            points = 0
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    if contratchoisie == "13":
        points = somme(listedeDes)
        message = "Vous allez marquer " + str(points) + " points, etes vous sur: mettez y ou n   "
        reponsecorrecte = False
        while reponsecorrecte == False:
            joueurDaccord = str(input(message))
            if joueurDaccord == "y":
                reponsecorrecte = True
                contrat[joueur][int(contratchoisie)] = points
                return (True)
            if joueurDaccord == "n":
                reponsecorrecte = True
                return (False)
    
                        
#calcule la somme des des

def somme(listedeDes):
    total = 0
    for i in range(5):
        total += listedeDes[i]
    return(total)

#calcule la somme des des ayant une valeur donné en entrée
def sommeValeur(val, listedeDes):
    total = 0
    for i in range(5):
        if listedeDes[i] == val:
            total += val
    return (total)





#verifie si les dés forment un brelan
def estBrelan(listedeDes):
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
def estCarre(listedeDes):
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
def estFull(listedeDes):
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
def estYams(listedeDes):
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
def estPetiteSuite(listedeDes):
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
def estGrandeSuite(listedeDes):
    grandeSuite = True
    for i in range(4):
        if listedeDes[i] != listedeDes[i+1] - 1:
            grandeSuite = False
    return(grandeSuite)





#Trie les des
def trierDes(trierl):
    for i in range(len(trierl)):
        for j in range(len(trierl)-i-1):
            if trierl[j] > trierl[j+1]:
                save = trierl[j]
                trierl[j] = trierl[j+1]
                trierl[j+1] = save
    return(trierl)

#genere des des et les mets dans une liste
def lancerDes(lancerl):
    for i in range (5):
        lancerl.append(random.randint(1,6))
    return(lancerl)

#relance les des choisis
def relancerDes(relancerl, despourRelancer):
    for i in range (5):
        if despourRelancer[i] == 1:
            relancerl[i] = random.randint(1,6)
    return(relancerl)

#aide a choisir les des
def choisirDes():
    global skip
    correcte = False
    desArelancer = str(input("Quels des voulez-vous relancer?    "))
    while correcte == False:
        if len(desArelancer) == 5 and (desArelancer[0] == "1" or desArelancer[0] == "0") and (desArelancer[1] == "1" or desArelancer[1] == "0") and (desArelancer[2] == "1" or desArelancer[2] == "0") and (desArelancer[3] == "1" or desArelancer[3] == "0") and (desArelancer[4] == "1" or desArelancer[4] == "0"):
            correcte = True
        else:
            print ("vous n'avez pas entrez ce qu'il faut: entrez 5 chiffres a la suite qui sont soit 0 soit 1; 0 = garder; 1 = relancer")
            desArelancer = str(input("Quels des voulez-vous relancer?    "))
    desArelancer = int(desArelancer)
    despourRelancer = []
    if desArelancer == 0:
        skip = True
    else:
        skip = False
        for i in range (5):
            if desArelancer%10 == 1:
                despourRelancer.append(1)
                desArelancer -= 1
                desArelancer = desArelancer//10
            else:
                despourRelancer.append(0)
                desArelancer = desArelancer//10
    if skip == False:
        despourRelancer[0], despourRelancer[4] = despourRelancer[4], despourRelancer[0]
        despourRelancer[1], despourRelancer[3] = despourRelancer[3], despourRelancer[1]
    return (despourRelancer)


# 1 tour entier(3 lancés)
def jouerTour(joueur, grille):
    global skip, listedeDes
    print("")
    print("")
    print("                   Joueur ", joueur)
    
    afficherGrille(joueur-1, grille)
    listedeDes = []
    listedeDes = lancerDes(listedeDes)
    listedeDes = trierDes(listedeDes)
    afficherDes(listedeDes)
    despourRelancer = choisirDes()
    if skip == False:
        listedeDes = relancerDes(listedeDes, despourRelancer)
        listedeDes = trierDes(listedeDes)
        afficherDes(listedeDes)
        despourRelancer = choisirDes()
        if skip == False:
            listedeDes = relancerDes(listedeDes, despourRelancer)
            listedeDes = trierDes(listedeDes)    
            afficherDes(listedeDes)

def afficherDes(listedeDes):
    # print la premiere ligne
    for i in range (5):
        if listedeDes[i] == 1:
            print("|     |", end = "")
        elif listedeDes[i] == 2:
            print("|o    |", end = "")
        elif listedeDes[i] == 3:
            print("|    o|", end = "")
        elif listedeDes[i] == 4:
            print("|o   o|", end = "")
        elif listedeDes[i] == 5:
            print("|o   o|", end = "")
        elif listedeDes[i] == 6:
            print("|o   o|", end = "")
        print("   ", end = "")
    print("")
        
    # print la deuxieme ligne    
    for i in range (5):
        if listedeDes[i] == 1:
            print("|  o  |", end = "")
        elif listedeDes[i] == 2:
            print("|     |", end = "")
        elif listedeDes[i] == 3:
            print("|  o  |", end = "")
        elif listedeDes[i] == 4:
            print("|     |", end = "")
        elif listedeDes[i] == 5:
            print("|  o  |", end = "")
        elif listedeDes[i] == 6:
            print("|o   o|", end = "")
        print("   ", end = "")
    print("")
    
    # print la troisieme ligne
    for i in range (5):
        if listedeDes[i] == 1:
            print("|     |", end = "")
        elif listedeDes[i] == 2:
            print("|    o|", end = "")
        elif listedeDes[i] == 3:
            print("|o    |", end = "")
        elif listedeDes[i] == 4:
            print("|o   o|", end = "")
        elif listedeDes[i] == 5:
            print("|o   o|", end = "")
        elif listedeDes[i] == 6:
            print("|o   o|", end = "")        
        print("   ", end = "")
    print("")

def finirprogram(contrat, joueurs):
    print ("le jeu est terminé, les scores sont en train d'être calculés")
    for i in range(joueurs):
        score = 0
        for j in range(1,14):
            score += contrat[i][j]
        if contrat[i][1]+contrat[i][2]+contrat[i][3]+contrat[i][4]+contrat[i][5]+contrat[i][6] >= 63:
            score += 35
        print("le joueur ", i+1, " a obtenue ", score, " points")
    
#boucle pour le programe
while True:
    start()
    correct = False
    while correct == False:    
        joueurs = str(input("1 ou 2 joueurs?   "))
        if joueurs == "1" or joueurs == "2":
            correct = True
    tourAQui = 0
    joueurs = int(joueurs)
    grille = creerGrille(joueurs)
    listcomplet = False
    #boucle pour une partie
    while listcomplet == False:
        tourAQui += 1
        if tourAQui % 2 == 0 and joueurs == 2:
            joueur = 2
        else:
            joueur = 1
        jouerTour(joueur, grille)
        choisirContrat(grille, joueur-1, listedeDes)
        listcomplet = True
        for i in range(joueurs):
            for j in range(1, 14):
                if grille[i][j] == -1:
                    listcomplet = False
    finirprogram(grille, joueurs)
    str(input("entrez n'importe quoi pour rejouer"))
                    