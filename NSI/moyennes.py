notes = {"nsi1" : 19, "nsi2" : 18, "math1" : 14, "math2": 15}
moyenne = 0
nbnotes = 0
for note in notes.values():
    moyenne += note
    nbnotes += 1
moyenne = moyenne / nbnotes
print (moyenne)