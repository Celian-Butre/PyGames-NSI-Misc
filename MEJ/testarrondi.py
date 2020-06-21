totalthrows = 0
increment = 4
assiettes = 3
floor = 0
for i in range (1,102):
    minimum = 0
    maximum = 100
    puissance = assiettes
    while minimum != maximum-1:
        puissance -= 1
        while minimum != maximum-1 and floor < i and floor < 100:
            if floor + (increment ** puissance) > 100:
                floor = 100
            else:
                floor += (increment ** puissance)
            if floor >= i:
                maximum = floor
            if floor < i:
                minimum = 0
            totalthrows += 1
print (totalthrows)