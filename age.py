# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:48:22 2021

@author: Andreas
"""
import time
import datetime

todaysDate = datetime.date.today()
current_year = todaysDate.year

def ageCalculator(birth_year, current_year):
    age = current_year - birth_year
    #print(f'Your age is {age}')
    return age

#birth_year = int(input('Enter the year you were born: '))

#current_year = int(input('Enter the current: '))

#ageCalculator(birth_year, current_year)


age = ageCalculator(1987,2020)

print(f'Your age is {age}')