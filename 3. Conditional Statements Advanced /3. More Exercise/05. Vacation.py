"""
Write a program that, given a given budget and season, calculates the price,
location, and accommodation for a vacation. The seasons are summer and winter
- "Summer" and "Winter". The locations are - "Alaska" and "Morocco".
Possible places of accommodation – "Hotel", "Hut" or "Camp".

• With a budget less than or equal to BGN 1,000:
o Accommodation in "Camp"
o Depending on the season, the location will be one of the following and will
cost a certain percentage of the budget:

 Summer - Alaska - 65% of the budget
 Winter - Morocco - 45% of the budget
• With a budget greater than BGN 1,000. and less than or equal to BGN 3000:
o Accommodation in "Hut"
o Depending on the season, the location will be one of the following and will
 cost a certain percentage of the budget:

 Summer - Alaska - 80% of the budget
 Winter - Morocco - 60% of the budget
• With a budget greater than BGN 3,000:

o Accommodation in "Hotel"
o Depending on the season, the location will be one of the following and will
 cost 90% of the budget:

 Summer – Alaska
 Winter – Morocco
"""


budget = float(input())
season = input()

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.60

elif budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {place} - {price:.2f}")

