def euclide(dico): #pas le mien désolé 
    a = dico["p"]
    b = dico["q"]
    while a%b != 0: 
        a, b = b, a%b 
    return (b)

def addition(dico):
    r1 = dico["r1"]
    r2 = dico["r2"]
    p1 = r1["p"]
    q1 = r1["q"]
    p2 = r2["p"]
    q2 = r2["q"]
    
    p3 = p1 * q2
    q3 = q1 * q2
    p4 = p2 * q1
    
    r3 = {"p" : p3+p4, "q" : q3}
    return(simplification(r3))

def multiplication(dico):
    r1 = dico["r1"]
    r2 = dico["r2"]
    p1 = r1["p"]
    q1 = r1["q"]
    p2 = r2["p"]
    q2 = r2["q"]
    
    r3 = {"p" : p1*p2, "q" : q1 * q2}
    
    return(simplification(r3))

def division(dico):
    r2 = dico["r2"]
    p2 = r2["p"]
    q2 = r2["q"]
    if p2 == 0:
        return("not allowed to divide by 0")
    p2,q2 = q2, p2
    
    dico["r2"] = {"p" : p2, "q" : q2}
    return(multiplication(dico))
    
def simplification(dico):
    pgcd = euclide(dico)
    dico = {"p" : dico["p"] // pgcd, "q" : dico["q"] // pgcd} 
    return (dico)

def saisie():
    p1 = int(input("p1:     "))
    q1 = int(input("q1:     "))
    p2 = int(input("p2:     "))
    q2 = int(input("q2:     "))
    r1 = {"p" : p1, "q" : q1}
    r2 = {"p" : p2, "q" : q2}
    dico = {"r1" : r1, "r2" : r2}
    
    return(dico)

def affichage(dico):
    if dico == ("not allowed to divide by 0"):
        print("not allowed to divide by 0")
        return(0)
    p = dico["p"]
    q = dico["q"]
    print(p, end = '')
    print("/", end = '')
    print(q)

dico = saisie()
print("addition         :    ", end ='')
affichage(addition(dico))
print("multiplication   :    ", end = '')
affichage(multiplication(dico))
print("division         :    ", end = '')
affichage(division(dico))