import time 
matrice = []
#matrice[m][n]
n = 20
#vertical
m = 20
#horizontal
generation = 10
for i in range(m+2):
    matrice.append([])
    for j in range(n+2):
        matrice[i].append(0)

def countAround(matrice, nCase, mCase):
    nextTo = matrice[nCase][mCase] + matrice[nCase][mCase+1] + matrice[nCase][mCase+2] + matrice[nCase+1][mCase+2]+ matrice[nCase+2][mCase+2] + matrice[nCase+2][mCase+1] + matrice[nCase+2][mCase] + matrice[nCase+1][mCase]
    return (nextTo)

def playATurn(matrice,n,m):
    matrice2 = []
    for i in range(m+2):
        matrice2.append([])
        for j in range(n+2):
            matrice2[i].append(0)
    for i in range(m):
        for j in range(n):
            nextTo = countAround(matrice, i, j)
            if nextTo == 3 and matrice[i+1][j+1] == 0:
                matrice2[i+1][j+1] = 1
            elif matrice[i+1][j+1] == 1 and (nextTo == 3 or nextTo == 2):
                matrice2[i+1][j+1] = 1
            elif matrice[i+1][j+1] ==1 and nextTo != 3 and nextTo != 2:
                matrice2[i+1][j+1] = 0
    return(matrice2)

def afficherGrille(matrice, n, m):
    for i in range (m):
        for j in range(n):
            if matrice[j+1][i+1] == 0:
                print(" ", end = " ")
            else:
                print("o", end = " ")
        print("")


matrice[10][10] = 1
matrice[10][11] = 1
matrice[11][11] = 1
matrice[11][10] = 1
afficherGrille(matrice, n, m)

for i in range(generation):
    matrice = playATurn(matrice,n,m)
    afficherGrille(matrice, n, m)