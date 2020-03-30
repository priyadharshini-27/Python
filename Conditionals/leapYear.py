def leapYear(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return "Leap Year"
    else:
        return "Not Leap Year"
n=int(input())
print(leapYear(n))