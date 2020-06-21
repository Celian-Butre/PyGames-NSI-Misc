#/celian
import os, sys
import mouvements
#import Celian_Leopold_2048 

def printEntireScreen(n,m,matrice):
    os.system("clear")
    print("score : ",mouvements.score )
    print("\n\n")
    for i in range(m):
        for j in range(n):
            spaces = ""
            for z in range(len(str(2**(n*m+1))) + 1 - len(str(matrice[i][j]))):
                spaces += " "
            print(matrice[i][j], end=spaces)
        print("\n\n")
        
#\celian