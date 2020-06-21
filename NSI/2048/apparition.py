#/celian
import random

def spawnNumb(oddsOfSpawn, n, m, matrice):
    is4Or2 = whichNumb(oddsOfSpawn)
    which0 = whereNumb(n, m, matrice)
    placeNumb(n, m, is4Or2, which0, matrice)
    return (matrice)

def whichNumb(oddsOfSpawn):
    is4Or2 = random.randint(1, 100)
    if is4Or2 <= oddsOfSpawn:
        return(4)
    else:
        return(2)

def whereNumb(n, m, matrice):
    howMany0 = 0
    for i in range (m):
        for j in range (n):
            if matrice[i][j] == 0:
                howMany0 += 1
    return (random.randint(1, howMany0))

def placeNumb(n, m, is4Or2, which0, matrice):
    r = 0
    for i in range (m):
        for j in range (n):
            if matrice[i][j] == 0:
                r += 1
                if r == which0:
                    matrice[i][j] = is4Or2
#\celian