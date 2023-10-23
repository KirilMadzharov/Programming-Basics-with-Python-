"""
Lily is now N years old. For every birthday she gets a present.
• For odd birthdays (1, 3, 5...n) he gets toys.
• For even birthdays (2, 4, 6...n) he receives money.

For the second birthday, he receives BGN 10.00, and the amount increases
by BGN 10.00 for each subsequent even birthday (2 -> 10, 4 -> 20, 6 -> 30...etc.).

 Over the years, Lily has secretly saved the money. Lily's brother, in the years
 that she receives money, takes BGN 1.00 from them. Lily sold the toys received
 over the years, each for P leva and added the amount to the money saved.

 With the money, she wanted to buy a washing machine for BGN X. Write a program
 to calculate how much money she has collected and whether she has enough to buy a washing machine.
"""


lily_age = int(input())
washing_machine = float(input())
one_toy_price = int(input())

birthday = 0
brother_money = 0
counter = 0
toys = 0

for age in range(lily_age):
    counter += 1
    if counter % 2 == 0:
        birthday += (counter / 2) * 10
        brother_money += 1
    else:
        toys += 1

money_for_toys = one_toy_price * toys
total_money = birthday - brother_money
diff = abs((money_for_toys + total_money) - washing_machine)

if money_for_toys + total_money >= washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

