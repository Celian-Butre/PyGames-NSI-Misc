def euclide(couple): #pas le mien désolé 
    (a,b) = couple
    while a%b != 0: 
        a, b = b, a%b 
    return b

def addition(couples):
    (r1, r2) = couples
    (p1, q1) = r1
    (p2, q2) = r2
    
    p3 = p1 * q2
    q3 = q1 * q2
    p4 = p2 * q1
    
    r3 = (p4+p3 , q3)
    return(simplification(r3))

def multiplication(couples):
    (r1, r2) = couples
    (p1, q1) = r1
    (p2, q2) = r2
    
    r3 = (p1*p2, q1 * q2)
    
    return(simplification(r3))

    
def simplification(couple):
    pgcd = euclide(couple)
    return (couple[0] // pgcd, couple[1] // pgcd)

def saisie():
    p1 = int(input("p1:     "))
    q1 = int(input("q1:     "))
    p2 = int(input("p2:     "))
    q2 = int(input("q2:     "))
    
    return(((p1, q1), (p2, q2)))

couples = saisie()
print(addition(couples))
print(multiplication(couples))