"""
There is a secret door in the city that everyone knows about, but no one
has been able to unlock it and see what is behind it. A three-digit code
must be entered to unlock it.

Write a program that generates combinations based on entered numbers - guesses by the user.
 Three digits are entered from the console. These digits will be the upper bound up
 to which we want to get all three-digit numbers where every single digit satisfies
 the following conditions:

• The units digit and the hundreds digit must be even
• The tens digit should be a simple number in the range (2...7).

These will be the possible combinations according to the assumptions entered by the user,
with which it will be possible to eventually unlock the door.
"""



hundreds = int(input())
tens = int(input())
singles = int(input())

for a in range(1, hundreds + 1):
    if a % 2 == 0:
        for b in range(1, tens + 1):
            if b in [2, 3, 5, 7]:
                for c in range(1, singles + 1):
                    if c % 2 == 0:
                        print(f"{a} {b} {c}")