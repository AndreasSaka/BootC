# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 20:45:07 2021

@author: Andreas
"""

winsA = 0
winsB = 0

play_again = ''

while play_again != 'end':
    choiceA = input('Player A please select rock/scissor/paper type end to finish: ')
    choiceB = input('Player B please select rock/scissor/paper or type end to finish: ')
    if choiceA == choiceB:
        winsA += 0
        winsB += 0
    elif choiceA == 'rock':
        if choiceB == 'scissor':
            winsA += 1
            winsB += 0
        elif choiceB == 'paper':
            winsA += 0
            winsB += 1
    elif choiceA == 'scissor': 
        if choiceB == 'rock':
            winsA += 0
            winsB += 1
        elif choiceB == 'paper':
            winsA += 1
            winsB += 0
    elif choiceA == 'paper': 
        if choiceB == 'rock':
            winsA += 1
            winsB += 0
        elif choiceB == 'scissor':
            winsA += 0
            winsB += 1
    play_again = input("Play again? type end to stop: ")
print('Player A wins: ',winsA)
print('Player B wins: ',winsB)
            
        