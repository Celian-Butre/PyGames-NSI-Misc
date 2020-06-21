import random, math
random.seed(1)
setMatrix = str(input("set Matrix manually? True or False   "))
if setMatrix == "False":
    RMatrix = [[-1,-1,-1,-1,-1,-1,0,-1,-1,100],[-1,-1,0,-1,-1,-1,-1,-1,-1,-1],[-1,0,-1,0,-1,-1,-1,-1,-1,-1],[-1,-1,0,-1,0,-1,-1,-1,-1,100],[-1,-1,-1,0,-1,-1,0,-1,-1,-1],[-1,-1,-1,-1,-1,-1,0,-1,-1,-1],[0,-1,-1,-1,0,0,-1,0,-1,-1],[-1,-1,-1,-1,-1,-1,0,-1,0,-1],[-1,-1,-1,-1,-1,-1,-1,0,-1,-1],[0,-1,-1,0,-1,-1,-1,-1,-1,100]]
else:
    RMatrix = []
    howManyRooms = int(input("How many rooms including outside   "))
    for i in range(howManyRooms):
        RMatrix.append([])
        for j in range(howManyRooms):
            RMatrix[i].append(-1)
    for i in range(howManyRooms):
        message = "how many rooms (and outside) are ajacent to room ", str(i)
        howManyConnections = int(input(message))
        for j in range(howManyConnections):
            doorConnection = int(input("List the rooms 1 by 1   "))
            RMatrix[i][doorConnection] = 0
    OutsideNumb = int(input("What is the Outside's numbe?   "))
    RMatrix[OutsideNumb][OutsideNumb] = 100
    RoomsLeadingOutside = int(input("How Many Rooms lead to outside  "))
    for i in range(RoomsLeadingOutside):
        RoomsThatLeadOutside = int(input("list 1 by 1 the rooms leading outside  "))
        RMatrix[RoomsThatLeadOutside][OutsideNumb] = 100
class QMatrix:
    def initiateQ(self):
        self.QMatrix = []
        for i in range(len(RMatrix)):
            self.QMatrix.append([])
            for j in range(len(RMatrix[i])):
                self.QMatrix[i].append(0)
Agent = QMatrix()
Agent.initiateQ()

lWin = 0
for i in range(len(RMatrix)):
    for j in range(len(RMatrix[i])):
        if RMatrix[i][j] == 100:
            lWin = j

Gamma = 0.8
for i in range (1000):
    NextSquare = random.randint(0,len(RMatrix)-1)
    CurrentSquare = -1
    while CurrentSquare != lWin:
        CurrentSquare = NextSquare
        allowed = False
        while allowed == False:
            allowed = True
            NextSquare = random.randint(0,len(RMatrix)-1)
            if RMatrix[CurrentSquare][NextSquare] == -1:
                allowed = False
        BestOption = -1
        for j in range(len(RMatrix)):
            Option = Agent.QMatrix[NextSquare][j]
            if BestOption <= Option:
                BestOption = Option
        Agent.QMatrix[CurrentSquare][NextSquare] = int(RMatrix[CurrentSquare][NextSquare] + Gamma * BestOption)
Max = 0
for i in range(len(Agent.QMatrix)):
    for j in range(len(Agent.QMatrix[i])):
        if Agent.QMatrix[i][j] > Max:
            Max = Agent.QMatrix[i][j]

for i in range(len(Agent.QMatrix)):
    for j in range(len(Agent.QMatrix[i])):
        Agent.QMatrix[i][j] = (100*Agent.QMatrix[i][j])//Max
while True:
    correctAnswer = False
    while correctAnswer == False:
        startingSquare = str(input("Which room does the agent start in?   "))
        isInt = True
        if len(startingSquare) == 0:
            isInt = False
        for i in range(len(startingSquare)):
            if startingSquare[i] != "0" and startingSquare[i] != "1" and startingSquare[i] != "2" and startingSquare[i] != "3" and startingSquare[i] != "4" and startingSquare[i] != "5" and startingSquare[i] != "6" and startingSquare[i] != "7" and startingSquare[i] != "8" and startingSquare[i] != "9":
                isInt = False
        if isInt == True:
            if int(startingSquare) >= 0 and int(startingSquare) < len(RMatrix) - 1:
                correctAnswer = True
    currentSquare = int(startingSquare)
    print("If the agent starts in the room ", currentSquare, " he will go through ", currentSquare, end = "")
    while currentSquare != lWin:
        BestOption = -1
        for j in range(len(RMatrix)):
            Option = Agent.QMatrix[currentSquare][j]
            if BestOption <= Option:
                BestOption = Option
                BestSquare = j
        currentSquare = BestSquare
        print (" ----> ", currentSquare, end = "")
    print("")