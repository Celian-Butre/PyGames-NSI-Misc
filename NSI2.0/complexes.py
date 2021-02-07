def conjuguer(z): #fonction conjuguer
    return ((z[0], z[1] * -1)) #return conjugaison
    
def addition(z, z1):
    return ((z[0] + z1[0]), (z[1] + z1[1]))

def multiplication(z0, z1):
    return ((z[0] * z1[1] - z[1] * z1[1]), (z[0] * z1[1] + z[1] * z1[0]))
    
def nombreComplexe(z): #imprime le nombre complexe sous sa forme algébrique
    print (z[0], end = "")
    if z[1] >= 0:
        print(" + ", end = "")
    else:
        print(" - ", end = "")
    print (abs(z[1]), end = "i")
    
x = float(input("partie réelle:         ")) #prendre X
y = float(input("partie imaginaire:     ")) #prendre Y

x1 = float(input("partie réelle:         ")) #prendre X
y1 = float(input("partie imaginaire:     ")) #prendre Y

z = (x, y) #créez couple
z1 = (x1, y1)

print ("le conjugué de ", end = "")
nombreComplexe(z)
print(" est ", end = "")
nombreComplexe(conjuguer(z)) #print réponse

print("")

print ("l'addition de ", end = "")
nombreComplexe(z)
print(" et ", end = "")
nombreComplexe(z1)
print(" est ", end = "")
nombreComplexe(addition(z, z1)) #print réponse

print("")

print ("la multiplication de ", end = "")
nombreComplexe(z)
print(" et ", end = "")
nombreComplexe(z1)
print(" est ", end = "")
nombreComplexe(multiplication(z, z1)) #print réponse

print("")
