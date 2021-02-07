# DST2 : exo listes abstraites (avec couples)

Empty = None

def is_null(L) :
    return L == Empty

def get_head(L) :
    return L[0]

def get_tail(L) :
    return L[1]

def set_head(L, x) :
    return (x, get_tail(L))

def set_tail(L, Lprime) :
    return (get_head(L), Lprime)

def string(L) :
    if is_null(L) :
        return "Empty"
    else :
        return "(" + str(get_head(L)) + ", " + string(get_tail(L)) + ")"

# Q1)i)
L = (1, (17, (3, Empty)))

# Q1)ii)
print("get_head(L) donne :", get_head(L))
print("get_head(get_tail(L)) donne :", get_head(get_tail(L)))
print("get_head(get_tail(get_tail(L))) donne :", get_head(get_tail(get_tail(L))))

# Q2)
L2 = (2, Empty)
L4 = (3, L2)
L3 = (4, L4)
L1 = (6, L3)
print(string(L1))

# Q3)
# Les n-uplets Python n'étant pas mutable, il faut reconstruire la liste L1 après avoir changer la tête de L4
L4 = set_head(L4, 42)
L3 = (4, L4)
L1 = (6, L3)
print(string(L1))

