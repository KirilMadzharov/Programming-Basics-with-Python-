"""
Write a program that checks if the number entered by the user is in the interval
[-100, 100] and is different from 0 and outputs "Yes" if it meets the conditions
or "No" if it does not.
"""

number_in_range = int(input())

if -100 <= number_in_range <= 100 and number_in_range != 0:
    print("Yes")
else:
    print("No")
