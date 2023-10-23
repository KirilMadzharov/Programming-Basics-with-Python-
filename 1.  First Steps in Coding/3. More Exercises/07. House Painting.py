"""
Write a program to calculate how many liters of paint are needed to paint a house.
Green paint is used for the walls and red for the roof. The consumption of green paint is 1 liter
for 3.4 m2, and for red - 1 liter for 4.3 m2.

The walls have the following dimensions:
• The front and back walls are squares with side "x"
on the front wall there is a rectangular door with a width of 1.2m and a height of 2m
• Sidewalls are rectangles with sides 'x' and 'y'
on both side walls there is one square window with a side of 1.5 m

The roof has the following dimensions:
• Two rectangles with sides "x" and "y"
• Two equilateral triangles with side "x" and height "h"

You need to calculate the area of all the sides and the area of the roof to
find how many liters of each paint will be needed.
"""

x = float(input())
y = float(input())
h = float(input())

x_walls = (x * x) * 2 - (1.2 * 2)
y_walls = (x * y) * 2 - (1.5 * 1.5) * 2
roof = (x * y) * 2 + ((x * h) / 2) * 2
green_paint = (x_walls + y_walls) / 3.4
red_paint = roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
