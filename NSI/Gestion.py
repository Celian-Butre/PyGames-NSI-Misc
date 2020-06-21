import random, math
num1 = int(input("Numéro 1 entre -128 et 127   "))
num2 = int(input("Numéro 2 entre -128 et 127   "))
num1bin = []
num2bin = []

num1save = num1
num2save = num2

if num1 < 0:
    num1  = num1 * -1
    num1 -= 1
    
if num2 < 0:
    num2  = num2 * -1
    num2 -= 1

while num1 != 0:
    num1bin.append(num1 % 2)
    num1 = num1//2
for i in range (8 - len(num1bin)):
    num1bin.append(0)

while num2 != 0:
    num2bin.append(num2 % 2)
    num2 = num2//2
for i in range (8 - len(num2bin)):
    num2bin.append(0)

if num1save < 0:
    for i in range(8):
        if num1bin[i] == 0:
            num1bin[i] = 1
        else:
            num1bin[i] = 0
if num2save < 0:
    for i in range(8):
        if num2bin[i] == 0:
            num2bin[i] = 1
        else:
            num2bin[i] = 0   
num1bin.append(0)
num2bin.append(0)
num2bin.reverse()
num1bin.reverse()
print(num1bin[1:9])
print(num2bin[1:9])
num2bin.reverse()
num1bin.reverse()
numfinal = []
for i in range(8):
    if num1bin[i] + num2bin[i] == 0:
        numfinal.append(0)
    if num1bin[i] + num2bin[i] == 1:
        numfinal.append(1)
    if num1bin[i] + num2bin[i] == 2:
        numfinal.append(0)
        num1bin[i+1] += 1
    if num1bin[i] + num2bin[i] == 3:
        numfinal.append(1)
        num1bin[i+1] += 1

numfinal.reverse()        
for i in range(8):
    print(numfinal[i], end = "")
print("")