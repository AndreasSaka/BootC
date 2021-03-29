# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 18:08:14 2021

@author: Andreas
"""

#word = 'madam'
def pal(word):
    summ = ''
    for i in range(len(word)):
        summ += word[len(word)-1-i]
    return summ
    #print(i)
    
word = input('Provide string as input: ')
x = pal(word)
if x == word:
    print('This word is a palindrome')
else:
    print('This word is not a palindrome!')