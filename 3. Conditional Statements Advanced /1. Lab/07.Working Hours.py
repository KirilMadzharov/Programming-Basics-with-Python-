"""
Write a program that reads the hour of the day (integer) and the day of the week (text)
- entered by the user and checks whether the office of a company is open, with the working hours
of the office being from 10 a.m. to 6 p.m., from Monday to Saturday inclusive
"""

hours = int(input())
day = input()

if 10 > hours or hours > 18 or day == "Sunday":
    print("closed")
else:
    print("open")
