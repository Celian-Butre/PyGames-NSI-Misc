# DST2 : exo listes tridimensionnelles

L = [ [ [23, 34], [1, 2, 34] ] , [ [-45, 67], [100], [987, -78] ] ]

print(L[1])

# Q1)
print("L[1][2][1] donne :", L[1][2][1])
print("L[-1][-1][-1] donne :", L[-1][-1][-1])
print()

# Q2)
def elements_liste_3D(L) :
    for i in range(len(L)) :
        for j in range(len(L[i])) :
            for k in range(len(L[i][j])) :
                print(L[i][j][k], end="")
                if k != len(L[i][j]) - 1 :
                    print(end=" ; ")
            print()
        print()

elements_liste_3D(L)

# Q3)
def extrema_liste_3D(L) :
    minimum = L[0][0][0]
    maximum = L[0][0][0]
    for i in range(len(L)) :
        for j in range(len(L[i])) :
            for k in range(len(L[i][j])) :
                if L[i][j][k] < minimum :
                    minimum = L[i][j][k]
                if L[i][j][k] > maximum :
                    maximum = L[i][j][k]
    return minimum, maximum

print(extrema_liste_3D(L))
