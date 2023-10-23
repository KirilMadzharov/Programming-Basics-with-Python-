"""
Write a program that reads from the console a number r and calculates and prints the face and perimeter
of a circle / circle of radius r, formatting the output as follows: "<calculated area>"
"<calculated parameter>".

Format the output data to the second decimal place.
"""

from math import pi

r = float(input())

diameter = 2 * r * pi
area = pi * (r * r)

print(f"{area:.2f}")
print(f"{diameter:.2f}")
