#Need to import time module for managing dates
import time
from datetime import datetime

#birthday_book is a file containing birthdays stored as a dictionary for anyone you want a reminder for
from birthday_book import *

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m')
year = time.strftime('%Y') 

#Empty list for storing today's birthdays
todays_birthdays = []

#For loop checkings birthdays against today's date and appending the [birthday, name] to todays_birthdays
for birthday, name in birthdays:
    if today in birthday:
        todays_birthdays.append([birthday, name])

#WRITE a for loop calculating age
#for birthday, name in todays_birthdays


#WRITE something to format output


#Old code for formatting output ", "
        # if todays_birthdays == '':
        #     todays_birthdays = name
        # else:
        #     todays_birthdays = todays_birthdays + ", " + name

#Checks to make sure at least one person has a birthday today
if todays_birthdays == []:
    print('No birthdays today')
else:
    print(todays_birthdays)