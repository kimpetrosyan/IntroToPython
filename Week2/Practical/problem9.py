import calendar
import datetime
import time

localtime = time.asctime()
print ("Local current time :", localtime)

tday = datetime.datetime.today()

print('Date: ', tday)
print('Year: ', tday.year)
print('Month: ', tday.month)

print('Day of the week (version 1): ', tday.isoweekday())
print('Day of the week (version 0): ', tday.weekday())

tdelta = datetime.timedelta(days = 5)
print('- 5 days: ', tday - tdelta)
print()

print('Date and Time: ', tday)

tdelta1 = datetime.timedelta(seconds = 5)

print('+ 5 sec: ', tday + tdelta1)