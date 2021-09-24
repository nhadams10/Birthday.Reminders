#Need to import time module for managing dates
import time
from datetime import datetime


#birthday_book is a file containing birthdays for anyone you want a reminder for
from birthday_book import *

#Eventually need to revise to account for time zones
today = time.strftime('%d.%m.%Y')
print(today)

#A date for testing purposes
test_date = '22.08.2021'
print(test_date)

#Empty string for storing today's birthdays
todays_birthdays = 'Test'



def birthday_checker(list):
for line in birthday_strings_list:
    print(line)
        #if today in line:
            #name = line.split('  ')[1]
            #todays_birthdays += name
    #if todays_birthdays == "":
        #todays_birthdays = "No Birthdays Today"

print(birthday_strings_list)

birthdays.close()
