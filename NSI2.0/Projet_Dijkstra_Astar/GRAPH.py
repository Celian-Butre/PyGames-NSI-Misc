class GRAPH:
    def __init__(self, dictAdj = {}, matAdj = [], listPoint = [], dictAdjEuclid = {}):
        """
        fournir soit dictAdj soit matAdj et listPoint soit dictAdjEuclid
        dictAdj = {'A': [('B', 13), ('C', 15)], 'B': [('A', 13)],'C':[('A', 15)]}
        matAdj = [[-1,13,15],[13,-1,-1],[15,-1,-1]]
        listPoint = ['A', 'B', 'C']
        dictAdjEuclid = {'A': ((0,0),['B', 'C']), 'B': ((13,0),['A']),'C':((0,15),['A'])}
        """
        if matAdj != [] and listPoint != []:
            self.matAdj = matAdj
            self.listPoint = listPoint
            self.dictAdj = self.createDictAdj()
        elif dictAdj != {}:
            self.dictAdj = dictAdj
            self.matAdj, self.listPoint = self.createMatAdj()
        elif dictAdjEuclid != {}:
            self.dictAdjEuclid = dictAdjEuclid
            self.dictAdj = self.createDictAdjFromEuclid()
            self.matAdj, self.listPoint = self.createMatAdj()
            
    def createDictAdjFromEuclid(self):
        listPointTemp = []
        for x in self.dictAdjEuclid:
            listPointTemp.append(x)
        dictAdj = {}
        for i in self.dictAdjEuclid:
            tempList = []
            for j in range(len(self.dictAdjEuclid[i][1])):
                tempList.append((self.dictAdjEuclid[i][1][j],(((self.dictAdjEuclid[i][0][0]-self.dictAdjEuclid[self.dictAdjEuclid[i][1][j]][0][0])**2+(self.dictAdjEuclid[i][0][1]-self.dictAdjEuclid[self.dictAdjEuclid[i][1][j]][0][1])**2)**0.5)))
            dictAdj[i] = tempList
        return(dictAdj)
            
    def createDictAdj(self):
        dictAdj = {}
        for i in range (len(self.listPoint)):
            tempList = []
            for j in range(len(self.listPoint)):
                if self.matAdj[i][j] != -1:
                    tempList.append((self.listPoint[j],self.matAdj[i][j]))
            dictAdj[self.listPoint[i]] = tempList
        return(dictAdj)
                    
    def createMatAdj(self):
        listPoint = []
        for x in self.dictAdj:
            listPoint.append(x)
        matAdj = []
        for i in range(len(self.dictAdj)):
            matAdj.append([])
            for j in range(len(listPoint)):
                found = False
                for k in range(len(self.dictAdj[listPoint[i]])):
                    if self.dictAdj[listPoint[i]][k][0] == listPoint[j]:
                        found = self.dictAdj[listPoint[i]][k][1]
                if found == False:
                    matAdj[i].append(-1)
                else:
                    matAdj[i].append(found)
        return((matAdj, listPoint))
    
    def visiterSommet(self, startPoint):
        listeSommet = []
        for i in range(len(self.dictAdj[startPoint])):
            listeSommet.append(self.dictAdj[startPoint][i][0])
        return(listeSommet)
    
if __name__ == '__main__':
    GmatAdj = [[-1,13,15],[13,-1,-1],[15,-1,-1]]
    GlistPoint = ['A', 'B', 'C']
    G = GRAPH(matAdj = GmatAdj, listPoint = GlistPoint)
    #assert(G1dictAdj == G.dictAdj)
    print("mat")
    print(G.dictAdj)
    G1dictAdj = {'A': [('B', 13), ('C', 15)], 'B': [('A', 13)],'C':[('A', 15)]}
    G1 = GRAPH(G1dictAdj)
    print("dict")
    print(G1.listPoint)
    print(G1.matAdj)
    G2dictAdjEuclid = {'A': ((0,0),['B', 'C']), 'B': ((13,0),['A']),'C':((0,15),['A'])}
    G2 = GRAPH(dictAdjEuclid = G2dictAdjEuclid)
    print("euclid")
    print(G2.dictAdj)
    print(G2.listPoint)
    print(G2.matAdj)