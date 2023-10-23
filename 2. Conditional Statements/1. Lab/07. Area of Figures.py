"""
To write a program in which the user enters the type and dimensions of a geometric figure and calculates its face.
There are four types of figures: square, rectangle, circle and triangle.
The first line of the input reads the type of figure
(text with the following options: square, rectangle, circle or triangle).

• If the figure is a square: a fractional number is read on the next line - the length of its side
• If the figure is a rectangle: on the next two lines read two fractional numbers - the lengths of its sides
• If the figure is a circle: on the next line read a fractional number - the radius of the circle
• If the figure is a triangle: on the next two lines read two fractional numbers -
the length of its side and the length of the height to it

Round the result to 3 decimal places.
"""

from math import pi
area_of_figures = str(input())

if area_of_figures == "square":
    side_a = float(input())
    area = side_a * side_a
    print(f"{area:.3f}")

elif area_of_figures == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a + side_b) * 2
    print(f"{area:.3f}")

elif area_of_figures == "circle":
    side_a = float(input())
    area = side_a * side_a * pi
    print(f"{area:.3f}")

elif area_of_figures == "triangle":
    side_a = float(input())
    side_b = float(input())
    area = (side_a * side_b) / 2
    print(f"{area:.3f}")

