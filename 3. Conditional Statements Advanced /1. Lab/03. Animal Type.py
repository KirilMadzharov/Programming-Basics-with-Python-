"""
Write a program that prints the class of the animal according to its name entered by the user.
1. dog -> mammal
2. crocodile, tortoise, snake -> reptile
3. others -> unknown
"""

animal = input()

if animal == "dog":
    print("mammal")
elif animal in "crocodile" "tortoise" "snake":
    print("reptile")
else:
    print("unknown")
