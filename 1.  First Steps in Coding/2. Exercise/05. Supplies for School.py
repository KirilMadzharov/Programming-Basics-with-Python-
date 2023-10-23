"""
The school year has already started and the teacher of class 10B - Annie has to buy a certain number
of packets of chemicals, packets of markers, as well as blackboard cleaner.
She is a regular customer of a bookstore, so there is a discount for her, which is some percentage
of the total amount.

Write a program that calculates how much money Annie will need to collect to pay the bill,
given the following price list:

• Package of chemicals - BGN 5.80.
• Pack of markers - BGN 7.20.
• Detergent - BGN 1.20 (per liter)
"""

pen_package = int(input())
marker_package = int(input())
detergent = int(input())
discount = float(input())

supplies = (pen_package * 5.80) + (marker_package * 7.20) + (detergent * 1.20)
total = supplies - (supplies * discount / 100)

print(total)
