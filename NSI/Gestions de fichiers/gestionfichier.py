f = open("fichier.txt","r", encoding="utf8")
j = f.read()
print(j)
r = j.split()
l = []
f = open("fichier.txt","r", encoding="utf8")
i = 0
for line in f:
    i += 1
    f = open("fichier.txt","r", encoding="utf8")
    l.append(f.readline(i))
print(l)