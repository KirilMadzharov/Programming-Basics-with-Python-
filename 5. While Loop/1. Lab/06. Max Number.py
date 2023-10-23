"""
Write a program that, until the
"Stop" command is received, reads integers
entered by the user, finds the largest among them,
and prints it. Enter one number per line.
"""


import sys

number = input()
max_num = - sys.maxsize

while number != "Stop":
    num = int(number)

    if num > max_num:
        max_num = num

    number = input()

print(max_num)

