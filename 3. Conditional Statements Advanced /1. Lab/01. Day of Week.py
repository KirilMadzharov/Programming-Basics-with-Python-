"""
Write a program that reads an integer entered by the user and prints the day of the week,
in the range [1...7], or prints "Error" in case the entered number is invalid.
"""

number_of_day = int(input())

if number_of_day == 1:
    print("Monday")
elif number_of_day == 2:
    print("Tuesday")
elif number_of_day == 3:
    print("Wednesday")
elif number_of_day == 4:
    print("Thursday")
elif number_of_day == 5:
    print("Friday")
elif number_of_day == 6:
    print("Saturday")
elif number_of_day == 7:
    print("Sunday")
else:
    print("Error")
