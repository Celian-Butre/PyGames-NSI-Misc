from INSERTION_SORT import *
import random

def genSortedList(length):
    genList = []
    for i in range(length):
        genList.append(random.randint(-1*(length**2), length**2))
    genList = INSERTION_SORT(genList)    
    return(genList)

def genNonSortList(length):
    genList = []
    for i in range(length):
        genList.append(random.randint(-1*(length**2), length**2)) 
    return(genList)

def fusion_listes_triees(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    place1 = 0
    place2 = 0
    finishedList = []
    while len1 != place1 and len2 != place2:
        if list1[place1] <= list2[place2]:
            finishedList.append(list1[place1])
            place1 += 1
        else:
            finishedList.append(list2[place2])
            place2 += 1
        
    if place1 == len1:
        finishedList+= list2[place2:]
    else:
        finishedList+= list1[place1:]

    return(finishedList)

def TRIFUSION(list1, list2):
    #tri list1
    if len(list1) != 1:
        list1 = TRIFUSION(list1[(len(list1)//2):],list1[:(len(list1)//2)])
    #tri list2
    if len(list2) != 1:
        list2 = TRIFUSION(list2[(len(list2)//2):],list2[:(len(list2)//2)])
    #tri 2 list triees
    len1 = len(list1)
    len2 = len(list2)
    place1 = 0
    place2 = 0
    finishedList = []
    while len1 != place1 and len2 != place2:
        if list1[place1] <= list2[place2]:
            finishedList.append(list1[place1])
            place1 += 1
        else:
            finishedList.append(list2[place2])
            place2 += 1
        
    if place1 == len1:
        finishedList+= list2[place2:]
    else:
        finishedList+= list1[place1:]
    return(finishedList)

if __name__ == '__main__':
    print(TRIFUSION(genNonSortList(9),genNonSortList(15)))
    