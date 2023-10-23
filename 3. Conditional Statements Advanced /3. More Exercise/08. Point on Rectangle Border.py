"""
Write a program that checks whether a point {x, y} lies on any of the sides of a
rectangle {x1, y1} – {x2, y2}. The input data is read from the console and consists
 of 6 lines entered by the user: the decimal numbers x1, y1, x2, y2, x and y
 (ensuring that x1 < x2 and y1 < y2). To print "Border" (point lies on either side)
 or "Inside / Outside" (otherwise).
"""


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

condition_1 = (x == x1 or x == x2) and (y1 <= y <= y2)
condition_2 = (y == y1 or y == y2) and (x1 <= x <= x2)

if condition_1 or condition_2:
    print("Border")
else:
    print("Inside / Outside")

