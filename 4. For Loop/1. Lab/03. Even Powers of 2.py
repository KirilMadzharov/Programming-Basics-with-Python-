"""
Write a program that reads a number n entered by the user
and prints the even powers of 2 ≤ 2n: 20, 22, 24, 26, …, 2n.
"""

n = int(input())

for i in range(0, n + 1, 2):  # iterate with a step of 2 for even numbers
    print(2**i)  # 2^0 = 1
