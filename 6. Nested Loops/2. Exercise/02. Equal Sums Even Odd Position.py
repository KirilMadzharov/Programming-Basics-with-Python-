"""
Write a program that reads two six-digit integers from the console.
Always the first number entered will be less than the second.
On the console to print on 1, a line separated by a space, all the numbers
that are between the two numbers read by the console and meet the condition
that the sum of the digits in even and odd positions is equal.
If there are no numbers matching the condition on the console,
no result is displayed.
"""

num1 = int(input())
num2 = int(input())

for current_num in range(num1, num2 + 1):
    current_num_str = str(current_num)
    even_num = 0
    odd_num = 0

    for symbol in range(0, len(current_num_str)):
        digit = int(current_num_str[symbol])

        if symbol % 2 == 0:
            even_num += digit
        else:
            odd_num += digit

    if even_num == odd_num:
        print(current_num_str, end=" ")
