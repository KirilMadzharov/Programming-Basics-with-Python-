"""
Hotel offers 2 types of rooms: studio and apartment.
 Write a program that calculates the total stay price for a studio and an apartment.

Prices depend on the month of stay:

May and October June and September July and August
Studio - BGN 50/night Studio - BGN 75.20/night Studio - BGN 76/night
Apartment - BGN 65/night Apartment - BGN 68.70/night Apartment - BGN 77/night

The following discounts are also available:
• For studio, for more than 7 nights in May and October: 5% discount.
• For studio, for more than 14 nights in May and October: 30% discount.
• For studio, for more than 14 nights in June and September: 20% discount.
• For an apartment, for more than 14 nights, regardless of the month: 10% discount.
"""


month = input()
nights_count = int(input())

studio = 0
apartment = 0

if month in "May" "October":
    studio = 50
    apartment = 65
    if 7 < nights_count <= 14:
        studio *= 0.95
    elif nights_count > 14:
        studio *= 0.70
        apartment *= 0.90

if month in "June" "September":
    studio = 75.2
    apartment = 68.7
    if nights_count > 14:
        studio *= 0.80
        apartment *= 0.90

if month in "July" "August":
    studio = 76
    apartment = 77
    if nights_count > 14:
        apartment *= 0.90

studio_price = studio * nights_count
apartment_price = apartment * nights_count

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")
