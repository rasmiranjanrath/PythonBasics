#printing todays date
import time as t
time = t.asctime(t.localtime(t.time()))
print (time)

#print a calander
import calendar
cal=calendar.month(2019,3)
#print cal

print(calendar.calendar(2019))