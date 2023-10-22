"""
Given an integer - initial number of points. Bonus points are accrued on it according to the rules described below.
To write a program that calculates the bonus points that the number receives and the total number
of points (the number + the bonus).

• If the number is up to and including 100, the bonus points are 5;
• If the number is greater than 100, the bonus points are 20% of the number;
• If the number is greater than 1000, the bonus points are 10% of the number.

• Additional bonus points (charged separately from the previous ones):
For an even number  + 1 pt.
For a number that ends in 5  + 2 pts.
"""

num = int(input())
bonus = 0

if num <= 100:
    bonus = 5
elif num > 1000:
    bonus = num * 0.1
else:
    bonus = num * 0.2

if num % 2 == 0:
    bonus += 1
elif num % 10 == 5:
    bonus += 2

total = num + bonus

print(bonus)
print(total)
