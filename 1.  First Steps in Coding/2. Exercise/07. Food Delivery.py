"""
A restaurant opens its doors and offers several menus at preferential prices:

• Chicken menu – BGN 10.35.
• Fish menu – BGN 12.40.
• Vegetarian menu – BGN 8.15.

Write a program that calculates how much it will cost a group of people to order takeout.
The group will also order a dessert, the price of which is equal to 20% of the total bill (excluding delivery).
The delivery price is BGN 2.50 and is charged at the end.
"""

chicken = int(input())
fish = int(input())
veggie = int(input())

total = (chicken * 10.35) + (fish * 12.40) + (veggie * 8.15)
delivery = (total * 0.2) + 2.50

print(total + delivery)
