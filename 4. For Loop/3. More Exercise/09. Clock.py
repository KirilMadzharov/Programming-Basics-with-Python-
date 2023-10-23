"""
Write a program that prints the hours of the day from 0:00 to 23:59, each on a separate line.

Hours must be written in the format "{hour} : {minutes}".
"""


hour = 23
minutes = 59

for i in range(hour + 1):
    for m in range(minutes + 1):
        print(f"{i} : {m}")

