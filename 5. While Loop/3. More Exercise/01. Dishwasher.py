"""
Gosho works in a restaurant and is responsible for loading the dishwasher at the end of the day.
Your task is to write a program that calculates whether a purchased amount of bottles of dishwashing
detergent is enough to wash a certain amount of dishes. Each bottle is known to contain 750 ml. detergent,
5 ml are needed for 1 plate, and 15 ml for a pot. Assume that every third load of dishes, the dishwasher
is filled only with pots and the other times with plates. Until you receive an "End" command, you will
continue to receive a number of dishes that need to be washed.
"""



detergent = int(input()) * 750

detergent_needed = 0
counter = 0
pot = 0
plate = 0

command = input()

while command != "End":
    dishes = int(command)
    if dishes == int(command):
        counter += 1

    if counter % 3 == 0:
        pot += dishes
        detergent_needed += dishes * 15

    else:
        plate += dishes
        detergent_needed += dishes * 5

    if detergent_needed > detergent:
        break

    command = input()

diff = abs(detergent - detergent_needed)

if detergent_needed <= detergent:
    print("Detergent was enough!")
    print(f"{plate} dishes and {pot} pots were washed.")
    print(f"Leftover detergent {diff} ml.")
else:
    print(f"Not enough detergent, {diff} ml. more necessary!")

