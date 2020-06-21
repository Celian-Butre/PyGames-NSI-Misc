import random
taille = int(input("Quelle taille voulez-vous?   "))
minimum = int(input("Quelle est le nombre minimum?   "))
maximum = int(input("Quelle est le nombre maximum?   "))

liste = []
for i in range (taille):
    liste.append(random.randint(minimum,maximum))
print(liste)

for i in range (1, taille):
    combiendécaller = 0
    for j in range (i):
        if liste[i] < liste[i-j-1]:
            combiendécaller += 1
    save = liste[i]
    for j in range (combiendécaller):
        liste[i-j] = liste[i-j-1]
    liste[i-combiendécaller] = save
print (liste)