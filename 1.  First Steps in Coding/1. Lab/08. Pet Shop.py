"""
Write a program that calculates the costs needed to buy dog and cat food.
The food is bought from a pet store, as one pack of dog food costs BGN 2.50,
and a pack of cat food costs BGN 4.
"""

dog_food = float(input())
cat_food = float(input())
dog_food_price = 2.50
cat_food_price = 4.00

result = (dog_food * dog_food_price) + (cat_food * cat_food_price)

print(f"{result} lv.")
