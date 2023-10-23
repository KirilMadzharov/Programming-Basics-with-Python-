"""
Write a program that reads n number of integers.

Print the largest and smallest number among those entered.
"""


import sys

iterations = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize
number = 0

for nums in range(iterations):
    number = int(input())

    if number > max_num:
        max_num = number

    if number < min_num:
        min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
