from ARBRE import ARBRE

class CompressionHuffman(ARBRE):
    def __init__(self, file = 0):
        if file != 0:
            self.file = file
            with open(self.file) as f:
                self.text = f.read()
        self.listChar = None
        self.frequencyChar = None
        self.compressionTree = None
        self.compressedText = None
        self.decompressedText = None
        
    def generateCharacterList(self):
        listChar = []
        currentChar = 0
        while currentChar < len(self.text): 
            if not (self.text[currentChar] in listChar):
                listChar.append(self.text[currentChar])
            currentChar += 1
        self.listChar = listChar
        
    def generateCharacterFrequency(self):
        frequencyChar = [(x, 0) for x in self.listChar]
        currentChar = 0
        while currentChar < len(self.text):
            for x in range(len(frequencyChar)):
                if frequencyChar[x][0] == self.text[currentChar]:
                    frequencyChar[x] = (frequencyChar[x][0], frequencyChar[x][1]+1)
            currentChar += 1
        self.frequencyChar = frequencyChar
    
    def sortFrequencyList(self, liste):
        for i in range(len(liste)):
            for j in range(len(liste) - i - 1):
                if liste[j][1] > liste[j+1][1]:
                    liste[j],liste[j+1] = liste[j+1],liste[j]
        #maybe put a return instead of directly affecting variable
        liste.reverse()
    
    def generateTree(self):
        import copy
        frequencyCharMutable = copy.deepcopy(self.frequencyChar)
        while len(frequencyCharMutable) > 1:
            self.sortFrequencyList(frequencyCharMutable)
            if type(frequencyCharMutable[-1][0]) is str:
                frequencyCharMutable.append((ARBRE(frequencyCharMutable[-1][0]), frequencyCharMutable.pop(-1)[1]))
            if type(frequencyCharMutable[-2][0]) is str:
                frequencyCharMutable.append((ARBRE(frequencyCharMutable[-2][0]), frequencyCharMutable.pop(-2)[1]))
            frequencyCharMutable.append( (ARBRE(root = (frequencyCharMutable[-2][0], frequencyCharMutable[-1][0]), left = frequencyCharMutable[-2][0], right = frequencyCharMutable[-1][0]), frequencyCharMutable.pop(-2)[1] + frequencyCharMutable.pop(-1)[1] ) )
        self.compressionTree = frequencyCharMutable[0][0]
        
    def compress(self):
        if self.listChar == None:
            self.generateCharacterList()
        if self.frequencyChar == None:
            self.generateCharacterFrequency()
        if self.compressionTree == None:
            self.generateTree()
        currentChar = 0
        compressedText = ''
        currentTree = self.compressionTree
        while currentChar < len(self.text):
            if currentTree.giveRoot() == self.text[currentChar]:
                currentChar += 1
                currentTree = self.compressionTree
            elif self.isItemIn(currentTree.giveLeft(), self.text[currentChar]):
                compressedText += '0'
                currentTree = currentTree.giveLeft()
            else:
                compressedText += '1'
                currentTree = currentTree.giveRight()
        self.compressedText = compressedText
    
    def decompress(self):
        currentChar = 0
        decompressedText = ''
        currentTree = self.compressionTree
        while currentChar < len(self.compressedText):
            if currentTree.isLeaf():
                decompressedText += currentTree.giveRoot()
                currentTree = self.compressionTree
            elif self.compressedText[currentChar] == '0':
                currentChar += 1
                currentTree = currentTree.giveLeft()
            else:
                currentChar += 1
                currentTree = currentTree.giveRight()
        self.decompressedText = decompressedText
                
if __name__ == "__main__":
    LOTF = CompressionHuffman("longerRandomText.txt")
    """
    print(len(LOTF.text))
    LOTF.generateCharacterList()
    #print(LOTF.listChar)
    LOTF.generateCharacterFrequency()
    #print(LOTF.frequencyChar)
    LOTF.sortFrequencyList(LOTF.frequencyChar)
    print(LOTF.frequencyChar)
    LOTF.generateTree()
    print(LOTF.compressionTree.giveLeft().giveLeft().giveLeft().giveLeft().giveLeft().giveRoot())
    print(LOTF.prefixPrint(LOTF.compressionTree))
    print(LOTF.isItemIn(LOTF.compressionTree.giveRight(), 'r'))
    """
    LOTF.compress()
    print(LOTF.compressedText)
    LOTF.decompress()
    print(LOTF.decompressedText)
    #for i in range(len(LOTF.listChar)):
        #print(LOTF.listChar[i], end = '')
    #LOTF.generateEncodingAlphabet()
    #LOTF.compress()
    #print(LOTF.conversionTable)
    #print(LOTF.compressedText)
    #LOTF.decompress()
    #print(LOTF.decompressedText)