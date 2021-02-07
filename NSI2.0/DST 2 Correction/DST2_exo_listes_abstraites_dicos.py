# DST2 : exo listes abstraites (avec dicos)

Empty = None

def is_null(L) :
    return L == Empty

def get_head(L) :
    return L['head']

def get_tail(L) :
    return L['tail']

def set_head(L, x) :
    L['head'] = x

def set_tail(L, Lprime) :
    L['tail'] = Lprime

def string(L) :
    if is_null(L) :
        return "Empty"
    else :
        return "(" + str(get_head(L)) + ", " + string(get_tail(L)) + ")"

# Q1)i)
L = {'head' : 1, 'tail' : { 'head' : 17, 'tail' : { 'head' : 3, 'tail' : Empty} } }

# Q1)ii)
print("get_head(L) donne :", get_head(L))
print("get_head(get_tail(L)) donne :", get_head(get_tail(L)))
print("get_head(get_tail(get_tail(L))) donne :", get_head(get_tail(get_tail(L))))

# Q2)
L2 = { 'head' : 2, 'tail' : Empty }
L4 = { 'head' : 3, 'tail' : L2 }
L3 = { 'head' : 4, 'tail' : L4 }
L1 = { 'head' : 6, 'tail' : L3 }
print(string(L1))

# Q3)
set_head(L4, 42)
print(string(L1))

