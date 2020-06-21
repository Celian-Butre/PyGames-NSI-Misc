#/Leopold
import time
listescore = []
listenames = []


scoreandnames = {}

file = open("highscores.txt", "r")


def recupererScores(file) :
    l = []
    try :
        with open("highscores.txt", "r") as file:
            for ligne in file :
                l.append(ligne.split())
    except FileNotFoundError :         
        pass

    file.close()
    
    
    return l

def scoretolist(recup, score):
    
    listescore = []
    for i in range (len(recup)):

        try:

            listescoreint = int(recup[i][2])
        
            listescore.append(listescoreint)

        except IndexError:
            pass 
    return listescore
        
def namestolist(recup, name):
    listenames = []
    for j in range (len(recup)):

        try:

            listenames.append(recup[j][1])

        except IndexError:
            pass
        
    return listenames




def classements(score, name, listscore, listnames):

    file = open("highscores.txt", "w")
    if len(listscore) < 10 :

        listscore.append(score)
        listscore.sort(reverse=True)
        
        ind = listscore.index(score)
        listnames.insert(ind, name)


    elif listscore[-1] < score:
        listscore.pop()
        listnames.pop()
        listscore.append(score)
        listscore.sort(reverse=True)
        ind = listscore.index(score)
        listnames.insert(ind, name)

    scoreandnames = {}

    for i in range(len(listscore)):
        listprint = [str(i+1), "           ", str(listnames[i]),"     ", str(listscore[i]),"\n"]
        file.writelines(listprint)
        scoreandnames[listnames[i]] = listscore[i]

    file.close()    


    
    return(scoreandnames)
#\Leopold