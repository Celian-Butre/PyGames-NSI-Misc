#/celian
import mouvements
from mouvements import*
def testDeFin(n,m,matrice,obj):
    for i in range(n):
        for j in range(m):
            if matrice[j][i] == obj:
                return(2)
    changeable = False
    for i in range(4):
        newgrid = []
        for j in range(m):
            newgrid.append([])
            for k in range(n):
                newgrid[j].append(matrice[j][k])
        newgrid = mouvement(n,m,newgrid,i,False)
        if newgrid != matrice:
            changeable = True
    if changeable == False:
        return (1)
    return(0)
#\celian