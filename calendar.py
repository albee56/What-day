year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))

# lst is the list contains all years
lst = list()
x = 1900
while x < year:
    lst.append(x)
    x = x + 1

# count is the total days before the enter year
count = 0
for ye in lst:
    if ye % 400 == 0 or (ye % 4 == 0 and ye % 100 != 0):
        z = 366
    else:
        z = 365
    count = count + z

# check if 'year' is leap year
leapyear = False
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    leapyear = True
    print('Leap Year')
elif year % 4 == 0 and year % 100 != 0:
    leapyear = True
    print('Leap Year')
else:
    leapyear = False
    print('Not Leap Year')

# count total days in the last year
if leapyear == True:
    monthday = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = sum(monthday[:month-1]) + day
elif leapyear == False:
    monthday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    a = sum(monthday[:month-1]) + day

# total days
count = count + a

if count % 7 != 0:
    print(count % 7)
else:
    print(7)
