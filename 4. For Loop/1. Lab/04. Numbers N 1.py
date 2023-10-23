"""
Write a program that reads a positive integer n entered by the user
and prints the numbers n through 1 in reverse order.

The number n entered will always be greater than 1.
"""

n = int(input())

for i in range(n, 0, -1):
    print(i)
