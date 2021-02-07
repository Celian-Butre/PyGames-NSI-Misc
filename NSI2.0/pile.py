pile = ['Machin', 'Chose', 'Truc']

def isVide(pile):
    if pile == []:
        return (True)
    return (False)
    #recuperation: pileVide = isVide(pile)

def push(pile, item):
    #copiage à la main
    pilefonction = []
    for i in range (length(pile)):
        pilefonction.append(pile[i])
    
    #push
    pilefonction.append(item)
    
    #return
    return (pilefonction)
    #recuperation: pile = push(pile, item)

def pop(pile):
    if isVide(pile) == False:
        #copiage à la main sauf l'item pop
        pilefonction = []
        for i in range (length(pile) - 1):
            pilefonction.append(pile[i])
    else:
        pilefonction = []
    
    if isVide(pile) == False:
        #recupere l'item
        item = pile[-1]
    else:
        item = None
        print('La pile est vide')
    #return
    return(pilefonction, item)
    #recuperation: pile, item = pop(pile) ou pile = pop(pile)[0]
    
def sommet(pile):
    return (pile[-1])
    #recuperation: sommet = sommet(pile)
    
def length(pile):
    return (len(pile))
    #recuperation: length = length(pile)
    
def clearPile(pile):
    #copiage à la main
    pilefonction = []
    for i in range (length(pile)):
        pilefonction.append(pile[i])
    
    for i in range (length(pile)):
        pilefonction = pop(pilefonction)[0]
    
    
    if isVide(pile) == True:
        print('La pile etait deja vide')
    
    #return
    return (pilefonction)
    #recuperation pile = clearPile(pile)
    

    
    
#pileVide = isVide(pile)
#pile = push(pile, 'bidule')
#pile, item = pop(pile)
#sommet = sommet(pile)
#length = length(pile)
pile = clearPile(pile)
print(pile)