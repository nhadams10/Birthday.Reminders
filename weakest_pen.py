#Need to import time module for managing dates
import time
from datetime import datetime

#birthday_book is a file containing birthdays stored as a dictionary for anyone you want a reminder for
from birthday_book import *

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m.%Y')

#Empty string for storing today's birthdays
todays_birthdays = ''

#For loop checkings dates against today's date
for day, name in birthdays.items():
    if todays_birthdays == "":
        if day == today:
            todays_birthdays += name
    else:
        if day == today:
            todays_birthdays += ", " + name

print(todays_birthdays)