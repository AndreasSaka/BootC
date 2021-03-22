# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:16:29 2021

@author: Andreas
"""

#a = int(input("Provide the first number: "))
#print(a)
#b = int(input("Provide the second number: "))
#print(b)

#a,b = b,a



def swap_nums(a,b):
    a,b = b,a
    return a,b

if __name__ == "__main__":
    a = int(input("Provide the first number: "))
    #print(a)
    b = int(input("Provide the second number: "))
    #print(b)
    a,b = swap_nums(a,b)
    print("The a swaped is: ", a)
    print("The b swaped is: ", b)


    