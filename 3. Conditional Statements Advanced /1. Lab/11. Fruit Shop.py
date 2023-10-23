"""
The fruit shop operates at the following prices on working days:

fruit banana apple orange grapefruit kiwi pineapple grapes
price 2.50 1.20 0.85 1.45 2.70 5.50 3.85

On Saturdays and Sundays, the store operates at higher prices:

fruit banana apple orange grapefruit kiwi pineapple grapes
price 2.70 1.25 0.90 1.60 3.00 5.60 4.20

Write a program that reads from the console the following three variables entered by
 the user and calculates the price according to the prices in the tables above:

• fruit - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
• day of the week - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
• quantity (real number).

Print the result rounded to 2 decimal places. For an invalid day of the week or an invalid fruit name, print "error".
"""

fruit = input()
day = input()
quantity = float(input())

price = 0

if day in "Monday" "Tuesday" "Wednesday" "Thursday" "Friday" \
        and fruit in "banana" "apple" "orange" "grapefruit" "kiwi" "pineapple" "grapes":
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85

    final_price = price * quantity
    print(f"{final_price:.2f}")

elif day in "Saturday" "Sunday" \
        and fruit in "banana" "apple" "orange" "grapefruit" "kiwi" "pineapple" "grapes":
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20

    final_price = price * quantity
    print(f"{final_price:.2f}")

else:
    print("error")
