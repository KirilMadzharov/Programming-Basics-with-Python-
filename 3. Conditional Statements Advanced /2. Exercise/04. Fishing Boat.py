"""
Tony and friends love to go fishing and are so passionate about
 fishing that they decide to go fishing by boat. The price for
 renting the vessel depends on the season and the number of fishermen:

Depending on the season:
• The price for renting the ship in the spring is BGN 3,000;
• The price for renting the ship in summer and autumn is BGN 4,200;
• The price for renting the ship in winter is BGN 2,600.

Depending on the number of the group, there is a different discount:
• If the group is up to 6 people inclusive - 10% discount;
• If the group is from 7 to 11 people inclusive - 15% discount;
• If the group is 12 or more - 25% discount.

Fishermen enjoy an additional 5% discount if they are an even number,
unless it is autumn - then they do not have an additional discount,
which is charged after deducting the discount according to the above criteria.

Write a program to calculate whether the fishermen will collect enough money.
"""

budget = int(input())
season = input()
fisherman = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if fisherman <= 6:
    price *= 0.9
elif 7 <= fisherman <= 11:
    price *= 0.85
elif fisherman >= 12:
    price *= 0.75

if fisherman % 2 == 0 and season != "Autumn":
    price *= 0.95

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
