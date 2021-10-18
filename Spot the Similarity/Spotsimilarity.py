# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:32:17 2021

@author: Admin
"""

import string
import random

Symbols = []
Symbols = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
#print(pos1)
#print(pos2)

# pos1 and pos2 are same symbols position in card1 and card2 respectively

sameSymbols = random.choice(Symbols)
Symbols.remove(sameSymbols)
if (pos1 == pos2):
    card2[pos1] = sameSymbols
    card1[pos1] = sameSymbols
    
else:
    card1[pos1] = sameSymbols
    card2[pos2] = sameSymbols
    card1[pos2] = random.choice(Symbols)
    Symbols.remove(card1[pos2])
    card2[pos1] = random.choice(Symbols)
    Symbols.remove(card2[pos1])
    
i = 0

while (i<5):
    if (i!=pos1 and i!=pos2):
        alphabet1 = random.choice(Symbols)
        Symbols.remove(alphabet1)
        alphabet2 = random.choice(Symbols)
        Symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i = i+1
print(card1)
print(card2)

ch = input("Spot the similarity symbol : ")
if (ch == sameSymbols):
    print("Right")
else:
    print("wrong")