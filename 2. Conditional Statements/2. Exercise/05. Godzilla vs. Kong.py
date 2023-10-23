"""
Filming for the highly anticipated Godzilla vs. Kong movie begins.
Screenwriter Adam Wingard asks you to write a program to calculate whether the
budgeted funds are sufficient to make the film. The shoot will require a certain number of extras,
clothing for each extra, and decor.

It is known that:
• The set for the film is worth 10% of the budget.
• For more than 150 extras, there is a 10% clothing discount.
"""

budget = float(input())
extras = int(input())
costume = float(input())

costume_price = extras * costume
decor = budget * 0.1

if extras > 150:
    costume_price *= 0.9

diff = abs(budget - (decor + costume_price))

if decor + costume_price > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
