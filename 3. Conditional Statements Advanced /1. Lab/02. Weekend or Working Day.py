"""
Write a program that reads the day of the week (text), in English - entered by the user.
If the day is working, it prints on the console - "Working day", if it is a holiday - "Weekend".
If a text other than a day of the week is entered, "Error" will be printed.
"""

day_of_week = input()

if day_of_week in "Monday" "Tuesday" "Wednesday" "Thursday" "Friday":
    print("Working day")
elif day_of_week in "Saturday" "Sunday":
    print("Weekend")
else:
    print("Error")
