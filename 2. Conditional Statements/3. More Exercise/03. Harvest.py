"""
From a vineyard with an area of X square meters, 40% of the harvest is set aside for wine production.
Y kilograms of grapes are obtained from 1 square meter of vineyard. 2.5 kg is needed for 1 liter of wine.
grapes. The desired quantity of wine to be sold is Z liters.
Write a program that calculates how much wine can be produced and whether this amount is sufficient.
If there is enough, the remainder is divided equally among the vineyard workers.
"""

from math import floor, ceil

x_vineyards = int(input())
y_grapes = float(input())
z_liters_wine = int(input())
workers = int(input())

wine = ((x_vineyards * y_grapes) / 2.5 ) * 0.4
diff = abs(wine - z_liters_wine)
liters_per_person = diff / workers

if wine >= z_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(liters_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
