import copy

class File:
    def __init__(self, listeDeDepart = []):
        """
        prend une liste de départ optionel
        """
        self.file = listeDeDepart
        self.length = 0
        fileClone = copy.deepcopy(listeDeDepart)
        while fileClone != []:
            self.length += 1
            fileClone.pop(0)
            
    def taille(self):
        """
        rend la taille actuelle de la file et prend rien apart le self
        """
        return(self.length)
    
    def ajouter(self, item):
        """
        prend l'objet et un item, et rend rien
        """
        self.file = self.file + [item]
        self.length += 1
        
    def __str__(self): #temporaire
        """
        est appelée lorsqu'on veut print, return une version string de la liste file
        """
        if self.estVide():
            return('File Vide')
        else:
            string = 'Tête '
            fileCopy = File(copy.deepcopy(self.file))
            for i in range(self.taille() - 1):
                string += str(fileCopy.extraire())
                string += '-->'
            string += str(self.oppose())
            string += ' queue'
            return(str(string))

    def extraire(self):
        """
        prend l'objet et rend/retire l'objet à défiler
        """
        if self.estVide() == True:
            return(None)
        self.length -= 1
        return(self.file.pop(0))
    
    def estVide(self):
        """
        rend True si la file est vide, False sinon
        """
        return(self.taille() == 0)
    
    def oppose(self):
        """
        permet de voir ce qui est au bout de la file
        """
        fileCopy = File(copy.deepcopy(self.file))
        a = None
        while not fileCopy.estVide():
            a = fileCopy.extraire()
        return(a)
    
    def occurence(self, item):
        """
        prend l'objet et une valeur en entrée et rend combien de fois elle est présent dans la File
        """
        fileCopy = File(copy.deepcopy(self.file))
        nb = 0
        while not fileCopy.estVide():
            a = fileCopy.extraire()
            if a == item:
                nb += 1
        return(nb)
        
if __name__ == '__main__':
    fileVide = File()
    fileTest = File([1,2,3,4,5])
    fileOccurence = File([1,1,1,3,3,3,5,7,11,11])
    print(fileTest.taille())
    print(fileTest)
    fileTest.ajouter(0)
    print(fileTest)
    print(fileTest.taille())
    print(fileTest.extraire())
    print(fileTest)
    print(fileTest.taille())
    print(fileVide.estVide())
    print(fileTest.estVide())
    print(fileVide.extraire())
    print(fileVide.oppose())
    print(fileTest.oppose())
    print(fileVide)
    print(fileTest)
    print(fileVide.occurence(3))
    print(fileTest.occurence(3))
    print(fileOccurence.occurence(1))
    print(fileOccurence.occurence(3))
    print(fileOccurence.occurence(5))
    print(fileOccurence.occurence(7))
    print(fileOccurence.occurence(11))
    print(fileOccurence)
    fileOccurence.ajouter(13)
    print(fileOccurence.oppose())