import random, copy
# Grand_Soleil, Nuages, Pluie, Tonerre
def MeteoChoix(Dernier_Choix):                                  # fonction qui choisit la meteo en fonction de la derniere meteo
    MeteoListe = ["Grand_Soleil", "Nuages", "Pluie", "Foudre"]  # liste des etats meteo possible
    if Dernier_Choix == "Pluie":                # si le dernier etait de la pluie
        MeteoRandom = random.randint(0,100)     # une variable aleatoire
        if MeteoRandom > 50:                    # si la variable aleatoire est au dessus de 50
            MeteoAjd = MeteoListe[3]            # la meteo sera de la foudre (la foudre ne peut donc se produire que directement apres la pluie)
            return MeteoAjd
    MeteoAjd = MeteoListe[random.randint(0,2)]  # sinon, choix aleatoire entre les trois autres etats meteo
    return MeteoAjd

def Meteo_Sucession(Meteo_Passe):   # fonction qui gere la succession de la meteo en fonction de la liste des meteos ayant eu lieu auparavant
    if len(Meteo_Passe) == 0:       # si la liste est vide
        Meteo_Passe.append({"Meteo" :"Grand_Soleil", "jour" : 1})   # append ceci
    else:                           # sinon
        if (Meteo_Passe[len(Meteo_Passe)-1]["jour"] < 5) and (Meteo_Passe[len(Meteo_Passe)-1]["Meteo"] != "Foudre"):    # si le nombre de jours est inferieur a 5, et que la meteo n'est pas la Foudre
            Meteo_Passe[len(Meteo_Passe)-1]["jour"] += 1            # rajouter un jour a la meteo
        else:
            Meteo_Passe.append({"Meteo":MeteoChoix(Meteo_Passe[len(Meteo_Passe)-1]["Meteo"]), "jour" : 1})  # rechoisir la meteo aleatoirement en le remettant au jour 1
    return Meteo_Passe              # chaque meteo dure donc 5 "jours", a part la foudre qui n'en dure qu'un seul

def Meteo_Extraction(Meteo_Passe):  # fonction qui sort la meteo actuelle de la liste de meteos passe
    Meteo_Extractee = Meteo_Passe[len(Meteo_Passe)-1]["Meteo"]
    return Meteo_Extractee

def Gestion_Foudre(MeteoDuJour, Liste_Cases):   # fonction qui gere la foudre
    if MeteoDuJour == "Foudre":                 # si la meteo est de la foudre
        while True:
            coord_i = random.randint(0, len(Liste_Cases) - 1)       # coordonnees aleatoires
            coord_j = random.randint(0, len(Liste_Cases) - 1)
            try:
                assert (Liste_Cases[coord_i][coord_j]["Biome"] != 2)        # il faut assurer que le biome n'est pas un lac
                assert (Liste_Cases[coord_i][coord_j]["etat"] == "Vierge")  # et que la case soit vierge (car elle ne doit pas frapper un endroit qui brule ou qui est calcinee)
                break
            except AssertionError:
                coord_i = random.randint(0, len(Liste_Cases) - 1)   # regenere les coordonnees aleatoires si assertion est fausse
                coord_j = random.randint(0, len(Liste_Cases) - 1)
        Liste_Cases[coord_i][coord_j]["etat"] = "Brule"             # cette case brule maintenant
        Liste_Cases[coord_i][coord_j]["Intensite du feu"] = 1       # et a une intensite du feu egale a 1
    return Liste_Cases

def VentDuJour(Vent_Dernier):                                   # fonction qui genere le vent de facon aleatoire
    ListeDirections = ["Nord","Est","Sud","Ouest", "Aucun"]     # etats du vent possible
    if Vent_Dernier == []:                                      # si la liste est vide
        Vent_Dernier.append({"Direction" : "Aucun", "Jours Restant" : random.randint(5,10)})    # le premier jour il n'y a aucun vent, et ceci durera pour 5 a 10 jours
    elif Vent_Dernier[0]["Jours Restant"] > 0:                  # sinonsi le nombre de jours restants est au dessus de 0
        Vent_Dernier[0]["Jours Restant"] -= 1                   # jours restant diminue de 1
    elif Vent_Dernier[0]["Jours Restant"] == 0:                 # sinonsi le nombre de jours restants est egal a 0
        Vent_Dernier[0] = {"Direction" : ListeDirections[random.randint(0,4)], "Jours Restant" : random.randint(5,20)}  # le vent est egal a un etat aleatoire, pour 5 a 20 jours
    return Vent_Dernier

def Vent_Extraction(VentDuJour):    # fonction qui sort le vent actuel de la liste de dico.
    Vent_Extractee = VentDuJour[0]["Direction"]
    return Vent_Extractee

if __name__ == '__main__' :
    Vent_Dernier = []
    for i in range(20):
        print(Vent_Extraction(VentDuJour(Vent_Dernier)))
            

