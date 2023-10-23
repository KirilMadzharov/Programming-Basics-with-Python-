"""
A young programmer has a certain budget and free time in a given season.
 Write a program that accepts as input the budget and the season, and outputs
 where the programmer will rest and how much he will spend.

The budget determines the destination, and the season determines how much of
the budget will be spent. If it is summer, he will rest at a campsite, and in winter at a hotel.
If he is in Europe, regardless of the season, he will rest in a hotel. Each campsite or hotel,
according to the destination, has its own price, which corresponds to a certain percentage of the budget:

• At BGN 100 or less - somewhere in Bulgaria:
 Summer - 30% of the budget;
 Winter - 70% of the budget.
• At BGN 1000 or less - somewhere in the Balkans:
 Summer - 40% of the budget;
 Winter - 80% of the budget.
• For more than BGN 1,000 - somewhere in Europe:
 When traveling in Europe, regardless of the season, will spend 90% of the budget.
"""

budget = float(input())
season = input()

destination = "Bulgaria" or "Balkans" or "Europe"
accommodation_type = "Camp" or "Hotel"

price = 0
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        accommodation_type = "Camp"
    elif season == "winter":
        price = budget * 0.7
        accommodation_type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        accommodation_type = "Camp"
    elif season == "winter":
        price = budget * 0.8
        accommodation_type = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    accommodation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{accommodation_type} - {price:.2f}")
