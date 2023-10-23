"""
Write a program that reads an integer N and generates all possible "lucky" and different
4-digit numbers (each digit of the number is in the interval [1...9]).

The number must meet the following conditions:

A lucky number is a 4-digit number where the sum of the
 first two digits is equal to the sum of the last two.

The number N must be divisible without a remainder by
the sum of the first two digits of the "lucky" number.
"""


number = int(input())

if number < 10:
    check = number
else:
    check = 10

for a in range(1, check):
    for b in range(1, check):
        if number % (a + b) != 0:
            continue

        for c in range(1, check):
            for d in range(1, check):
                if a + b == c + d:
                    print(f"{a}{b}{c}{d}", end=" ")

