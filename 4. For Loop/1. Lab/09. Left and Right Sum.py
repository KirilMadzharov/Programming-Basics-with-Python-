"""
Write a program that reads 2 * n-th number of integers
supplied by the user and checks whether the sum of the first n numbers

(left sum) is equal to the sum of the second n numbers (right sum).

If there is a tie, print " Yes, sum = " + the sum;

otherwise it prints " No, diff = " + the difference.

The difference is calculated as a positive number (in absolute value).
"""


iterations = int(input())

left_sum = 0
right_sum = 0

for numbers in range(iterations * 2):
    current_num = int(input())
    if numbers < iterations:
        left_sum += current_num
    else:
        right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
