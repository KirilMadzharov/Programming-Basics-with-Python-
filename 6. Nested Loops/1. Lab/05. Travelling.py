"""
Annie loves to travel and wants to visit several different
destinations this year.

Once she's chosen a destination, she'll estimate how much
money she'll need to get there and start saving.
When she has saved enough, she will be able to travel.

The console will first read the destination and the minimum
 budget (decimal number) that will be needed for the trip.

It will then read several amounts (decimal numbers) that Annie
saves by working, and when she has saved enough for the trip,
she will leave, and the console should read:

"Going to {destination}!"

When she has visited all the destinations she wants,
she will enter "End" instead of a destination and
the program will end.
"""



destination = input()

while destination != "End":
    needed_money = float(input())
    collected_money = 0

    while collected_money < needed_money:
        current_money = float(input())
        collected_money += current_money

    print(f"Going to {destination}!")

    destination = input()

