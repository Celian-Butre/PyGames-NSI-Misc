NIL = None

class ListeAbs:
    def __init__(self, item, son = NIL):
        self.item = item
        self.son = son
    
    def printList(self, res = ''):
        if self.son == NIL:
            res += (str(self.item)+ ' --> ')
            print(res[: -5])
        else:
            res += (str(self.item)+ ' --> ')
            self.son.printList(res)
    
    def removeLink(self):
        if self.son == NIL:
            self.item = NIL
        else:
            self.item = self.son.item
            self.son = self.son.son
    
    def addLink(self, item):
        if self.son == NIL:
            self.son = ListeAbs(item)
        else:
            self.son = ListeAbs(item,self.son)
        

if __name__ == '__main__':
    listeTest = ListeAbs(5,ListeAbs(4,ListeAbs(3,ListeAbs(2,ListeAbs(1,ListeAbs(0))))))
    listeTest.printList()
    listeTest.son.removeLink()
    listeTest.printList()
    listeTest.son.son.son.addLink(4.5)
    listeTest.printList()
    