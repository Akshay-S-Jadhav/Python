# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:53:17 2021

@author: Akshay Sandip Jadhav
"""

"""
   This is Game is played between two person, where they first decide 
   the ending point of the game, And count alternatly.
   
   Here the multiple of 3 should be called as Fizz, multiple of 5 should be called as Buzz 
   and Multiple of both 3 and 5 should be called as FizzBuzz, Whoever will fail to give Fizzbuzz 
   sequence will loose the game

   For Ex: Player 1 start the game with 1 
           Player 2 will say 2, then here comes the game where player 1 will have to say Fizz since it is multiple of 3,
           likewise for 5 it will be Buzz, 6 will be Fizz, 9,12 will be Fizz , And 15 will have Fizzbuzz and so on...

    This is all about FizzBuzz Game

    Note : This is only the demo and  illustration of the Game and not as the actual game since there is no interactivity in this code.
   
"""


def main():
    print("__________________________________________________________________")
    print("====================Welcome to Fizzbuzz game======================")
    print("__________________________________________________________________")
    r = int(input("Choose Your Range till where you want to see the Fizzbuzz game : "))
    print("This is just the demo of game that how it work the actual interactive code ")
    fizzbuzz(r)
    



def fizzbuzz(r):
    for i in range(1,r):
        if (i%3==0 and i%5==0):
            print(str(i)+"= FizzBuzz")
        else:
            if(i%3==0):
                print(str(i)+"=Fizz")
            else:
                if(i%5==0):
                    print(str(i)+"=Buzz")
                else:
                    print(str(i))

