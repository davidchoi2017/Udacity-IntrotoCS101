
'''
Author: David Choi
Date completed: 12/14/2017
This file was created to solve a homework problem on Udacity's Intro to Computer Science course.
The problem to solve is, given your birthday, calculate your age in days from today, and take into account leap days as well.
I first laid out a plan of the program which is in outline form below:

I. Count number of days from birthdate to end of that year and store in variable [let's call it variable 'begdays']
    A. Find difference between birthday and end of birthyear and store in variable
        1. Count number of days from birthday to end of that bmonth and store in variable
            a. Sum (Month number of days +1) minus birthdate and store in variable
                1. Determine total number of days in the month in question
                2. Add 1 to that number
                3. subtract birthdate from that number.
        2. Count number of days from day after last day of birthmonth to Dec 31 of that year and store in variable
        3. Sum steps 1 and 2
    B.  Add 1 day if birth year is leap year and birth date is on or before leap day
        1. Is birth year a leap year?
            a. if so, is the birthdate in jan or feb?
                i. if so, add 1 day.
II. Count the number of days between year after birth year and the current year and store in variable [let's call it variable 'middledays']
    A. Sum (1 - current year) minus (1 + birthyear) and multiply that sum by 365 and store in variable
    B. Find number of extra leap days that occur and store in variable
        1. Find number of leap years from (1 + birthyear) and (1 - current year) inclusive and store in that variable
    C. Sum steps A and B to get total
III. Count remainder days from Jan 1 of Current year to Current day and store in variable [let's call it variable 'enddays']
    A. Find difference
    B. Add 1 day if current year is leap year and current date is on or after leap day
        1. Is current year a leap year?
            a. if so, is the current date on or after the leap day?
                i. if so, add 1 day.
IV. Return sum of steps I through III.
'''
#Receive user input of birthdate and store birthdate info in variables
bmonth = input('What is your birth month?')
bday = input('What is your birth day?')
byear = input('What is your birth year?')

#Store current date info in variables
import datetime
now = datetime.datetime.now()
cmonth = now.month
cday = now.day
cyear = now.year

#function to determine if a given year is a leap year
def is_leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Function to run to see if you need to add a day to account for a leap day in range from given date to 12/31 of same year
def add_leap_day(p,q):
    if is_leap_year(q) == True:
        if p <= 2:
            return 1
        else:
            return 0
    else:
        return 0

#Function to run to see if you need to add a day to account for a leap day in range from jan 1st of given year to given date within that given year
def add_leap_day2(e,f):
    if is_leap_year(f) == True:
        if e > 2:
            return 1
        else:
            return 0
    else:
        return 0

#Function to determine if leap day is present between two dates in same year:
def add_leap_day3(g,h,i,l):
    if is_leap_year(g) == True:
        if h > 2 or i < 2:
            return 0
        if i == 2:
            if l == 29:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0

#Function to determine number of days in the Month
def days_in_month(m):
    if m == 2:
        return 28
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    else:
        return 30

#Function to determine remaining days in year from a given start date (including the starting day)
def headyear(startm,startd,starty):
    firstm = (1 + days_in_month(startm)) - startd
    restofyear = 0
    for startpoint in range(1+startm,13):
        restofyear += days_in_month(startpoint)
    leapfactor1 = add_leap_day(startm,starty)
    hyeartotal = firstm + restofyear + leapfactor1
    return hyeartotal


#Function to determine number days between two dates in the same year:
def sameyear(startm1,startd1,starty1,endm1,endd1):
    if startm1 == endm1:
        tot = endd1 - startd1 + 1
        return tot
    if endm1-startm1 == 1:
        firstm1 = (1 + days_in_month(startm1)) - startd1
        leapfactor3 = add_leap_day3(starty1,startm1,endm1,endd1)
        tot = firstm1 + endd1 + leapfactor3
        return tot
    else:
        firstm1 = (1 + days_in_month(startm1)) - startd1
        midm = 0
        for sample in range(1+startm1,endm1):
            midm += days_in_month(sample)
        leapfactor3 = add_leap_day3(starty1,startm1,endm1,endd1)
        tot = firstm1 + midm + endd1 + leapfactor3
        return tot

#Function to determine number days from Jan 1st of given year to a given end day within that same year (including the end day)
def tailyear(tailm,taild,taily):
    endpart = taild
    firstpart = 0
    for k in range(1,tailm):
        firstpart += days_in_month(k)
    leapfactor2 = add_leap_day2(tailm,taily)
    tailtotal = endpart + firstpart + leapfactor2
    return tailtotal

#Function to calculate number of days from Jan 1st of a given starting year to January 1st of a given ending year:
def days_in_yrange(begy,endy):
    basetotal = 365*(endy - begy)
    leaptotal = 0
    for t in range(begy,endy):
        if is_leap_year(t) == True:
            leaptotal += 1
    rangetotal = basetotal + leaptotal
    return rangetotal

#number days from bday to 12/31 [variable = begdays]
begdays = headyear(bmonth,bday,byear)

#number of days from Jan 1st of (byear+1) to Dec 31st of the year before current year [variable = middledays]
middledays = days_in_yrange(byear+1,cyear)

#number of days from Jan 1st of current year to current day (including current day) [variable = enddays]
enddays = tailyear(cmonth,cday,cyear)

#Sum the total to find final tally
def days_old(w,z):
    if z - w >= 2:
        grand_total = begdays + middledays + enddays
        return grand_total
    if z - w == 1:
        grand_total = begdays + enddays
        return grand_total
    else:
        grand_total = sameyear(bmonth,bday,byear,cmonth,cday)
        return grand_total

print(days_old(byear,cyear))
