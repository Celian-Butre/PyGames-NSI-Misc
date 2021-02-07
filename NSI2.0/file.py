file = ['Machin', 'Chose', 'Truc']

def isVide(file):
    if file == []:
        return (True)
    return (False)
    #recuperation: fileVide = isVide(file)

def push(file, item):
    #copiage à la main
    filefonction = []
    for i in range (length(file)):
        filefonction.append(file[i])
    
    #push
    filefonction.append(item)
    
    #return
    return (filefonction)
    #recuperation: file = push(file, item)

def pop(file):
    if isVide(file) == False:
        #copiage à la main sauf l'item pop
        filefonction = []
        for i in range (length(file) - 1):
            filefonction.append(file[i+1])
    else:
        filefonction = []
    
    if isVide(file) == False:
        #recupere l'item
        item = file[0]
    else:
        item = None
        print('La file est vide')
    #return
    return(filefonction, item)
    #recuperation: file, item = pop(file) ou file = pop(file)[0]
    
def sommet(file):
    return (file[0])
    #recuperation: sommet = sommet(file)
    
def length(file):
    return (len(file))
    #recuperation: length = length(file)
    
def clearfile(file):
    #copiage à la main
    filefonction = []
    for i in range (length(file)):
        filefonction.append(file[i])
    
    for i in range (length(file)):
        filefonction = pop(filefonction)[0]
    
    
    if isVide(file) == True:
        print('La file etait deja vide')
    
    #return
    return (filefonction)
    #recuperation file = clearfile(file)
    

    
    
#fileVide = isVide(file)
#file = push(file, 'bidule')
#file, item = pop(file)
#sommet = sommet(file)
#length = length(file)
#file = clearfile(file)
print(file)