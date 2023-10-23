"""
Write a program that reads two integers n and l entered by the user
and generates in alphabetical order all possible passwords that consist
 of the following 5 characters:

• Character 1: digit from 1 to n.
• Character 2: digit from 1 to n.

• Symbol 3: a small letter from among the first l letters of the Latin alphabet.
• Symbol 4: a small letter from among the first l letters of the Latin alphabet.
• Character 5: a digit from 1 to n, greater than the first 2 digits.
"""


n = int(input())
l = int(input())

for a in range(1, n):
    for b in range(1, n):
        for c in range(ord("a"), ord("a") + l):
            for d in range(ord("a"), ord("a") + l):
                for e in range(max(a, b) + 1, n + 1):
                    print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")

