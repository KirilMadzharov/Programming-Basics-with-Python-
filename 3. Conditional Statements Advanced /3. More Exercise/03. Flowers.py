"""
A flower shop offers 3 types of flowers: chrysanthemums, roses and tulips. Prices depend on the season.

Season Chrysanthemums Roses Tulips

Spring / Summer BGN 2.00/pc. BGN 4.10/pc. BGN 2.50/pc.
Autumn / Winter BGN 3.75/pc. BGN 4.50/pc. BGN 4.15/pc.

On holidays, the prices of all flowers increase by 15%. The following discounts are available:

• For purchases of more than 7 tulips in the spring - 5% of the price of the entire bouquet.
• For purchases of 10 or more roses in winter - 10% of the price of the entire bouquet.
• For purchases of more than 20 flowers in total in all seasons - 20% of the price of the entire bouquet.

Discounts are made in the order so written and can be stacked! All discounts apply after the holiday price increase!
The price for arranging the bouquet is always BGN 2.

Write a program that calculates the price of a bouquet.
"""


chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

if season in "Spring" "Summer":
    price_c = 2.00
    price_r = 4.10
    price_t = 2.50

elif season in "Autumn" "Winter":
    price_c = 3.75
    price_r = 4.50
    price_t = 4.15

if holiday == "Y":
    price_c *= 1.15
    price_r *= 1.15
    price_t *= 1.15

bouquet = chrysanthemums * price_c + roses * price_r + tulips * price_t

if season == "Spring" and tulips > 7:
    bouquet *= 0.95

if season == "Winter" and roses >= 10:
    bouquet *= 0.90

if chrysanthemums + roses + tulips > 20:
    bouquet *= 0.80

final_price = bouquet + 2

print(f"{final_price:.2f}")

