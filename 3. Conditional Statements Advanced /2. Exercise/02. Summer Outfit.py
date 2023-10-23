"""
Summer is a season with very changeable weather and Victor needs your help.
Write a program that, based on the time of day and the degrees, recommends
Victor what clothes to wear. Your friend has different plans for each stage
of the day, which also require a different appearance - you can see them from the table.

Exactly two lines are read from the console:
• Degrees - whole number;
• Time of day - text with three options "Morning", "Afternoon" or "Evening".

Time of day / degrees
Morning
Afternoon
Evening

10 <= degrees <= 18 Outfit = Sweatshirt
Shoes = Sneakers Outfit = Shirt
Shoes = Moccasins Outfit = Shirt
Shoes = Moccasins

18 < degrees <= 24 Outfit = Shirt
Shoes = Moccasins Outfit = T-Shirt
Shoes = Sandals Outfit = Shirt
Shoes = Moccasins

degrees >= 25 Outfit = T-Shirt
Shoes = Sandals Outfit = Swim Suit
Shoes = Barefoot Outfit = Shirt
Shoes = Moccasins

As output, print to the console one line: "It's {degrees} degrees, get your {clothes} and {shoes}."
"""

degrees = int(input())
time_of_day = input()

if 10 <= degrees <= 18 and time_of_day == "Morning":
    outfit = "Sweatshirt"
    shoes = "Sneakers"

elif 18 < degrees <= 24 and time_of_day == "Morning":
    outfit = "Shirt"
    shoes = "Moccasins"

elif degrees >= 25 and time_of_day == "Morning":
    outfit = "T-Shirt"
    shoes = "Sandals"

if 10 <= degrees <= 18 and time_of_day == "Afternoon":
    outfit = "Shirt"
    shoes = "Moccasins"

elif 18 < degrees <= 24 and time_of_day == "Afternoon":
    outfit = "T-Shirt"
    shoes = "Sandals"

elif degrees >= 25 and time_of_day == "Afternoon":
    outfit = "Swim Suit"
    shoes = "Barefoot"

if 10 <= degrees <= 18 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

elif 18 < degrees <= 24 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

elif degrees >= 25 and time_of_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
