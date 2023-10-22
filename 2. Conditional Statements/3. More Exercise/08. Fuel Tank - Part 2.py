"""
Write a program to calculate how much it will cost a driver to fill his car's tank,
given the type of fuel he fills, the price per liter of fuel, and whether he has a
discount card. Fuel prices are as follows:

• Gasoline – BGN 2.22 per liter,
• Diesel – BGN 2.33 per liter
• Gas – BGN 0.93 per liter

If the driver has a discount card, he benefits from the following reductions per
 liter of fuel: 18 cents per liter of petrol, 12 cents per liter of diesel
 and 8 cents per liter of gas.

If the driver has loaded between 20 and 25 liters inclusive, he receives
an 8 percent discount on the final price, for more than 25 liters of fuel,
 he receives a 10 percent discount on the final price.
"""

fuel_type = input()
quantity = float(input())
club_cart = input()

price = 0

if fuel_type == "Gasoline" and club_cart == "Yes":
    price = 2.22 - 0.18
elif fuel_type == "Gasoline" and club_cart == "No":
    price = 2.22
elif fuel_type == "Diesel" and club_cart == "Yes":
    price = 2.33 - 0.12
elif fuel_type == "Diesel" and club_cart == "No":
    price = 2.33
elif fuel_type == "Gas" and club_cart == "Yes":
    price = 0.93 - 0.08
elif fuel_type == "Gas" and club_cart == "No":
    price = 0.93

final_price = quantity * price

if 20 <= quantity <= 25:
    final_price -= final_price * 0.08
elif quantity > 25:
    final_price -= final_price * 0.10

print(f"{final_price:.2f} lv.")
