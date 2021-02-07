arbreVide = None

class Knot: #class noeud
    def __init__(self, item, arbre1, arbre2):
        self.item = item
        self.arbre1 = arbre1
        self.arbre2 = arbre2
    
    def giveRacine(self):
        return(self.item)
    
    def giveTree1(self):
        return(self.arbre1)
    
    def giveTree2(self):
        return(self.arbre2)

class Arbre: #classe arbre
    def __init__(self, knot):
        self.knot = knot
    
    def giveKnot(self):
        return(self.knot)
    
    def giveRacine(self):
        return(self.knot.giveRacine())
    
    def giveArbre1(self):
        return(self.knot.giveTree1())
    
    def giveArbre2(self):
        return(self.knot.giveTree2())
        
def cons(item, arbre1 = arbreVide, arbre2 = arbreVide): #fonction constructeur
    return Arbre(Knot(item, arbre1,arbre2))

def hauteur(arbre): #fonction hauteur
    thisTree = arbre
    depth = 0
    while thisTree != arbreVide:
        thisTree = thisTree.giveKnot().giveTree1()
        depth += 1
    return(depth)

def taille(arbre): #fonction taille (nombre d'éléments)
    thisTree = arbre
    if thisTree.giveArbre1() == None:
        return(1)
    else:
        size1 = taille(thisTree.giveArbre1())
        size2 = taille(thisTree.giveArbre2())
        return(size1 + size2 + 1)

def generatePerfectTree(level): #creer un arbre (parfait)
    treeMatrix = []
    treeMatrix.append([])
    for i in range(2**level):
        treeMatrix[0].append(arbreVide)
    for i in range(level):
        numberOfTreesInLevel = 2**(level-i-1)
        firstNumberOnLevel = 2**(level-i-1) - 1
        treeMatrix.append([])
        for j in range(numberOfTreesInLevel):
            treeMatrix[i+1].append(cons(firstNumberOnLevel + j, treeMatrix[i][j*2], treeMatrix[i][j*2+1]))
    return(treeMatrix[-1][-1])

def affichage(arbre):
    thisTree = arbre
    newlist = [arbre.giveRacine()]
    if thisTree.giveArbre1() == None and thisTree.giveArbre2() == None:
        return(newlist)
    list1 = []
    list2 = []
    if thisTree.giveArbre1() != None:
        list1 = affichage(thisTree.giveArbre1())
    if thisTree.giveArbre2() != None:
        list2 = affichage(thisTree.giveArbre2())
    newlist = newlist + list1 + list2
    return(newlist)

A = cons(1)
B = cons(2)
C = cons(3)
D = cons(4)

E = cons(3,A,B)
F = cons(7,C,D)

G = cons(10,E,F)

print(hauteur(G))
perfTree = generatePerfectTree(3)
print(hauteur(perfTree))
print(taille(perfTree))
print(affichage(perfTree))