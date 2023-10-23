"""
Maria wants to buy her son a present. She works in a flower shop.
An order for flowers comes into the shop. Write a program that calculates
the amount of the order and whether the profit is enough for the gift.

Flowers have the following prices:

• Magnolias – BGN 3.25
• Hyacinths – 4 BGN
• Roses – BGN 3.50
• Cacti – 8 BGN

From the total amount, Maria has to pay 5% taxes.
"""

from math import floor, ceil

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cactus = int(input())
gift_price = float(input())

income = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cactus * 8
total = income - (income * 0.05)
diff = abs(total - gift_price)

if total >= gift_price:
    print(f"She is left with {floor(diff)} leva.")
else:
    print(f"She will have to borrow {ceil(diff)} leva.")
