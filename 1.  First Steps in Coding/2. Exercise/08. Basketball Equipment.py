"""
Jesse decides he wants to play basketball, but he needs equipment to practice.
Write a program that calculates what costs Jesse will incur if he starts coaching,
knowing the cost of basketball coaching over a 1-year period.

 Required equipment:

• Basketball shoes - their price is 40% less than the fee for one year
• Basketball team - its price is 20% cheaper than sneakers
• Basketball – its price is 1/4 of the price of the basketball team
• Basketball accessories – their price is 1 / 5 of the price of the basketball
"""

sum_for_year = int(input())

sneakers = sum_for_year - (sum_for_year * 0.4)
clothes = sneakers - (sneakers * 0.2)
ball_price = clothes - (clothes * 0.75)
accessories = ball_price - (ball_price * 0.80)

total = sum_for_year + sneakers + clothes + ball_price + accessories

print(total)
