 def dichotomique(liste, item):
    if len(liste) == 1:
        if liste[0] == item:
            return(True)
        else:
            return(False)
    milieu = (len(liste)//2)
    if liste[milieu] == item:
        return(True)
    if liste[milieu] > item:
        list2 = liste[:milieu]
        return(dichotomique(list2,item))
    if liste[milieu] < item:
        list2 = liste[milieu + 1:]
        return(dichotomique(list2,item))
        
if __name__ == '__main__':
    liste = [1,2,3,4,5,6,7,8,9,10]
    print(dichotomique(liste,0))
    print(dichotomique(liste,1))
    print(dichotomique(liste,2))
    print(dichotomique(liste,3))
    print(dichotomique(liste,4))
    print(dichotomique(liste,5))
    print(dichotomique(liste,6))
    print(dichotomique(liste,7))
    print(dichotomique(liste,8))
    print(dichotomique(liste,9))
    print(dichotomique(liste,10))
    print(dichotomique(liste,11))