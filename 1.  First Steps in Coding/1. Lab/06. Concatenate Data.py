"""
Write a program that reads first name, last name, age, and city
from the console and prints the following message:
"You are <firstName> <lastName>, a <age>-years old person from <town>."
"""

first_name = input()
last_name = input()
age = int(input())
town = input()

print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")
