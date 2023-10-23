"""
Write a program that reads an angle in radians (a decimal number)
and converts it to degrees.
Use the formula: degree = radian * 180 / π.
You can access the number π in Python through the math module.
To use its functionality, you must first turn on the consta pi.
"""

from math import pi

radians = float(input())
degrees = radians * 180 / pi

print(degrees)
