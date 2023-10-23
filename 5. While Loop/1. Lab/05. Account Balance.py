"""
Write a program that calculates how much total money is in
the account after you make a certain number of deposits.

 On each line you will receive the amount you need to deposit
 into the account until you receive a "NoMoreMoney" command.

 For each amount received, the console should display
 "Increase: " + the amount and add it to the account.

 If you get a number less than 0 the console should display

 "Invalid operation!" and the program to end.

When the program ends, it should print

"Total: " + the total amount in the account

formatted to the second decimal place.
"""


money = input()
current_sum = 0

while money != "NoMoreMoney":
    if float(money) < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {float(money):.2f}")
    current_sum += float(money)
    money = input()

print(f"Total: {current_sum:.2f}")
