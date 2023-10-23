"""
Annie is afraid that one of her social network accounts will be hacked,
so she decides to make a password generator that will be secure enough.

Your task is to help her write a program that will generate these passwords
 separated from each other by the "|" character.

To write a program that generates a series of characters as in the pattern:
ABxyBA

as each time a new code is generated, the character values are incremented by 1.
If A exceeds 55, it returns to 35. If B exceeds 96, it returns to 64.
"""




a = int(input())
b = int(input())
max_passwords = int(input())

counter = 0
A = ord("#")
B = ord("@")

for x in range(1, a + 1):
    if counter >= max_passwords or counter == (a * b):
        break
    for y in range(1, b + 1):
        print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
        A += 1
        B += 1
        if A > ord("7"):
            A = ord("#")
        if B > ord("`"):
            B = ord("@")
        counter += 1
        if counter >= max_passwords or counter == (a * b):
            break