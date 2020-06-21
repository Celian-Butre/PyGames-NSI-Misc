import random
# Grand_Soleil, Nuages, Pluie, Foudre
def MeteoChoix(Dernier_Choix):
    MeteoListe = ["Grand_Soleil", "Nuages", "Pluie", "Foudre"]
    if Dernier_Choix == "Pluie":
        MeteoRandom = random.randint(0,100)
        if MeteoRandom > 70:
            MeteoAjd = MeteoListe[3]
            return MeteoAjd
    MeteoAjd = MeteoListe[random.randint(0,2)]
    return MeteoAjd

def Meteo_Sucession(Meteo_Passe):
    if len(Meteo_Passe) == 0:
        Meteo_Passe.append({"Meteo" :"Grand_Soleil", "jour" : 1})
    else:
        if (Meteo_Passe[len(Meteo_Passe)-1]["jour"] < 3) and (Meteo_Passe[len(Meteo_Passe)-1]["Meteo"] != "Foudre"):
            Meteo_Passe[len(Meteo_Passe)-1]["jour"] += 1
        else:
            Meteo_Passe.append({"Meteo":MeteoChoix(Meteo_Passe[len(Meteo_Passe)-1]["Meteo"]), "jour" : 1})
    return Meteo_Passe

def Meteo_Extraction(Meteo_Passe):
    Meteo_Extractee = Meteo_Passe[len(Meteo_Passe)-1]["Meteo"]
    return Meteo_Extractee

def Gestion_Foudre(MeteoDuJour, Liste_Cases):
    if MeteoDuJour == "Foudre":
        while True:
            coord_i = random.randint(0, len(Liste_Cases) - 1)
            coord_j = random.randint(0, len(Liste_Cases) - 1)
            try:
                assert (Liste_Cases[coord_i][coord_j]["Biome"] != 2)
                assert (Liste_Cases[coord_i][coord_j]["etat"] == "Vierge")
            except AssertionError:
                coord_i = random.randint(0, len(Liste_Cases) - 1)
                coord_j = random.randint(0, len(Liste_Cases) - 1)
            Liste_Cases[coord_i][coord_j]["etat"] = "Brule"
            Liste_Cases[coord_i][coord_j]["Intensite du feu"] = 1
            break
    return Liste_Cases

if __name__ == '__main__' :
    print('hi')
            

