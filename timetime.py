import time

result = time.gmtime(1545925769)
print(result)

from datetime import date

today = date.today()
print(today)

from time import strftime, gmtime
print('Current date and time: ',strftime("%a,%d-%b-%Y %H:%M:%S +0000", gmtime()))
print('alternate date and time: ',strftime("%a,%d-%b-%Y-%H-%M", gmtime()))
print('Current year: ',strftime("%Y", gmtime()))
print('Month of year: ',strftime("%m", gmtime()))
print('Week number of the year: ',strftime("%d", gmtime()))
print('Day of year: ',strftime("%j", gmtime()))
print('Day of the month: ',strftime("%d", gmtime()))
print('Day of week: ',strftime("%A", gmtime()))
