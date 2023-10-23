"""
Write a program to multiply positive numbers by 2.

A series of real numbers are read from the console, each on a new line,
until a negative is entered. After each multiplied number on a new line print

"Result: {the result of the multiplication}".

The result of the multiplication should be formatted to the second digit
 after the decimal separator.

 If a negative number is received, the console should print
 "Negative number!" and the program to finish execution.
"""


number = float(input())

while number >= 0:
    num = number * 2
    print(f"Result: {num:.2f}")

    number = float(input())
else:
    print("Negative number!")
