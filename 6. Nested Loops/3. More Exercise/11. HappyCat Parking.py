"""
Desi needs to take her cat to the vet at the Happy Cat Clinic,
but there is a parking fee.

 Write a program that calculates the total cost of parking Desi's car
 in the parking lot to take her cat to the vet.
 The parking lot is different from the others and has a varied price list.

 For every even day and odd hour, the parking lot charges BGN 2.50.
 On every odd day and even hour, the fee is BGN 1.25, in all other cases BGN 1 is charged.
 Billing is done every hour of the day. Each of the outputs must be rounded to the second decimal place.
"""


days = int(input())
hours = int(input())

price = 0
total = 0
for a in range(1, days + 1):
    for b in range(1, hours + 1):
        if a % 2 == 0 and b % 2 != 0:
            price += 2.5
        elif a % 2 != 0 and b % 2 == 0:
            price += 1.25
        else:
            price += 1
    print(f"Day: {a} - {price:.2f} leva")
    total += price
    price = 0
print(f"Total: {total:.2f} leva")
