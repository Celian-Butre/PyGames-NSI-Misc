import random
taille = int(input("Quelle taille voulez-vous?   "))
minimum = int(input("Quelle est le nombre minimum?   "))
maximum = int(input("Quelle est le nombre maximum?   "))

liste = []
for i in range (taille):
    liste.append(random.randint(minimum,maximum))
print(liste)

for i in range(taille): #pour chaque triement
    minimum = liste[i]
    posmin = i
    for j in range (i,taille): #pour chercher le minimum
        if minimum > liste[j]:
            minimum = liste[j]
            posmin = j
    save = liste[i]
    liste[i] = liste[posmin]
    liste[posmin] = save
print(liste)