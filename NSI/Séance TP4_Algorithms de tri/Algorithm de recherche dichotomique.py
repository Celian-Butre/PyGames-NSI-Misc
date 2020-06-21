import random
taille = int(input("Quelle taille voulez-vous?   "))
minimum = int(input("Quelle est le nombre minimum?   "))
maximum = int(input("Quelle est le nombre maximum?   "))

L = []
for i in range (taille):
    L.append(random.randint(minimum,maximum))

list.sort(L)
print(L)
nmbtoSrch = int(input("Quelle nombre cherchez vous?    "))
posunder = 0
posover = taille-1
found = False
while posunder+1 != posover and found == False:
    postosearch = posunder + (posover-posunder)//2
    if L[postosearch] == nmbtoSrch:
        found = True
    elif L[postosearch] > nmbtoSrch:
        posover = postosearch
    elif L[postosearch] < nmbtoSrch:
        posunder = postosearch
if found == True:
    print(nmbtoSrch, " est dans la liste, il est en position ",postosearch)
else:
    print(nmbtoSrch, " n'est pas dans la liste, il n'est pas compris entre ",L[posunder], " et ", L[posover])