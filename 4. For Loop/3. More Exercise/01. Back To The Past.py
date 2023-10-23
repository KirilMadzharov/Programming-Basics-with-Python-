"""
Ivancho is 18 years old and receives an inheritance that consists
 of X amount of money and a time machine.

 He decides to go back to the year 1800, but he doesn't know
 if the money will be enough to live without working.

 Write a program that calculates whether Ivancho will have enough
 money to not have to work up to and including a given year.

 Assuming that for each even year (1800, 1802, etc.) he will spend BGN 12,000.
 For each odd number (1801,1803, etc.) he will spend:

12,000 + 50 * [the years he reached in the given year].

"""


inheritance = float(input())
year_to_live = int(input())

money = 0

for years in range(1800, year_to_live + 1, 1):
    if years % 2 == 0:
        money += 12000
    else:
        money += 12000 + 50 * ((18 + years) - 1800)

diff = abs(inheritance - money)

if inheritance >= money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")

