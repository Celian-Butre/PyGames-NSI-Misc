# DST2 : exo factorielle

# Pour Q3) : utilisation d'un décorateur Python (un décorateur Python est une fonction qui prend une fonction en paramètre et retourne une fonction)
# Permet ici d'afficher automatiquement les appels récursif de la fonction, avec les arguments respectifs
def trace(func) :
    def wrapper(arg) :
        print('    ' * wrapper.space, end='')
        print('--> {}({})'.format(func.__name__, str(arg)))
        wrapper.space += 1
        if arg == 0 :
            print('    ' * wrapper.space, "| cas de base : 0! = 1 |", sep='')
        val = func(arg)
        wrapper.space -= 1
        print('    ' * wrapper.space, end='')
        print('{} <-- {}({})'.format(str(val), func.__name__, str(arg)))
        return val
    wrapper.space = 0
    return wrapper


def facto_ite(n) :
    facto = 1
    for i in range(1, n+1) :
        facto = facto * i
    return facto


@trace  # on utilise le décorateur sur la version récursive de la factorielle
def facto_rec(n) :
    if n == 0 :
        return 1
    else :
        return n * facto_rec(n-1)

print("Les mêmes niveaux d'indentations concernent le même appel de fonction (--> pour l'appel et <-- pour le retour) :\n")
print("Exécution et appels récursifs successifs de facto_rec(3) :\n")
facto_rec(3)

print()
print("Exécution et appels récursifs successifs de facto_rec(10) :\n")
facto_rec(10)
