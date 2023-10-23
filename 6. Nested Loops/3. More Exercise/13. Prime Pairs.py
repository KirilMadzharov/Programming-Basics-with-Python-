"""
Write a program that generates and prints to the console four-digit numbers in
which the first and second pairs of digits form two-digit prime numbers
(an example of such a number is 1723).

The final value to which the pairs should be generated is determined by another
2 digits passed as input, which determine how much the final value is greater than the starting value.
"""


start_first_pair = int(input())
start_second_pair = int(input())
difference_first_pair = int(input())
difference_second_pair = int(input())

for a in range(start_first_pair, start_first_pair + difference_first_pair + 1):
    for b in range(start_second_pair, start_second_pair + difference_second_pair + 1):

        i_is_prime = True
        j_is_prime = True

        for c in range(2, a):
            if a % c == 0:
                i_is_prime = False
                break

        for d in range(2, b):
            if b % d == 0:
                j_is_prime = False
                break
        if i_is_prime and j_is_prime:
            print(f"{a}{b}")

