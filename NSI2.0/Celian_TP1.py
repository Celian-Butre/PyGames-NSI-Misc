class ArbreTernaire:
    def __init__(self, racine, fils_aine = None, fils_cadet = None, fils_benjamin = None):
        self.racine = racine
        self.fils_aine = fils_aine
        self.fils_cadet = fils_cadet
        self.fils_benjamin = fils_benjamin
    
    def est_ternaire(self):
        if self.fils_aine == None and self.fils_cadet == None and self.fils_benjamin == None:
            #print(1, self.racine)
            return(True)
        
        if len(self.fils_aine.racine) == 0 or len(self.fils_benjamin.racine) == 0:
            #print(2, self.racine)
            return(False)
        
        if self.racine == self.fils_aine.racine or self.racine == self.fils_aine.racine or self.racine == self.fils_aine.racine:
            #print(3, self.racine)
            return(False)
        
        if len(self.racine) == 2 and self.fils_cadet != '':
            return(False)
        
        #print(1)
        #aineTrue
        aineTrue = False
        for i in range(len(self.racine)):
            #print(2)
            if self.racine[:i] == self.fils_aine.racine:
                #print(4, self.racine)
                aineTrue = True
        
        benjaminTrue = False
        for i in range(len(self.racine)):
            if self.racine[i:] == self.fils_benjamin.racine:
                #print(5, self.racine)
                benjaminTrue = True
                
        cadetTrue = False
        if self.fils_cadet.racine in self.racine:
            #print(6, self.racine)
            cadetTrue = True
        
        if aineTrue == False or cadetTrue == False or benjaminTrue == False:
            #print(7, self.racine)
            return(False)
        
        if self.fils_aine.est_ternaire() == False or self.fils_cadet.est_ternaire() == False or self.fils_benjamin.est_ternaire() == False:
            #print(8, self.racine)
            return(False)
        #print(9, self.racine)
        return(True)
        
    
    def parcours_profondeur(self):
        print(self.racine)
        if (self.fils_aine != None) :
            self.fils_aine.parcours_profondeur()
        if (self.fils_cadet != None) :
            self.fils_cadet.parcours_profondeur()
        if (self.fils_benjamin != None) :
            self.fils_benjamin.parcours_profondeur()
    
def parcours_largeur(tree1, liste = [], liste2 = []):
    if liste == []:
        liste.append(tree1)
    if tree1.fils_aine != None:
        liste.append(tree1.fils_aine)
    if tree1.fils_cadet != None:    
        liste.append(tree1.fils_cadet)
    if tree1.fils_benjamin != None:    
        liste.append(tree1.fils_benjamin)
    liste2.append(liste.pop(0).racine)
    if liste != []:
        parcours_largeur(liste[0], liste, liste2)
    
    return (liste2)
           
if __name__ == '__main__':
    A1 = ArbreTernaire('abcde', ArbreTernaire('ab', ArbreTernaire('a', None, None, None), ArbreTernaire('', None, None, None), ArbreTernaire('b', None, None, None)), ArbreTernaire('bcd', ArbreTernaire('b', None, None, None), ArbreTernaire('c', None, None, None), ArbreTernaire('d', None, None, None)), ArbreTernaire('de', ArbreTernaire('d', None, None, None), ArbreTernaire('', None, None, None), ArbreTernaire('e', None, None, None)))


    print(A1.est_ternaire())
    A1.parcours_profondeur()
    print(parcours_largeur(A1))