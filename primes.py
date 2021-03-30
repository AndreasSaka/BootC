# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:55:35 2021

@author: Andreas
"""
import random

def picknroll():
    x = random.randint(2,100)
    return x

def isprime(x):
    if x > 1:
        for i in range(2,x):
            if x%i == 0 and x%1==0:
                print(f'{x} is a prime')
            else:
                print(f'{x} is not  a prime')

new = picknroll()
isprime(new)