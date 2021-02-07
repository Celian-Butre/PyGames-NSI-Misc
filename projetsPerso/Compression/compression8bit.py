class Compression8bit:
    def __init__(self, file = 0):
        if file != 0:
            self.file = file
            with open(self.file) as f:
                self.text = f.read()
                
        self.listChar = None
        self.bitLength = None
        self.conversionTable = None
        self.listChar = None

    def generateCharacterList(self):
        listChar = []
        currentChar = 0
        while currentChar < len(self.text): 
            if not (self.text[currentChar] in listChar):
                listChar.append(self.text[currentChar])
            currentChar += 1
        self.listChar = listChar
        
    def generateEncodingAlphabet(self):
        import math
        self.bitLength = math.ceil(math.log(len(self.listChar), 2))
        self.conversionTable = [(('0'*(self.bitLength-len((bin(i)[2:]))) + (bin(i)[2:])), self.listChar[i]) for i in range(len(self.listChar))]
    
    def compress(self):
        if self.listChar == None:
            self.generateCharacterList()
        if self.bitLength == None or self.conversionTable == None:
            self.generateEncodingAlphabet()
        encodedText = ""
        currentChar = 0
        while currentChar < len(self.text):
            for x in self.conversionTable:
                if x[1] == self.text[currentChar]:
                    encodedText += x[0]
            currentChar += 1
        self.compressedText = encodedText
        
    def decompress(self):
        decodedText = ""
        currentChar = 0
        while currentChar < len(self.compressedText):
            for x in self.conversionTable:
                if x[0] == self.compressedText[currentChar:currentChar+self.bitLength]:
                    decodedText += x[1]
            currentChar += self.bitLength
        self.decompressedText = decodedText
            
if __name__ == "__main__":
    #"""
    LOTF = Compression8bit("longerRandomText.txt")
    LOTF.generateCharacterList()
    print(LOTF.listChar)
    #for i in range(len(LOTF.listChar)):
        #print(LOTF.listChar[i], end = '')
    LOTF.generateEncodingAlphabet()
    LOTF.compress()
    print(LOTF.conversionTable)
    print(LOTF.compressedText)
    LOTF.decompress()
    print(LOTF.decompressedText)
    #"""