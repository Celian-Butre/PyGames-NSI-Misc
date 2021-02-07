# DST2 : exo tri fusion

L = [99, -2, 17, 3, 42]

# Q2) cf après Q4)
# Pour Q2) : utilisation d'un décorateur Python (un décorateur Python est une fonction qui prend une fonction en paramètre et retourne une fonction)
# Permet ici d'afficher automatiquement les appels récursif de la fonction, avec les arguments respectifs
def trace(func) :
    def wrapper(arg) :
        print('    ' * wrapper.space, end='')
        print('--> {}({})'.format(func.__name__, str(arg)))
        wrapper.space += 1
        if arg == [] :
            print('    ' * wrapper.space, "(cas de base : liste vide [], rien à trier)", sep='')
        if len(arg) == 1 :
            print('    ' * wrapper.space, "(cas de base : liste à un élément, déjà triée)", sep='')
        val = func(arg)
        wrapper.space -= 1
        print('    ' * wrapper.space, end='')
        print('{} <-- {}({})'.format(str(val), func.__name__, str(arg)))
        return val
    wrapper.space = 0
    return wrapper

# Q3)
def scinder(L) :
    return L[:(len(L)+1)//2], L[(len(L)+1)//2:]

print("\nRésultat de scinder({}) :".format(L), scinder(L))

# Q4)
def fusionner(L1, L2) :
    L_fusion = []
    i1 = 0
    i2 = 0
    while (i1 + i2 < len(L1) + len(L2) ) :
        if i1 >= len(L1) :      # cas L1 épuisée
            return L_fusion + L2[i2:]
        elif i2 >= len(L2) :    # cas L2 épuisée
            return L_fusion + L1[i1:]
        else :                  # cas L1 et L2 non épuisées
            if L1[i1] < L2[i2] :
                L_fusion.append(L1[i1])
                i1 = i1 + 1
            else :
                L_fusion.append(L2[i2])
                i2 = i2 + 1
    return L_fusion


@trace  # on utilise le décorateur sur la fonction tri_fusion()
def tri_fusion(L) :
    if len(L) <= 1 :    # une liste vide ou à 1 seul élément est déjà triée (et Célian, utiliser sorted() pour vérifier si une liste à deux éléments est déjà triée, c'est de la triche)
        return L
    else :
        (moitie1, moitie2) = scinder(L)
        return fusionner(tri_fusion(moitie1), tri_fusion(moitie2))

# Q2) et Q4)
print("\nExécution et appels récursifs successifs de tri_fusion({}) :\n".format(L))

print("\nRésultat de tri_fusion({}) :".format(L), tri_fusion([99, -2, 17, 3, 42]), end="\n\n")

print("\nTri de la liste vide [] :\n")
tri_fusion([])

