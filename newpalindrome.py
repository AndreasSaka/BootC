# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:41:08 2021

@author: Andreas
"""

echtor = 'KIKA'
echtor = echtor.lower()

a,b = 3,4

a, *b = 3,4,5,6

def foo(*args):
    for a in args:
        print(a)
        
        
def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result


def myfunc(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}=={value}')
        
        
a,b,c,d=spam=foo, *boo=[10,20,'ham','eggs']    


def palindrome(name):
    list3 = []
    for char in name:
        lista.append(char)
    list3 = lista.copy()
    list3.reverse()
    if(lista == list3):
        return True
    else:
        return False
    
name = input('Provide a string: ')
lista = []
result = palindrome(name)
print(result)