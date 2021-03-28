# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 10:53:13 2021

@author: Andreas
"""

p = 10000

r = 3.5

t = 7

#FV = P(1 + rt)
#amt*((1+(0.01*int)) ** years)
#FV =  p * (1+ r*t)

def formula(p,r,t):
    #print('Calculating the future value: ')
    fv = p*((1+(0.01*r)) ** t)
    #print(f'The future value for {p} is {fv}: ')
    return fv
    
fv = formula(p,r,t) 
print('The future value is', round(fv,2))