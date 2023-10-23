"""
Write a program that calculates how many natural number solutions (including zero) the equation has:
x1 + x2 + x3 = n

The number n is an integer and is entered from the console.
"""

number = int(input())
combinations = 0

for n1 in range(number + 1):
    for n2 in range(number + 1):
        for n3 in range(number + 1):
            if n1 + n2 + n3 == number:
                combinations += 1

print(combinations)
