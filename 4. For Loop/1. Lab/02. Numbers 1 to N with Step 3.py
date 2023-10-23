"""
Write a program that reads a number n
entered by the user and prints the numbers 1 through n through 3.
"""

n = int(input())

for i in range(1, n + 1, 3):
    print(i)
