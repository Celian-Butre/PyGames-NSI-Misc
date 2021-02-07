class textAnalysis:
    def __init__(self, file):
        ALPHABET = [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f'), ('G', 'g'), ('H', 'h'), ('I', 'i'), ('J', 'j'), ('K', 'k'), ('L', 'l'), ('M', 'm'), ('N', 'n'), ('O', 'o'), ('P', 'p'), ('Q', 'q'), ('R', 'r'), ('S', 's'), ('T', 't'), ('U', 'u'), ('V', 'v'), ('W', 'w'), ('X', 'x'), ('Y', 'y'), ('Z', 'z')]

        USEFULLCHARS = [' ', ',', ';' '-', ':', '.', '!', '?']
        self.file = file
        with open(self.file) as f:
            self.text = f.read()
        
    def generateWordList(self):
        tempWordList = self.text.split()
        wordList = []
        for i in range (len(tempWordList)):
            if not(tempWordList[i] in wordList):
                wordList.append(tempWordList[i])
        
        return(wordList)
        
    
    def generateLetterList(self):
        letterList = []
        for i in range (len(self.lowerCaseText)):
            if not(self.lowerCaseText[i] in letterList):
                for j in range(len(ALPHABET)):
                    if self.lowerCaseText[i] == ALPHABET[j][1]:
                        letterList.append(self.lowerCaseText[i])
        self.letterList = letterList
        return(letterList)
    
    def generateWordFrequency(self):
        wordFrequency = []
        for i in range (len(self.wordList)):
            wordFrequency.append((self.wordList[i], 0))
        for i in range (len(self.text.split())):
            for j in range(len(wordFrequency)):
                if wordFrequency[j][0] == self.text.split()[i]:
                    wordFrequency[j] = (wordFrequency[j][0], wordFrequency[j][1] + 1)
        #sort list
        for i in range (1, len(wordFrequency)):
            combiendécaller = 0
            for j in range(i):
                if wordFrequency[i][1] < wordFrequency[i-j-1][1]:
                    combiendécaller += 1
            save = wordFrequency[i]
            for j in range (combiendécaller):
                wordFrequency[i-j] = wordFrequency[i-j-1]
            wordFrequency[i-combiendécaller] = save
        wordFrequency.reverse()
        return(wordFrequency)
            
    def generateLetterFrequency(self):
        letterFrequency = []
        for i in range (len(self.letterList)):
            letterFrequency.append((self.letterList[i], 0))
        for i in range (len(self.lowerCaseText)):
            for j in range(len(letterFrequency)):
                if letterFrequency[j][0] == self.lowerCaseText[i]:
                    letterFrequency[j] = (letterFrequency[j][0], letterFrequency[j][1] + 1)
        #sort list
        for i in range (1, len(letterFrequency)):
            combiendécaller = 0
            for j in range(i):
                if letterFrequency[i][1] < letterFrequency[i-j-1][1]:
                    combiendécaller += 1
            save = letterFrequency[i]
            for j in range (combiendécaller):
                letterFrequency[i-j] = letterFrequency[i-j-1]
            letterFrequency[i-combiendécaller] = save
        letterFrequency.reverse()
        self.letterFrequency = letterFrequency
        return(letterFrequency)
    
    def generateLowerCaseText(self):
        lowerCaseText = ''
        for i in range(len(self.text)):
            for j in range(len(ALPHABET)):
                if self.text[i] == ALPHABET[j][0] or self.text[i] == ALPHABET[j][1]:
                    lowerCaseText += ALPHABET[j][1]
            for j in range(len(USEFULLCHARS)):
                if self.text[i] == USEFULLCHARS[j]:
                    lowerCaseText += USEFULLCHARS[j]
            if self.text[i] == '\n':
                lowerCaseText += ' '
        self.lowerCaseText = lowerCaseText
        return(lowerCaseText)
                    
    def generateUpperCaseText(self):
        pass
        
    def printFrequency(self, frequencedList):
        maxLen = len(str(frequencedList[0][1]))
        for i in range(len(frequencedList)):
            string = str(frequencedList[i][1])
            numb = (maxLen - len(str(frequencedList[i][1])) + 2)
            string2 = str(' ' * numb)
            string += string2
            string += str(frequencedList[i][0])
            print(string)