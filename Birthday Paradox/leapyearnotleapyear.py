# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:59:11 2021

@author: Admin
"""

year =int(input("Enter the year : "))

if (year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Not a Leap year")