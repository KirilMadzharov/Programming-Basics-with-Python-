"""
A bicycle race for charity is coming up, in which the participants are divided into juniors and seniors.
 The money is raised from the cyclists' participation fee.

 According to the age group and the type of track on which the race will be held, the fee is different.

Trail cross-country downhill road group

juniors 5.50 8 12.25 20
seniors 7 9.50 13.75 21.50

If 50 or more participants gather in the "cross-country" competition (junior and senior in total),
the fee is reduced by 25%. The organizers set aside 5% of the collected amount for expenses.
"""


juniors = int(input())
seniors = int(input())
trail_type = input()

if trail_type == "trail":
    tax = juniors * 5.50 + seniors * 7

elif trail_type == "cross-country":
    tax = juniors * 8 + seniors * 9.50
    if juniors + seniors >= 50:
        tax *= 0.75

elif trail_type == "downhill":
    tax = juniors * 12.25 + seniors * 13.75

elif trail_type == "road":
    tax = juniors * 20 + seniors * 21.50

final_sum = tax * 0.95

print(f"{final_sum:.2f}")
