
from datetime import datetime
from time import time


now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time_var = now.strftime("%H:%M:%S")
print("time:", time_var)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)
# HH:MM:SS.mmmmmm+zz:zz
t_time = now.strftime("%H:%M:%S:")	
print(f'time is {t_time}')
'''
To get a date string with millisecondsz, 
use [:-3] to trim the last three digits of %f (microseconds):
>>> from datetime import datetime 
>>> datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
'2022-09-24 10:18:32.926'

'''
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
date_time_2 = now.strftime("%m/%d%Y-%H:%M:%S")
print(date_time_2)

#dt: datetime = datetime.fromisoforma
print(type(time()))
print(str(time()))
