import os

def enleverHistoriquePartiesPrecedentes (Historique_Stockage):
    if os.path.exists(Historique_Stockage):
        os.remove(Historique_Stockage)
    
def recupererHistorique (Historique_Stockage):
    historique = []
    try :
        with open(Historique_Stockage, "r") as f:
            for ligne in f :
                l = ligne.split()
                historique.append(l)                                    # ligne.split() est une liste comprenant tous les mots (separes par un espace)
    except FileNotFoundError :                                                      # Dans le cas ou le fichier n' existe pas (et dans ce cas, la liste reste vide et revient a creer le tout premier fichier)
        pass                                                                        # Si le fichier n' existe pas, on ne recupere rien et ne fait donc rien, et le fichier sera cree lors de l'appel de la fonction ecrireScore
    return historique

def ecrireHistorique (Liste_Cases, Historique_Stockage):
    l = [recupererHistorique(Historique_Stockage), Liste_Cases]
    f = open(Historique_Stockage, "w")
    f.write(str(l))                                         # Permet de marquer une separation entre chaque grille
    f.close()


