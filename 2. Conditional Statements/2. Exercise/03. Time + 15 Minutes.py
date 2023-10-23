"""
Write a program that reads the hour and minutes of a 24-hour day entered by
 the user and calculates what the time will be in 15 minutes.

 Print the result in hours:minutes format.

 Hours are always between 0 and 23 and minutes are always between 0 and 59.
 Hours are written as one or two digits.
 Minutes are always written as two digits, with a leading zero when necessary.
"""

hours = int(input())
minutes = int(input())
minutes += 15

hours += minutes // 60
minutes %= 60

if hours == 24:
    hours = 0

print(f"{hours}:{minutes:02d}")
