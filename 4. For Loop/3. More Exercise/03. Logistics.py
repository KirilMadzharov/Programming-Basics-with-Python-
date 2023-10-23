"""
You are responsible for the logistics of various cargoes.
Depending on the weight of the load, a different vehicle is required.

The price per ton for which the cargo is transported is different for each vehicle:

• Up to 3 tons - minibus (200 BGN per ton)
• From 4 to 11 tons - truck (175 BGN per ton)
• 12 tons and more - train (120 BGN per ton)

Your task is to calculate the average price per ton of transported cargo,
as well as the percentage of tons transported by each vehicle,
compared to the total weight (in tons) of all cargo.
"""


cargo = int(input())

bus = 0
truck = 0
train = 0
price = 0
quantity = 0

for i in range(cargo):
    tons = int(input())

    if tons <= 3:
        bus += tons
        price += tons * 200
        quantity += tons
    elif tons <= 11:
        truck += tons
        price += tons * 175
        quantity += tons
    elif tons >= 12:
        train += tons
        price += tons * 120
        quantity += tons

average_price = price / quantity
bus_average = (bus / quantity) * 100
truck_average = (truck / quantity) * 100
train_average = (train / quantity) * 100

print(f"{average_price:.2f}")
print(f"{bus_average:.2f}%")
print(f"{truck_average:.2f}%")
print(f"{train_average:.2f}%")

