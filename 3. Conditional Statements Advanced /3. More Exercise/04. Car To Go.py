"""
Write a program to calculate the price, type and class of a rental car based on a given budget and season.

The seasons are summer and winter - "Summer" and "Winter".
The types of cars are convertible and jeep - "Cabrio" and "Jeep".

• With a budget less than or equal to BGN 100:

o The class will be - "Economy class"
o Depending on the season, the car and the price will be:
 Summer – Convertible – 35% of the budget
 Winter - Jeep - 65% of the budget

• With a budget greater than BGN 100. and less than or equal to BGN 500:
o The class will be - "Compact class"
o Depending on the season, the car and the price will be:
 Summer – Convertible – 45% of the budget
 Winter - Jeep - 80% of the budget

• With a budget greater than BGN 500:
o The class will be - "Luxury class"
o For each season, the car will be a jeep and the price will be:
 90% of the budget
"""


budget = float(input())
season = input()

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_model = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car_model = "Jeep"
        price = budget * 0.65

if 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_model = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car_model = "Jeep"
        price = budget * 0.80

elif budget > 500:
    car_class = "Luxury class"
    car_model = "Jeep"
    price = budget * 0.90

print(f"{car_class}")
print(f"{car_model} - {price:.2f}")

