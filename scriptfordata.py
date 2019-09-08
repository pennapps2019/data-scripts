import random


# Arbitrary values given to latitude, longitude and the current hour
latitude = 30
longitude = 30
hour = 8


# Array to keep track of the days of the week
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = 0


# Pick a random number between 1 and 100, and set a range for the random number
number = random.uniform(1.0,100.0)
low = 0.0
high = 100.0

if (number < 20):
    low = number-1
    high = number+1
else:
    low = number-(number/10)
    high = number+(number/10)


# Print a semi-randomly generated data for our application
for i in range(50):
    hour = 8
    
    for j in range(6):
        if (hour == 8 or hour == 9):
            print('2019-09-08 0%d:00:00,%.4f,%.4f,%.4f,%s' % (hour,random.uniform(low,high),latitude,longitude,days[day]))
        else:
            print('2019-09-08 %d:00:00,%.4f,%.4f,%.4f,%s' % (hour,random.uniform(low,high),latitude,longitude,days[day]))
        hour += 1
    
    if (day == 7):
        day = 0
    else:
        day += 1
        
