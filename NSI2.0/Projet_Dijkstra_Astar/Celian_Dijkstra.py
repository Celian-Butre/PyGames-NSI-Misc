from GRAPH import GRAPH
import math
class Dijkstra(GRAPH):    
    def Dijkstra(self, startPoint, endPoint):
        #creation d'un dictionnaire avec chemin le plus court
        dictDistance = {}
        for x in self.dictAdj:
            if x == startPoint:
                dictDistance[x] = (0, [x])
            else:
                dictDistance[x] = (math.inf,[])
        #variables nécessaire pour la première itération de la boucle pour
        closestPoint = startPoint
        distanceBetween = 0
        untreatedPoints = []
        treatedPoints = []
        for i in range(len(self.listPoint)):
            untreatedPoints.append(self.listPoint[i])
        #tant que le point le plus proche non traité n'est pas le point final
        while closestPoint != endPoint:
            #retirer le point traité
            untreatedPoints.remove(closestPoint)
            treatedPoints.append(closestPoint)
            #obtenir la liste des voisins
            neighborPoints = self.visiterSommet(closestPoint)
            #mettre a jour les voisins
            for i in range(len(neighborPoints)):
                #obtenir la distance entre les voisins et le point le plus proche
                for j in range(len(self.dictAdj[closestPoint])):
                    if self.dictAdj[closestPoint][j][0] == neighborPoints[i]:
                        distanceBetween = self.dictAdj[closestPoint][j][1]
                #mettre a jour la distance et le chemin si il est favorable
                if dictDistance[neighborPoints[i]][0] > dictDistance[closestPoint][0] + distanceBetween:
                        dictDistance[neighborPoints[i]] = (dictDistance[closestPoint][0] + distanceBetween, dictDistance[closestPoint][1] + [neighborPoints[i]])
            #trouver le nouveau point le plus proche
            minimum = dictDistance[untreatedPoints[0]]
            minimumPoint = untreatedPoints[0]
            for i in range(len(untreatedPoints)):
                if dictDistance[untreatedPoints[i]] < minimum and dictDistance[untreatedPoints[i]] != -1:
                    minimum = dictDistance[untreatedPoints[i]]
                    minimumPoint = untreatedPoints[i]
            closestPoint = minimumPoint
        #rendre la distance la plus court entre le point de départ et le point d'arrivée en plus du chemin
        treatedPoints.append(closestPoint)
        self.printDistances(dictDistance, endPoint, treatedPoints)
        
    def printDistances(self, dictDistance, endPoint, treatedPoints):
        print("Voici la distance pour aller au point d'arrivé ", endPoint, ": ", dictDistance[endPoint][0], end = '. ')
        print("Le chemin est: ", dictDistance[endPoint][1][0], end = '')
        for i in range(len(dictDistance[endPoint][1]) - 1):
            print(" -->", dictDistance[endPoint][1][i+1], end = '')
        print('')
        print("Voici les points pour lesquelles un chemin optimale a été trouvé")
        for x in treatedPoints:
            print(x, ' est à une distance minimum de ', dictDistance[x][0], ' en passant par: ', dictDistance[x][1][0], end = '')
            for i in range(len(dictDistance[x][1]) - 1):
                print (' --> ', dictDistance[x][1][i+1], end = '')
            print('')
        infinits = 0
        for x in dictDistance:
            if dictDistance[x][0] == math.inf:
                infinits += 1
        if len(treatedPoints) + infinits != len(dictDistance):
            print("Voici les points pour lesquelles un chemin a été trouvé, mais qui n'est peut-être pas optimal")
        distancesOver = []
        for x in dictDistance:
            if (not (x in treatedPoints)) and (x != endPoint):
                if dictDistance[x][0] != math.inf:
                    distancesOver.append(dictDistance[x][0])
        distancesOver.sort()
        for i in range(len(distancesOver)):
            for x in dictDistance:
                if dictDistance[x][0] == distancesOver[i]:
                    print(x, ' est à une distance minimum de ', dictDistance[x][0], ' en passant par: ', dictDistance[x][1][0], end = '')
                    for j in range(len(dictDistance[x][1]) - 1):
                        print (' --> ', dictDistance[x][1][j+1], end = '')
                    print('')
        if infinits != 0:
            print("Voici les points pour lesquelles on a eu la flemme de trouver un chemin, (c'est trop loin, j'y vais pas)")
            for x in dictDistance:
                if dictDistance[x][0] == math.inf:
                    print(x)
                
    def DijkstraPseudo(self, startPoint, endPoint):
        dictDistance = self.createDictShortPath(startPoint) #creation d'un dictionnaire avec chemin le plus court
        (closestPoint, distanceBetween, untreatedPoints) = self.initiateFirstWhile(startPoint) #variables nécessaire pour la première itération de la boucle pour
        while closestPoint != endPoint: #tant que le point le plus proche non traité n'est pas le point final
            untreatedPoints.remove(closestPoint) #retirer le point traité
            neighborPoints = self.visiterSommet(closestPoint)#obtenir la liste des voisins
            for i in range(len(neighborPoints)):#mettre a jour les voisins
                distanceBetween = self.getDistance(neighborPoints, closestPoint, i) #obtenir la distance entre les voisins et le point le plus proche
                dictDistance = self.updateDistance(dictDistance, distanceBetween, neighborPoints, closestPoint, i) #mettre a jour la distance et le chemin si il est favorable
            closestPoint = self.findClosest(dictDistance, untreatedPoints, i)#trouver le nouveau point le plus proche
        return(dictDistance[endPoint]) #rendre la distance la plus court entre le point de départ et le point d'arrivée en plus du chemin
            
    def createDictShortPath(self, startPoint):
        dictDistance = {}
        for x in self.dictAdj:
            if x == startPoint:
                dictDistance[x] = (0, [x])
            else:
                dictDistance[x] = (math.inf,[])
        return(dictDistance)
    
    def initiateFirstWhile(self,startPoint):
        closestPoint = startPoint
        distanceBetween = 0
        untreatedPoints = []
        for i in range(len(self.listPoint)):
            untreatedPoints.append(self.listPoint[i])
        return(closestPoint, distanceBetween, untreatedPoints)
    
    def getDistance(self,neighborPoints, closestPoint, i):
        for j in range(len(self.dictAdj[closestPoint])):
            if self.dictAdj[closestPoint][j][0] == neighborPoints[i]:
                distanceBetween = self.dictAdj[closestPoint][j][1]
        return(distanceBetween)
    
    def updateDistance(self, dictDistance, distanceBetween, neighborPoints, closestPoint, i):
        if dictDistance[neighborPoints[i]][0] > dictDistance[closestPoint][0] + distanceBetween:
                        dictDistance[neighborPoints[i]] = (dictDistance[closestPoint][0] + distanceBetween, dictDistance[closestPoint][1] + [neighborPoints[i]])
        return(dictDistance)
    
    def findClosest(self, dictDistance, untreatedPoints, i):
        minimum = dictDistance[untreatedPoints[0]]
        minimumPoint = untreatedPoints[0]
        for i in range(len(untreatedPoints)):
            if dictDistance[untreatedPoints[i]] < minimum and dictDistance[untreatedPoints[i]] != -1:
                minimum = dictDistance[untreatedPoints[i]]
                minimumPoint = untreatedPoints[i]
        closestPoint = minimumPoint
        return(closestPoint)
        
if __name__ == '__main__':
    wikiDictAdj = {'A' : [('B', 85),('C', 217),('E', 173)], 'B' : [('A', 85),('F', 80)], 'C' : [('A', 217),('G', 186),('H', 103)], 'D' : [('H', 183)], 'E' : [('A', 173),('J', 502)], 'F' : [('B', 80),('I', 250)], 'G' : [('C', 186)], 'H' : [('C', 103),('D', 183),('J', 167)], 'I' : [('F', 250),('J', 84)], 'J' : [('E', 502),('H', 167),('I', 84)]}
    
    GWikipedia = Dijkstra(wikiDictAdj)
    print(GWikipedia.listPoint)
    print(GWikipedia.matAdj)
    GWikipedia.Dijkstra('A', 'J')
    GWikipedia.Dijkstra('A', 'D')
    GWikipedia.Dijkstra('A', 'B')
    """
    print(GWikipedia.DijkstraPseudo('A', 'J'))
    print(GWikipedia.DijkstraPseudo('A', 'D'))
    """
    Exemple2matAdj = [[-1, -1, -1, 42, -1, 12],[-1, -1, 13, 2, -1, -1],[-1, 13, -1, 17, 15, -1],[42, 2, 17,-1,-1,-1],[-1, -1, 15, -1, -1,36],[12, -1, -1, -1, 36, -1]]
    Exemple2listPoint = ['A', 'B', 'C', 'D', 'E', 'F']
    
    GExemple2 = Dijkstra(matAdj = Exemple2matAdj, listPoint = Exemple2listPoint)
    """
    print(GExemple2.DijkstraPseudo('A', 'C'))
    """
    GExemple2.Dijkstra('A', 'C')
    
    
    Exemple3dictAdjEuclid = {'A' : ((0, 0), ['B', 'F']), 'B' : ((1, 1), ['A', 'C', 'F']), 'C' : ((2, 1), ['B', 'D']), 'D' : ((1, 3), ['C', 'E']), 'E' : ((3, 2), ['D', 'F']), 'F' : ((0, 2), ['A', 'E'])}
    GExemple3 = Dijkstra(dictAdjEuclid = Exemple3dictAdjEuclid)
    """
    print(GExemple3.DijkstraPseudo('A', 'D'))
    """
    GExemple3.Dijkstra('A', 'D')