"""
Write a program that prints the hours of the day from 0:00 to 23:59, each on a separate line.

Hours must be written in the format "{hour}:{minutes}".
"""


for i in range(24):
    for j in range(60):
        print(f"{i}:{j}")
