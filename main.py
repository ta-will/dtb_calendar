import sys
import datetime

#The calendar needs to be static it should have the correct amount of days as well as the current month, year

currentMonth = currentDay = currentYear = currentWkDay = datetime.datetime.now()

currentMonth = currentMonth.strftime("%m")
currentDay = currentDay.strftime("%d")
currentYear = currentYear.strftime("%Y")
currentWkDay = currentWkDay.strftime("%w")

currentDay = int(currentDay)
currentYear = int(currentYear)
currentMonth = int(currentMonth)
currentWkDay = int(currentWkDay)

feb = 0
leapYear = False

#I'm coming back to this with a more specific leap year formula but for now I'm laying down groundwork
if (currentYear % 4 == 0):
    leapYear = True
    feb = 29
else:
    leapYear = False
    feb = 28


monthLengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
totalnumofDays = monthLengths[currentMonth - 1]
currentDaysRem = [totalnumofDays - currentDay]

#print(totalnumofDays - currentDay)
#print(currentWkDay)

remainingCalander = []
weekdayNum = currentWkDay

#I want to fill the rest of the days of the month with the appropriate weekday
for days in range(currentDay , totalnumofDays + 1):
    remainingCalander.append(weekdayNum)
    weekdayNum+= 1

    if(weekdayNum >= 7):
        weekdayNum = 0


print( str(currentWkDay) + " " + str(remainingCalander))
