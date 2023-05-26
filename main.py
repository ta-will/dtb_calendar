import sys
import math
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

#using this to
currentDayCopy = currentDay

feb = 0
leapYear = False

#--------------------------------------------------------------------------------------------------------#
#I'm coming back to this with a more specific leap year formula but for now I'm laying down groundwork
if (currentYear % 4 == 0):
    leapYear = True
    feb = 29
else:
    leapYear = False
    feb = 28

#---------------------------------------------------------------------------------------------------------#

monthLengths = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
totalnumofDays = monthLengths[currentMonth - 1]
currentDaysRem = [totalnumofDays - currentDay]

#print(totalnumofDays - currentDay)
#print(currentWkDay)

remainingDaysArr = []
weekdayNum = currentWkDay

#I want to fill the rest of the days of the month with the appropriate weekday
for days in range(currentDay , totalnumofDays + 1):
    remainingDaysArr.append(weekdayNum)
    weekdayNum+= 1

    if(weekdayNum >= 7):
        weekdayNum = 0

print(currentDay)
#print( str(currentWkDay) + " " + str(remainingDaysArr))

calendar = [["x" for x in range(7)] for y in range(6)]

#I want to fill the calendar starting with the first day of the month and then filling in the
#rest of the days, if the month starts with wednesday the first x-axis value should
#be in the middle of the array

#finding where to starting the list(array)
startingDay = datetime.datetime(currentYear, currentMonth, 1)
startingDay =startingDay.strftime("%w")
startingDay = int(startingDay)
startingDayCopy = startingDay

row = 0
count = 0
for x in range(totalnumofDays):
    calendar[row][startingDayCopy] = (count + 1)
    startingDayCopy+= 1
    count+= 1
    
    if(startingDayCopy >= 7):
        startingDayCopy = 0
        row+= 1


for x in range(6):
    print(calendar[x])