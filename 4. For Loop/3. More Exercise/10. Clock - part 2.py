"""
Write a program to print the hours of the day from 0:0:0 to 23:59:59,
each on a separate line.

Times should be written in the format "{hour} : {minutes} : {seconds} ".
"""


hour = 23
minutes = 59
seconds = 59

for i in range(hour + 1):
    for m in range(minutes + 1):
        for s in range(seconds + 1):
            print(f"{i} : {m} : {s}")
