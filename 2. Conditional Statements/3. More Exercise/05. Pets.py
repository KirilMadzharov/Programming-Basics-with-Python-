"""
Marina likes to travel. She has 3 pets (dog, cat and turtle).
When he goes on a trip, he has to consider how much food to leave for them
so that they don't go hungry.

Write a program that calculates how many kilograms of food everyone will
eat during the time Marina is away and whether the food left by her will be enough for them.
Each animal eats a certain amount of food per day.
"""

from math import floor, ceil

count_days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_gr = float(input())

needed_food = (count_days * dog_food_kg) + (count_days * cat_food_kg) + \
              ((count_days * turtle_food_gr) / 1000)
diff = abs(food_kg - needed_food)

if food_kg > needed_food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
