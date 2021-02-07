def INSERTION_SORT(numberList):
    for i in range (1, len(numberList)):
        combiendécaller = 0
        for j in range (i):
            if numberList[i] < numberList[i-j-1]:
                combiendécaller += 1
        save = numberList[i]
        for j in range (combiendécaller):
            numberList[i-j] = numberList[i-j-1]
        numberList[i-combiendécaller] = save
    return (numberList)