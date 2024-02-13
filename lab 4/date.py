"""
#1
Write a Python program to subtract five days from current date.
"""
import datetime
def Date():
    current = datetime.datetime.now()
    five_ago=current - datetime.timedelta(days=5)
    print(five_ago.strftime("%A"))
Date()

"""
#2
Write a Python program to print yesterday, today, tomorrow.
"""

import datetime
def Dates():
    current= datetime.datetime.now()
    yesterday = current - datetime.timedelta(days=1)
    tomorrow = current + datetime.timedelta(days=1)
    print(yesterday.strftime("%A"))
    print(current.strftime("%A"))
    print(tomorrow.strftime("%A"))
Dates()

"""
#3
Write a Python program to drop microseconds from datetime.
"""
import datetime
def micro(x):
    return x.replace(microsecond=0)

current = datetime.datetime.now()
current_without= micro(current)
print(current_without)

"""
#4
Write a Python program to calculate two date difference in seconds.
"""

import datetime
def difference():
    current = datetime.datetime(2038, 3, 2, 10, 38, 14)
    the_last_of_us = datetime.datetime(2013, 9, 27, 1, 47, 55)
    differences = current - the_last_of_us
    total_seconds = differences.total_seconds()
    print(total_seconds)
difference()