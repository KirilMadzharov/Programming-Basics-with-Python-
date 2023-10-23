"""
The SoftUni team is organizing a football tournament.

First we read from the console the capacity of the stadium
and the number of all fans. Then, for each fan, the sector
in which it is located is read.

The first team's fans are in sectors A and B, and the second team's
fans are in C and D.

Write a program that calculates the percentages of fans in each sector,
relative to the total number of fans in the stadium, as well as the total
percentage of fans for both teams. according to the capacity of the stadium.

The total number of fans does NOT exceed the capacity of the stadium.
"""


stadium_capacity = int(input())
fans = int(input())

A = 0
B = 0
V = 0
G = 0

for i in range(fans):
    sector = input()

    if sector == "A":
        A += 1
    elif sector == "B":
        B += 1
    elif sector == "V":
        V += 1
    elif sector == "G":
        G += 1

avg_A = (A / fans) * 100
avg_B = (B / fans) * 100
avg_V = (V / fans) * 100
avg_G = (G / fans) * 100
avg_stadium = (fans / stadium_capacity) * 100

print(f"{avg_A:.2f}%")
print(f"{avg_B:.2f}%")
print(f"{avg_V:.2f}%")
print(f"{avg_G:.2f}%")
print(f"{avg_stadium:.2f}%")

