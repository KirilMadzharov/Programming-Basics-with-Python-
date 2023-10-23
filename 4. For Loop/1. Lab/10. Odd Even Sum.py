"""
Write a program that reads n-th number of integers
supplied by the user and checks whether the sum of the numbers
in even positions is equal to the sum of the numbers in odd positions.

• If the sums are equal, print two lines: "Yes" and on a new line "Sum = " + the sum;
• If the amounts are not equal, print two lines: "No" and on a new line "Diff = " + the difference.

The difference is calculated in absolute value.
"""



n = int(input())

odd_sum = 0
even_sum = 0

for position in range(1, n + 1):
    current_num = int(input())
    if position % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f"Yes")
    print(f"Sum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No")
    print(f"Diff = {diff}")
