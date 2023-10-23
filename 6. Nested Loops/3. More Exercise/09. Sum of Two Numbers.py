"""
Write a program that checks all possible combinations of a pair of
numbers in the interval of two given numbers.

The output is printed which order is the combination whose sum of
the numbers is equal to a given magic number.

If there is no combination matching the condition, a message
is printed saying that it was not found.
"""



start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
number_found = False

for a in range(start, end + 1):
    for b in range(start, end + 1):
        counter += 1
        if a + b == magic_number:
            number_found = True
            break
    if number_found:
        break
if number_found:
    print(f"Combination N:{counter} ({a} + {b} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")

