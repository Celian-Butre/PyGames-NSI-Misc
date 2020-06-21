#/celian
score = 0

def cramAll(n,m,matrice):
    for y in range(m): #pour chaque ligne
        for x in range(n-1): #pour chaque case sauf la dernière
            for c in range (n-1-x):
                if matrice[y][x] == 0:
                    j = x
                    for d in range (n-1-x):
                        matrice[y][j] = matrice[y][j+1]
                        j += 1
                    matrice[y][n-1] = 0

def addAll(n,m,matrice,addScore):
    global score
    for y in range(m):
        for x in range(n-1):
            if matrice[y][x] == matrice[y][x+1] and matrice[y][x] != 0:
                matrice[y][x] += matrice[y][x]
                if addScore == True:
                    score += matrice[y][x]
                matrice[y][x+1] = 0

def rotateGrid(n,m,grid):
    secondgrid = []
    for i in range(n):
        secondgrid.append([])
    for i in range(n):
        for j in range(m):
            secondgrid[n-1-i].append(grid[j][i])
    return(secondgrid)

def mouvement(n,m,matrice,direction,addScore):
    # n = width
    # m = height
    # 0 = left 1 = up 2 = right 3 = down
    if direction < 4 and direction > -1: #On tourne la matrice pour que le déplacement soit à gauche
        for i in range(direction):
            matrice = rotateGrid(n,m,matrice)
            m,n = n,m
        # on fait le mouvement
        cramAll(n,m,matrice)
        addAll(n,m,matrice,addScore)
        cramAll(n,m,matrice)
        # on remet la grille dans le bon sens
        for i in range(4-direction):
            matrice = rotateGrid(n,m,matrice)
            m,n = n,m
    return(matrice)
#\celian