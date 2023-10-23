"""
Atanas decides to spend his vacation in Bansko and go skiing. Before he goes,
 however, he needs to book a hotel and calculate how much the stay will cost him.

 The following types of rooms are available, with the following prices for a stay:
    "room for one person" – BGN 18.00 per night
    "apartment" – BGN 25.00 per night
    "president apartment" – BGN 35.00 per night

According to the number of days he will stay in the hotel (example: 11 days = 10 nights)
 and the type of room he will choose, he can enjoy a different discount.

The reductions are as follows:
    type of premises less than 10 days between 10 and 15 days more than 15 days
    room for one person does not use a discount does not use a discount does not use a discount
    apartment 30% of the final price 35% of the final price 50% of the final price
    president apartment 10% of the final price 15% of the final price 20% of the final price

After the stay, Atanas' assessment of the hotel's services may be positive or negative.
If his assessment is positive, Atanas adds 25% of it to the price with the discount already deducted.
If his assessment is negative, 10% will be deducted from the price.
"""


days_stay = int(input())
room_type = input()
review = input()

nights = days_stay - 1
price = 0
total_price = 0

if room_type == "room for one person":
    price = 18

if room_type == "apartment" and nights < 10:
    price = 25 * 0.70
elif room_type == "apartment" and 10 >= nights <= 15:
    price = 25 * 0.50
elif room_type == "apartment" and nights > 15:
    price = 25 * 0.50

if room_type == "president apartment" and nights < 10:
    price = 35 * 0.90
elif room_type == "president apartment" and 10 >= nights <= 15:
    price = 35 * 0.85
elif room_type == "president apartment" and nights > 15:
    price = 35 * 0.80

if review == "positive":
    price *= 1.25
elif review == "negative":
    price *= 0.90

final_price = nights * price

print(f"{final_price:.2f}")

