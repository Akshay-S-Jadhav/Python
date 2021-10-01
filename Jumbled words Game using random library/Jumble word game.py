# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:28:01 2021

@author: Admin
"""
import random

def choose():
    words = ['akshay', 'ved', 'siddhu', 'omkar', 'rainbow', 'jay', 'book', 'back', 'sanskrit', 'crocodile',
             'goat', 'assignment', 'right', 'write']
    pick = random.choice(words)
    return pick

def jumble(words):
    jumbled = " ".join(random.sample(words,len(words)))
    return jumbled

def thank(p1n,p2n,p1s,p2s):
    print("_________________________________________")
    print(p1n, "Your Score is :", p1s)
    print(p2n, "Your Score is :", p2s)
    print("_________________________________________")
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    if p1s==p2s:
        print(" The game is Draw")
    elif p1s>p2s:
        print(p1n," is the winner")
    else:
        print(p2n," is the winner")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("                                          \n")
    print("Thanks for playing")
    print("-------------------^_^----------------------")
    
def play():
    p1n = input("Player 1 , Please Enter your name : ")
    p2n = input("Player 2 , Please Enter your name : ")
    p1s = 0
    p2s = 0
    turn = 0
    
    while(1):
        # Computer's task
        picked_word = choose() 
        #Create Quesion 
        qn = jumble(picked_word)
        print(qn)
        
        # player 1 turn
        
        if turn%2==0:
            print(p1n, "Your turn")
            ans = input("What is answer : ")
            if ans == picked_word:
                p1s=p1s+1
                print("Your score is: ",p1s)
            else:
                print("Better luck next time, I Thought: ",picked_word)
            c = input("Press y to Continue and n to Quit:")
            if c=='n':
                thank(p1n,p2n,p1s,p2s)
                break
        
        #player 2
        else:
            print(p2n,"Your Turn")
            ans = input("What is answer : ")
            if ans == picked_word:
                p2s=p2s+1
                print("Your score is:",p2s)
            else:
                print("Better Luck nest time, I thought : ",picked_word)
            c = input("Press y to Continue and n to Quit:")
            if c=='n':
                thank(p1n,p2n,p1s,p2s)
                break
        turn = turn + 1

play()