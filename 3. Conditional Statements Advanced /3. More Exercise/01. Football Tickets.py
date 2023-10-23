"""
When tickets were released for Euro 2016, a group of fans decided to buy them.
Tickets have two categories with different prices:

• IP – BGN 499.99.
• Normal – BGN 249.99.

The fans have a certain budget, and the number of people in the group determines
 what percentage of the budget should be set aside for transport From 1 to 4 - 75% of the budget.

• From 5 to 9 – 60% of the budget.
• From 10 to 24 – 50% of the budget.
• From 25 to 49 – 40% of the budget.
• 50 or more – 25% of the budget.

Write a program that calculates whether they can buy tickets for the selected category with the
remaining money from the budget. And how much money will they have left or need.
"""

budget = float(input())
category = input()
people = int(input())

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25

if category == "VIP":
    ticket = 499.99
elif category == "Normal":
    ticket = 249.99

expences = transport + ticket * people
difference = abs(budget - expences)

if budget >= expences:
    print(f"Yes! You have {difference:.2f} leva left.")
elif budget < expences:
    print(f"Not enough money! You need {difference:.2f} leva.")

