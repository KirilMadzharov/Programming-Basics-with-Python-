"""
Write a program that reads a single number n, then reads n number
of integers and prints the arithmetic mean of their sum, formatted
to the second digit after the decimal point.
"""



n = int(input())

sum_num = 0

for i in range(n):
    number = int(input())
    sum_num += number
average = sum_num / n

print(f"{average:.2f}")

