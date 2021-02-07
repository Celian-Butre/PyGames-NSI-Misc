graph = [[2,3],[1,4],[1,4,5],[2,3,5,8],[3,4,8],[8],[8],[4,5,6,7]]

def listeSommet(graph):
    listeDesSommet = []
    for i in range (len(graph)):
        for j in range (len(graph[i])):
            alreadyIn = False
            for l in range (len(listeDesSommet)):
                if listeDesSommet[l] == graph[i][j]:
                    alreadyIn = True
            if alreadyIn == False:
                listeDesSommet.append(graph[i][j])
    
    print('les sommets sont: ', end = '')
    for i in range (len(listeDesSommet)):
        print(listeDesSommet[i], end = '')
    print('')
    
listeSommet(graph)