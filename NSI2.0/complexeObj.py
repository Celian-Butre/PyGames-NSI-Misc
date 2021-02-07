import math

class Complexe:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
        self.algeb_trigoexp()
        
    def giveRe(self):
        return (self.Re)
    
    def giveIm(self):
        return (self.Im)
    
    def __str__(self):
        print("\n")
        print(self.module, "e^i", self.argument)
        print("\n")
        print(self.module, "(cos(", self.argument, ") + i*sin(", self.argument, "))") 
        if self.Im == 1:
            return str(self.Re)+'+i'
        elif self.Im == -1:
            return str(self.Re)+'-i'
        else:
            if self.Im >= 0:
                return str(self.Re)+'+'+str(self.Im)+'i'
            else:
                return str(self.Re)+'-'+str(-self.Im)+'i'
    
    def __mul__(self, c):
        return(Complexe((self.Re * c.Im - self.Im * c.Im), (self.Re * c.Im + self.Im * c.Re)))
    
    def __add__(self, c):
        return(Complexe(self.Re + c.Re,  c.Im + self.Im))
    
    def conjuguer(self):
        return(Complexe(self.Re, -self.Im))
    
    def algeb_trigoexp(self):
        self.module = math.sqrt(self.giveRe()**2 + self.giveIm()**2)
        arccos = math.acos(self.giveRe()/self.module)
        arcsin = math.asin(self.giveIm()/self.module)
        if self.giveRe() >= 0:
            if self.giveIm() >= 0:
                self.argument = abs(arccos)
            else:
                self.argument = -1*abs(arccos)
        else:
            if self.giveIm() >= 0:
                self.argument = -1*abs(arccos) + math.pi
            else:
                self.argument = abs(arccos) + math.pi
    
if __name__ == '__main__':        
    c = Complexe(3,1)
    c1 = Complexe(1,2)
    print(c)
    print(c+c1)
    print(c*c1)
    print(c.conjuguer())