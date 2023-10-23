"""
Petya has a children's toy shop. She gets a big order to fulfill.
With the money he will earn, he wants to go on an excursion.

Toy prices:
• Puzzle - BGN 2.60.
• Talking doll - BGN 3
• Teddy bear - BGN 4.10.
• Mignon - BGN 8.20.
• Truck - BGN 2

If the ordered toys are 50 or more, the store makes a discount of 25% of the total price.
From the money earned, Petya must give 10% for the rent of the shop. To calculate whether
 the money will be enough for her to go on an excursion.
"""

trip = float(input())
puzzle = int(input())
talking_doll = int(input())
teddy_bear = int(input())
minion = int(input())
truck = int(input())
discount = 0

total_price = puzzle * 2.60 + talking_doll * 3 + teddy_bear * 4.10 + minion * 8.20 + truck * 2
total_toys = puzzle + talking_doll + teddy_bear + minion + truck

if total_toys >= 50:
    total_price *= 0.75

rent = total_price * 0.10
profit = total_price - rent

expenses = abs(profit - trip)

if profit >= trip:
    print(f"Yes! {expenses:.2f} lv left.")
else:
    print(f"Not enough money! {expenses:.2f} lv needed.")
