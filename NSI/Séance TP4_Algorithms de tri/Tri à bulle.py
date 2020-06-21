import random
taille = int(input("Quelle taille voulez-vous?   "))
minimum = int(input("Quelle est le nombre minimum?   "))
maximum = int(input("Quelle est le nombre maximum?   "))

liste = []
for i in range (taille):
    liste.append(random.randint(minimum,maximum))
print(liste)

for i in range(taille):
    for j in range(taille-i-1):
        if liste[j] > liste[j+1]:
            save = liste[j]
            liste[j] = liste[j+1]
            liste[j+1] = save
print(liste)