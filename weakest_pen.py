#Need to import time module for managing dates
import time
from datetime import datetime

#birthday_book is a file containing birthdays stored as a dictionary for anyone you want a reminder for
from birthday_book import *

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m.%Y')

#Empty string for storing today's birthdays
todays_birthdays = ''

#For loop checkings dates against today's date and appending the related name to a string
#Need to edit to check only the DD.MM not the YY
for day, name in birthdays.items():
    if day == today:
        if todays_birthdays == '':
            todays_birthdays = name
        else:
            todays_birthdays = todays_birthdays + ", " + name

#Checks to make sure at least one person has a birthday today
if todays_birthdays == '':
    print('No birthdays today')
else:
    print(todays_birthdays)