"""
An enterprising Bulgarian opens neighborhood shops in several cities and sells at different prices
depending on the city:

city / product coffee water beer sweets peanuts
Sofia 0.50 0.80 1.20 1.45 1.60
Plovdiv 0.40 0.70 1.15 1.30 1.50
Varna 0.45 0.70 1.10 1.35 1.55

Write a program that reads a product (text), a city (text), and a quantity (decimal number)
entered by the user, and calculates and prints how much the corresponding quantity of the
selected product costs in the specified city.
"""

product = input()
city = input()
quantity = float(input())

price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.50
    elif product == "water":
        price = 0.80
    elif product == "beer":
        price = 1.20
    elif product == "sweets":
        price = 1.45
    elif product == "peanuts":
        price = 1.60

if city == "Plovdiv":
    if product == "coffee":
        price = 0.40
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.15
    elif product == "sweets":
        price = 1.30
    elif product == "peanuts":
        price = 1.50

if city == "Varna":
    if product == "coffee":
        price = 0.45
    elif product == "water":
        price = 0.70
    elif product == "beer":
        price = 1.10
    elif product == "sweets":
        price = 1.35
    elif product == "peanuts":
        price = 1.55

final_price = price * quantity

print(final_price)
