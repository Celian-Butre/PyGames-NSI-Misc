import random
matrice = [[8,1,6],[3,5,7],[4,9,2]]
size = 3
magique = False
def totcol(col):
    global matrice, size
    tot = 0
    for i in range (size):
        tot += matrice[i][col]
    return(tot)

def totligne(ligne):
    global matrice, size
    tot = 0
    for i in range (size):
        tot += matrice[ligne][i]
    return(tot)

def totdiag(inverse):
    global matrice, size
    tot = 0
    for i in range(size):
        tot += matrice[abs((size-1)*inverse-i)][i]
    return(tot)

def estMagique():
    global magique
    defaulttot = totcol(0)
    magique = True
    for i in range (3):
        if totcol(i) != defaulttot or totligne(i) != defaulttot:
            magique = False
            print(1)
    if totdiag(0) != defaulttot or totdiag(1) != defaulttot:
        magique = False
        print(2)
    
    return(magique)

def estParfait():
    global matrice, size
    magique = estMagique()
    if magique == False:
        return (False)
    else:
        listtrier = []
        for i in range (size):
            for j in range(size):
                listtrier.append(matrice[i][j])
        for i in range (len(listtrier)):
            for j in range(len(listtrier)-i-1):
                if listtrier[j] > listtrier[j+1]:
                    save = listtrier[j]
                    listtrier[j] = listtrier[j+1]
                    listtrier[j+1] = save
        if listtrier[0] == 1:
            for i in range(len(listtrier)-1):
                if listtrier[i] + 1 != listtrier[i+1]:
                    return(False)
        else:
            return(False)
    return(True)
        
print(estParfait())