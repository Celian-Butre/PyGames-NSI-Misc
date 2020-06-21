#!/usr/bin/env python
# coding: utf-8

# In[1]:

import random

nmbreleves = int(input("Combien d'élèves?    "))
notesur = int(input("Sur combien est-ce noté?  "))

notes = []
quantnotes = []

def printlabels():
  print("")

# In[2]:

def finddigits(nombre):
    digit = 1
    while nombre > 9:
        digit += 1
        nombre = nombre// 10
    return (digit)

# In[3]:

def printlegendes(totaldigit, notelegende):
    for i in range(totaldigit):
        for j in range (notesur+1):
            if notelegende[j][i] == 'x':
                print (" ", end = " ")
            else:
                print(notelegende[j][i], end = " ")
        print ("")

# In[4]:

def legendes():
    notelegende = []
    totaldigit = finddigits(notesur)
    for i in range (notesur+1):
        notelegende.append([])
        for j in range (totaldigit):
            notelegende[i].append('x')
        idigit = finddigits(i)
        modifiedi = i
        for j in range (idigit):
            thingToUse = modifiedi // 10**(idigit-1-j)
            notelegende[i][j] = thingToUse
            modifiedi -= thingToUse * 10**(idigit-1-j)
    printlegendes(totaldigit, notelegende)

# In[5]:

def gennotes():
  for i in range(nmbreleves):
    notes.append(random.randint(0, notesur))

def digitalizenotes():
  for i in range (notesur + 1):
    notetosearch = i
    currentamount = 0
    for j in range (nmbreleves):
      if notes[j] == notetosearch:
        currentamount += 1
    quantnotes.append(currentamount)

# In[6]:

def findmaxnotes():
  maxquant = 0
  for i in range (notesur + 1):
    if maxquant < quantnotes[i]:
      maxquant = quantnotes[i]
  return (maxquant)

def printnotes():
  for i in range (maxquant):  
    printtier = maxquant - i
    for j in range (notesur + 1):
      if quantnotes[j] == printtier:
        print("#", end = " ")
        quantnotes[j] -= 1
      else:
        print(" ", end = " ")
    print("")

# In[7]:

gennotes()
digitalizenotes()

# In[8]:

maxquant = findmaxnotes()
printnotes()
printlabels()
legendes()