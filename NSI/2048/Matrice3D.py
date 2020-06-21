#/Leopold
def matrice3D(matrice3D):
    save=open('sauvegarde.txt','a')
    save.write('\n')
    save.write(matrice3D)
    
    
    try :
        with open("sauvegarde.txt") as save:
            data = save.readlines()
            lastline = data[-1]

    except FileNotFoundError :
        pass
    
    save.close()

    return lastline

def clearMatrice():

    save = open("sauvegarde.txt","r+")
    save.truncate(0)
    save.close()
#\Leopold