"""
Write a console program that reads the age (real number) and gender
('m' or 'f') entered by the user and prints an address from among the following:
• "Mr." – male (gender 'm') aged 16 or over
• "Master" – boy (gender 'm') under 16 years old
• "Ms." – female (gender 'f') aged 16 or over
• "Miss" – girl (gender 'f') under 16 years old
"""

age = float(input())
gender = input()

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")

if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
