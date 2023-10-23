"""
Write a program that reads a product name entered by the user and checks whether it is a fruit or a vegetable.

• "fruit" has the following possible values: banana, apple, kiwi, cherry, lemon and grapes;
• Vegetables have the following possible values: tomato, cucumber, pepper and carrot;
• All others are "unknown".

Display "fruit", "vegetable" or "unknown" according to the product entered.
"""

fruit_or_vegetable = input()

if fruit_or_vegetable in "banana" "apple" "kiwi" "cherry" "lemon" "grapes":
    print("fruit")
elif fruit_or_vegetable in "tomato" "cucumber" "pepper" "carrot":
    print("vegetable")
else:
    print("unknown")
