"""
Rumen wants to repaint the living room and has hired craftsmen for this purpose.
Write a program that calculates the cost of the repair given the following prices:

• Protective nylon - BGN 1.50 per square meter
• Paint - BGN 14.50 per liter
• Paint thinner - BGN 5.00 per liter

Just in case, to the necessary materials, Rumen wants to add another 10% of the amount
of paint and 2 sq.m. nylon, of course, and BGN 0.40 for bags. The amount paid to craftsmen for 1 hour
of work is equal to 30% of the sum of all material costs.
"""

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours = int(input())

supplies = ((nylon_needed + 2) * 1.50 + (paint_needed + (paint_needed * 0.10)) * 14.50 + (thinner_needed * 5.00)) + 0.40
workers = (supplies * 0.3) * hours

print(supplies + workers)
