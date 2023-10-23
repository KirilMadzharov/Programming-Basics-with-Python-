"""
Marin and Nellie buy a house not far from Sofia.
Nellie loves flowers so much that she convinces you to write a program
to calculate how much it will cost them to plant a certain number of flowers
 and whether the available budget will be enough for them. Different flowers have different prices:

flower Rose Dahlia Tulip Narcissus Gladiola

Price per piece in BGN 5 3.80 2.80 3 2.50

The following discounts are available:
• If Nellie buys more than 80 Roses - 10% discount from the final price;
• If Nellie buys more than 90 Dahlias - 15% discount from the final price;
• If Nellie buys more than 80 Tulips - 15% discount from the final price;
• If Nellie buys less than 120 Narcissus - the price increases by 15%;
• If Nellie Buys less than 80 Gladioli - the price increases by 20%.

3 lines are read from the console:
• Flower type - text with options "Roses", "Dahlias", "Tulips", "Narcissus" or "Gladiolus";
• Number of flowers - integer;
• Budget - integer.

To print to the console on one line:
• If their budget is sufficient - "Hey, you have a great garden with {number of flowers} {type of flowers}
 and {remaining amount} leva left.";
• If their budget is NOT enough - "Not enough money, you need {necessary amount} leva more.".

Amount to be formatted to the second decimal place.
"""

type_of_flowers = input()
flowers_count = int(input())
budget = int(input())

price = 0

if type_of_flowers == "Roses":
    price = 5
elif type_of_flowers == "Dahlias":
    price = 3.8
elif type_of_flowers == "Tulips":
    price = 2.8
elif type_of_flowers == "Narcissus":
    price = 3
elif type_of_flowers == "Gladiolus":
    price = 2.5

if type_of_flowers == "Roses" and flowers_count > 80:
    price *= 0.9
elif type_of_flowers == "Dahlias" and flowers_count > 90:
    price *= 0.85
elif type_of_flowers == "Tulips" and flowers_count > 80:
    price *= 0.85
elif type_of_flowers == "Narcissus" and flowers_count < 120:
    price *= 1.15
elif type_of_flowers == "Gladiolus" and flowers_count < 80:
    price *= 1.2

final_price = price * flowers_count
diff = abs(budget - final_price)

if budget >= final_price:
    print(f"Hey, you have a great garden with {flowers_count} {type_of_flowers} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
