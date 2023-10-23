"""
Write a program that calculates how much money a truck driver will make in one season.
At the entrance, the program receives in which season the driver will work, as well as
how many kilometers per month he will drive. One season is 4 months. Depending on the
season and the number of kilometers per month, he will be paid a different amount per kilometer:

Spring/Autumn Summer Winter
km per month <= 5000 BGN 0.75/km BGN 0.90/km BGN 1.05/km
5000 < km per month <= 10000 BGN 0.95/km BGN 1.10/km BGN 1.25/km
10000 < km per month <= 20000 BGN 1.45/km - for any season

After 10% is deducted for taxes, the remaining money is printed.
"""


season = input()
km_for_month = float(input())

if km_for_month <= 5000:
    if season in "Spring" "Autumn":
        price = (km_for_month * 0.75) * 4
    elif season == "Summer":
        price = (km_for_month * 0.90) * 4
    elif season == "Winter":
        price = (km_for_month * 1.05) * 4

if 5000 < km_for_month <= 10000:
    if season in "Spring" "Autumn":
        price = (km_for_month * 0.95) * 4
    elif season == "Summer":
        price = (km_for_month * 1.10) * 4
    elif season == "Winter":
        price = (km_for_month * 1.25) * 4

if 10000 < km_for_month <= 20000:
    if season in "Spring" "Autumn" "Summer" "Winter":
        price = (km_for_month * 1.45) * 4

salary = price * 0.90

print(f"{salary:.2f}")

