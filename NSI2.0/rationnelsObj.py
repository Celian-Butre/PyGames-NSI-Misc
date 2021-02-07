class Rationnel:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        
    def print(self):
        print (self.p, '/', self.q, end = '', sep = '')
        
    def giveP(self):
        return (self.p)
    
    def giveQ(self):
        return (self.q)
    
    def __str__(self):
        return str(self.p)+'/'+str(self.q)
    
    def multRat(self, r):
        return(Rationnel(self.p * r.p, self.q * r.q))
    
    def __mul__(self, r):
        return(Rationnel(self.p * r.p, self.q * r.q))
    
    def __add__(self, r):
        return(Rationnel(self.p * r.q + r.p * self.q, r.q * self.q)) 
    
    def simpl(self):
        return(Rationnel(self.p // Euc(self), self.q // Euc(self)))
        
def Euc(r):
    a,b = r.giveP(), r.giveQ()
    while a%b != 0: 
        a, b = b, a%b 
    return b

if __name__ == '__main__':        
    r = Rationnel(3,5)
    r1 = Rationnel(1,2)
    print(r)

    print(r*r1)

    print(r+r1)

    print(r.simpl())