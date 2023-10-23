"""
Write a program that reads n-th number of integers entered by the user and checks
if there is a number among them that is equal to the sum of all the others.

• If there is such an element, print "Yes" and on a new line "Sum = " + its value
• If there is no such element, print "No" and on a new line "Diff = " + the difference
between the largest element and the sum of the others (by absolute value)
"""


import sys

iterations = int(input())

max_num = -sys.maxsize
sum_numbers = 0

for number in range(iterations):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

sum_numbers -= max_num
diff = abs(max_num - sum_numbers)

if sum_numbers == max_num:
    print(f"Yes")
    print(f"Sum = {sum_numbers}")
else:
    print(f"No")
    print(f"Diff = {diff}")
