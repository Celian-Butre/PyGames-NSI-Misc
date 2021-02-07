from insertionSort import *
import math

liste = [-23, 1, 1, 1, 2, 2, 2, 3, 4, 5, 10, 54]

def checkSort(liste):
    for i in range (len(liste) - 1):
        if liste[i] > liste[i+1]:
            return (False)
    return (True)

def dichotomique(liste, n):
    sort = checkSort(liste)
    if sort == False:
        liste = insertionSort(liste)
    length = len(liste)
    min = 0
    max = length - 1
    a = 0
    while min != max + 1:
        a += 1
        center = (min + max)//2
        if liste[center] == n:
            return(True)
        elif liste[center] > n:
            max = center - 1
        else:
            min = center + 1
    return(False, a)
            
def complexite(long):
    #boucle while, affectations pour une liste de taille long, qui ne contient pas l'objet desire
    boucle = int(math.log2(long+1))
    affectations = (3 + boucle * 2)
    return(boucle, affectations)
    
if __name__ == '__main__':
    print(dichotomique(liste, 7))
    #"""
    print('test')
    liste = []
    for i in range(10000):
        liste.append(0)
        print(i, dichotomique(liste, 7)[1], 1 + int(math.log2(i+1)))
    #"""
    