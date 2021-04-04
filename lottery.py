# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:01:32 2021

@author: Andreas
"""

#numbers = '5,16,25,3,4,1'

# #numbers.split(",")

# user_input = "1,2,3,4,5,6,7"

# user_numbers = user_input.split(",")

# #convert all the strings to numbers

# use_num_int = []

# for number in user_numbers:
#     use_num_int.append(int(number))
    
# use_num_int

# kaka = [number for number in user_numbers]

# [number*2 for number in user_numbers]

# [int(number) for number in user_numbers]


########
##sets##
##sets##
########
import random

def get_nms():
    nms = input('Enter your numbers, seperated by commas: ')
    #set of intergers
    nums_list = nms.split(",")
    nums_new = {int(number) for number in nums_list}
    return nums_new

def creat_lottery_numbers():
    values = set()
    while len(values) < 6:
        for index in range(6):
            values.add(random.randint(1,20))
    return values
  
def menu():
    #ask player for numbers
    nums = set()
    nums = get_nms()
    #calculate lottery numbers
    lottery_nums = creat_lottery_numbers()
    #print out the winnings
    matched = lottery_nums.intersection(nums)
    print("You matched the numbers {} and you won ${}!".format(matched,100**len(matched)))
    
      
#print(get_nms())
#print(creat_lottery_numbers())
menu()