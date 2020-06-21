ligne = int(input("Quelle ligne voulez vous?    "))
currentline = []
for i in range (ligne):
    currentline.append(0)

currentline[0] = 1
for j in range(ligne):    
    for i in range (1,ligne):
        currentline[-i] += currentline[-i-1]

maxnumb = currentline[ligne//2]
c = 1
while maxnumb > 9:
    c += 1
    maxnumb = maxnumb//10

for i in range (ligne):
    currentline[i] = 0

tabulation = ligne
    
currentline[0] = 1
print ((tabulation+1)*(c+1)*" ",end = "")
print (1)
for j in range(ligne-1): 
    print("")
    for i in range (1,ligne):
        currentline[-i] += currentline[-i-1]
    print(tabulation*(c+1)*" ",end = "")
    tabulation -= 1
    for i in range (ligne):
        if currentline[i] == 0:
            print (" ",end = c*" ")
        else:
            d = currentline[i]
            e = 1
            while d > 9:
                e += 1
                d = d//10
            print (currentline[i],end = (c-e+1)*" ")
            print ("", end = (c*" "))
    print ("")