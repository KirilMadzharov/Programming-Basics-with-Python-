"""
Write a program that reads from the console the side and height
of a triangle and calculates its face. Use the triangle face formula:

area = a * h / 2.

Format the output to the second decimal place.
"""

a = float(input())
h = float(input())

triangle_area = a * h / 2

print(f"{triangle_area:.2f}")

