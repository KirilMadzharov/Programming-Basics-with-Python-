"""
Write a program that reads an integer from the console
and on each successive line integers until their sum is
 greater than or equal to the original number.

After reading is complete, print the sum of the entered  numbers.
"""


number = int(input())

sum_num = 0

while sum_num < number:
    sum_text = int(input())
    sum_num += sum_text

print(sum_num)
