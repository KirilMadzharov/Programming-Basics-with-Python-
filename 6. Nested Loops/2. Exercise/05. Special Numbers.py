"""
Write a program that reads an integer N entered by the user
and generates all possible "special" numbers from 1111 to 9999.

 For a number to be "special", it must satisfy the following condition:
• N to be divided by each of its digits without a remainder.

Example: for N = 16, 2418 is a special number:
• 16 / 2 = 8 with no remainder
• 16 / 4 = 4 with no remainder
• 16 / 1 = 16 with no remainder
• 16 / 8 = 2 with no remainder
"""


number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                is_valid = number % i == 0 and number % j == 0 and number % k == 0 and number % l == 0
                if is_valid:
                    print(f"{i}{j}{k}{l}", end=" ")

