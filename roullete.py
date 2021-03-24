import random

def IsDivisibleBy(x):
    return x%2 == 0
    

def iseven(x):
    '''
    The function checks whether the
    given number is an odd or an even
    number.
    '''
    arithmos = ''
    if IsDivisibleBy(x) == True:
        arithmos = 'EVEN'
        #print(f'{x} is an even number')
    else:
        arithmos = 'ODD'
        #print(f'{x} is an odd number')
        

def isred(x):
    '''
    The function checks whether the
    given number is Red or BLACK
    number.
    '''
    color = ''
    if (x<=10 or 19<=x<=28 and IsDivisibleBy(x) == True):
        #print(f'{x} is Red')
        color = 'RED'
    else:
        #print(f'{x} is Black')
        color = 'BLACK'
    return color



for i in range(1,4):
    x =random.randint(0,36)
    if x > 18:
        print(f'The {x} is a big number')
        arnum = iseven(x)
        print(f'{x} is an {arnum}')
        cola = isred(x)
        print(f'The {x} is {cola}')
    else:
        print(f'The {x} is a small number')
        arnum = iseven(x)
        print(f'{x} is an {arnum}')
        cola = isred(x)
        print(f'The {x} is {cola}')



