"""
Write a program that reads a number n entered by the user
and prints all numbers ≤ n from the sequence: 1, 3, 7, 15, 31, ….

Each subsequent number is calculated by multiplying
the previous one by 2 and adding 1.
"""



number = int(input())

sum_num = 1

while sum_num <= number:
    print(sum_num)
    sum_num = sum_num * 2 + 1
