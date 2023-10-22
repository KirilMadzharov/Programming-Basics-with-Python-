"""
Three sports competitors finish in some number of seconds (between 1 and 50).
Write a program that reads the times of the competitors in seconds entered by the user
and calculates their total time in "minutes:seconds" format.
Display seconds with a leading zero (2  "02", 7  "07", 35  "35").
"""

first = int(input())
second = int(input())
third = int(input())

time = first + second + third

minutes = time // 60
seconds = time % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
