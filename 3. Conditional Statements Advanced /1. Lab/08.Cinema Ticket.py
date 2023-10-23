"""
Write a program that reads the day of the week (text) - entered by the user
and prints on the console the price of a movie ticket according to the day of the week:

Monday Tuesday Wednesday Thursday Friday Saturday Sunday
12 12 14 14 12 16 16
"""

day_of_week = input()
price = 0

if day_of_week in "Monday" "Tuesday" "Friday":
    price = 12
elif day_of_week in "Wednesday" "Thursday":
    price = 14
elif day_of_week in "Saturday" "Sunday":
    price = 16

print(price)
