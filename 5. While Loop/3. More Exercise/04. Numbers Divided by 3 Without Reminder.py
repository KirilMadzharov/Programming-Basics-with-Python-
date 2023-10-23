"""
Write a program that prints all numbers in the range 1 to 100 that are
divisible by 3 without a remainder, one per line.
"""


for i in range(1, 100):
    if i % 3 == 0:
        print(i)
