import random
taille = int(input("Quelle taille voulez-vous?   "))
minimum = int(input("Quelle est le nombre minimum?   "))
maximum = int(input("Quelle est le nombre maximum?   "))

liste = []
liste1 = []
liste2 = []

taille2 = random.randint(0,taille)

for i in range (taille2):
    liste1.append(random.randint(minimum,maximum))
print(liste1)

for i in range (taille-taille2):
        liste2.append(random.randint(minimum,maximum))
print(liste2)

for i in range (1, len(liste1)):
    combiendécaller = 0
    for j in range (i):
        if liste1[i] < liste1[i-j-1]:
            combiendécaller += 1
    save = liste1[i]
    for j in range (combiendécaller):
        liste1[i-j] = liste1[i-j-1]
    liste1[i-combiendécaller] = save
print (liste1)

for i in range (1, len(liste2)):
    combiendécaller = 0
    for j in range (i):
        if liste2[i] < liste2[i-j-1]:
            combiendécaller += 1
    save = liste2[i]
    for j in range (combiendécaller):
        liste2[i-j] = liste2[i-j-1]
    liste2[i-combiendécaller] = save
print (liste2)

liste1checking = 0
liste2checking = 0

while len(liste) < taille:
    if liste1checking == len(liste1):
        for i in range (liste2checking, len(liste2)):
            liste.append(liste2[i])
    elif liste2checking == len(liste2):
        for i in range (liste1checking, len(liste1)):
            liste.append(liste1[i])
    else:
        if liste2[liste2checking] < liste1[liste1checking]:
            liste.append(liste2[liste2checking])
            liste2checking += 1
        else:
            liste.append(liste1[liste1checking])
            liste1checking += 1
            
print (liste)