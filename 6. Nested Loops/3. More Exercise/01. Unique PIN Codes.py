"""
Write a program that generates three-digit PIN codes, the digits
of each PIN code being in a certain interval. For a PIN code to be valid,
it must meet the following conditions:

• The first and third digits must be even.
• The second digit must be a prime number in the range [2...7].
"""


n1 = int(input())
n2 = int(input())
n3 = int(input())

for a in range(1, n1 + 1):
    if a % 2 != 0:
        continue
    for b in range(1, n2 + 1):
        if b not in (2, 3, 5, 7):
            continue
        for c in range(1, n3 + 1):
            if c % 2 == 0:
                print(f"{a} {b} {c}")
