"""
Write a program that reads n-th number of integers
entered by the user and sums them.

• The number of numbers n is entered from the first line of the input.
• One whole number is entered from the next n lines.

The program must read the numbers, add them, and print the sum.
"""


count_of_numbers = int(input())
sum_of_numbers = 0

for i in range(count_of_numbers):
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)

