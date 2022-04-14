#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 06:51:38 2021

@author: esther
"""

'''
Given a, b, c for a quadratric expression ax2 + bx + c = 0. Write a function getX
that returns the larger of the values of X, i.e. given x1 = -2 and x2 = 5, 
getX should return 5. 
'''
 
def getX(a, b, c):
    d = (b**2) - (4*a*c)
    #print(d)
    
    if d >= 0:
        x1 = (-b + (d) ** 0.5)/(2*a)
        x2 = (-b - (d) ** 0.5)/(2*a)
    
    if x1 > x2:
        return x1
    else:
        return x2

#num = getX(1, 5, 6)
#print(num)
