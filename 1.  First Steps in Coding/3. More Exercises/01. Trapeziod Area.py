"""
Write a program that reads from the console three fractional numbers b1, b2 and h and calculates
the face of a trapezoid with bases b1 and b2 and height h.
The formula for the face of a trapezoid is (b1 + b2) * h / 2.
The figure below shows a trapezoid with sides 8 and 13 and height 7. It has a face of (8 + 13) * 7 / 2 = 73.5.
The answer must be formatted to the second digit after the decimal point.
"""

b1 = float(input())
b2 = float(input())
h = float(input())

trapezoid_area = (b1 + b2) * h / 2
# result = "{:.2f}".format(trapezoid_area)
print(f"{trapezoid_area:.2f}")
