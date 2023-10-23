"""
Write a program that reads an integer n
entered by the user and prints a pyramid of numbers.

Example:

input:

10

Output:

1
2 3
4 5 6
7 8 9 10
"""


n = int(input())

current_number = 1
is_current_number_bigger_than_n = False

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if current_number > n:
            is_current_number_bigger_than_n = True
            break

        print(str(current_number) + ' ', end='')
        current_number += 1

    if is_current_number_bigger_than_n:
        break
    print()


