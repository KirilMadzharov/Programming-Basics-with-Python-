"""
Given n integers in the interval [1…1000]. Of these, some percentage p1 are below 200,
another percentage p2 are from 200 to 399, another percentage p3 are from 400 to 599,
another percentage p4 are from 600 to 799 and the remaining p5 percentage are from 800 and above.

Write a program that calculates and prints the percentages p1, p2, p3, p4 and p5.
Example: we have n = 20 numbers: 53, 7, 56, 180, 450, 920, 12, 7, 150, 250, 680, 2,
600, 200, 800, 799, 199, 46, 128, 65.

We get the following distribution and visualization:

Range Numbers in range Number of numbers Percent
< 200 53, 7, 56, 180, 12, 7, 150, 2, 199, 46, 128, 65 12 p1 = 12 / 20 * 100 = 60.00%
200 … 399 250, 200 2 p2 = 2 / 20 * 100 = 10.00%
400 … 599 450 1 p3 = 1 / 20 * 100 = 5.00%
600 … 799 680, 600, 799 3 p4 = 3 / 20 * 100 = 15.00%
≥ 800 920, 800 2 p5 = 2 / 20 * 100 = 10.00%
"""


n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(n):
    num = int(input())

    if num < 200:
        p1 += 1
    elif 200 <= num <= 399:
        p2 += 1
    elif 400 <= num <= 599:
        p3 += 1
    elif 600 <= num <= 799:
        p4 += 1
    elif num >= 800:
        p5 += 1

p1_percent = (p1 / n) * 100
p2_percent = (p2 / n) * 100
p3_percent = (p3 / n) * 100
p4_percent = (p4 / n) * 100
p5_percent = (p5 / n) * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")

