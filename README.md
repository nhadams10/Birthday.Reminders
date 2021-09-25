# Birthday.Reminders
*Basic script to remind me of important birthdays. Calendar and FB do similar things, but want to customize how far in advance I am notified.*

Currently, the program can print a list of today's birthdays but not yet warn at a set range in advance. To get to that functionality, the follow features should be implemented:

- A means of setting how far in advance / when the birthday warning should be sent
- A means of checking if there are any upcoming birthdays
- A means of customizing the output to read cleanly for upcoming birthdays as well as todays birthdays

Afterwards, the last feature to implement will be an SMS notification with the following requirements:
- Daily, at 5am UTC, run the program
- If there are no birthdays/birthday notifications today, do nothing
- If there are birthdays/birthday notifications, send SMS message to the user
