"""
Write a program that, until receiving the "Stop"
 command, reads integers entered by the user,
 finds the smallest among them, and prints it.

Enter one number per line.
"""


import sys

number = input()
min_num = sys.maxsize

while number != "Stop":
    num = int(number)

    if num < min_num:
        min_num = num

    number = input()

print(min_num)

