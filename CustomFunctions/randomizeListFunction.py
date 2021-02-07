def randomizeListFunction(listItems): #function to randomize the order of members in a list
    import random #imports random
    numberList = [] #creates a new list
    for i in range (len(listItems)): #does something to the new list as many times as items in the first list
        notDoubled = False #sets notDoubled by default to false
        while notDoubled == False: #does this while notDoubled == False
            randomNumber = random.randint(1,len(listItems)) #creates a number that is in between 0 and the number of items in the first list
            notDoubled = True #temporarily sets it to true
            for j in range (len(numberList)): #checks every member of the new list
                if numberList[j] == randomNumber: #if the randomNumber already appears in the new list
                    notDoubled = False #resets it to false and loops the while
        numberList.append(randomNumber) #adds the unique random number to the list
        
    #STANDARD INSERTION SORT THAT MIRRORS ITS ACTIONS TO THE FIRST LIST    
    for i in range (1, len(numberList)): #repeats 1 time less than in numberList
        moveByThis = 0 #sets this to 0
        for j in range (i): #repeats i times
            if numberList[i] < numberList[i-j-1]: #stuff
                moveByThis += 1 #stuff
        save = numberList[i] #stuff
        save2 = listItems[i] #mirrors the action on the previous line to the first list
        for j in range (moveByThis): #stuff
            numberList[i-j] = numberList[i-j-1] #stuff
            listItems[i-j] = listItems[i-j-1] #mirrors the action on the previous line to the first list
        numberList[i-moveByThis] = save #stuff
        listItems[i-moveByThis] = save2 #mirrors the action on the previous line to the first list
    return (listItems) #returns the modifed randomized list