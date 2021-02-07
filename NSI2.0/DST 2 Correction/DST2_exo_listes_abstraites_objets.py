# DST2 : exo listes abstraites (avec objets)

class Liste :

    def __init__(self, h, t) :
        self.__head = h
        self.__tail = t

    def is_null(self) :
        return self == Empty

    def get_head(self) :
        return self.__head

    def get_tail(self) :
        return self.__tail

    def set_head(self, h) :
        self.__head = h

    def set_tail(self, t) :
        self.__tail = t

    # Pour la protection des attributs
    # décorateur @property : accesseur d'attribut
    # décorateur @property : mutateur d'attribut
    @property
    def head(self) :
        return self.__head

    @property
    def tail(self) :
        return self.__tail

    @head.setter
    def head(self, h) :
        self.__head = h

    @tail.setter
    def tail(self, t) :
        self.__tail = t

    def __str__(self) :
        if self.is_null() :
            return "Empty"
        else :
            return "("+str(self.head)+", "+ str(self.tail)+")"

Empty = Liste(None, None)

# Q1)i)
L = Liste(1, Liste(17, Liste(3, Empty)))
print("L =", L)

# Q1)ii)
print()
print("L.get_head() donne :", L.get_head())
print("L.get_tail().get_head() donne :", L.get_tail().get_head())
print("L.get_tail().get_tail().get_head() donne :", L.get_tail().get_tail().get_head())

# Q2)
print()
L2 = Liste(2, Empty)
L4 = Liste(3, L2)
L3 = Liste(4, L4)
L1 = Liste(6, L3)
print("L1 =", L1)

# Q3)
print()
# Avec les listes intermédiaires :
print("Exécution de L1.get_tail().get_tail().set_head(42)")
L1.get_tail().get_tail().set_head(42)
print("L1 =", L1)

# Directement sur L4 :
print()
print("Exécution de L4.head = 17000 (méthode avec le décorateur Python @head.setter)")
L4.head = 17000
print("L1 =", L1)

