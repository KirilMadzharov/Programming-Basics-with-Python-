"""
Write a program that reads nth number of numbers entered by the user and calculates
 the sum, minimum, and maximum of the numbers in even and odd positions (count of 1).

When there is no minimum / maximum element, print "No".

The output should be formatted as follows:

"OddSum=" + {sum of numbers in odd positions},
"OddMin=" + { minimum value of numbers in odd positions } / {“No”},
"OddMax=" + { maximum value of numbers in odd positions } / {“No”},
"EvenSum=" + { sum of numbers in even positions },
"EvenMin=" + { minimum value of numbers in even positions } / {“No”},
"EvenMax=" + { maximum value of numbers in even positions } / {“No”}

Each number must be formatted to the second decimal place.
"""


import sys

n = int(input())
odd_sum = 0
even_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())

    if i % 2 == 0:
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
        even_sum += number

    else:
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number
        odd_sum += number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f},")
print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f},")
print(f"EvenMax={even_max:.2f},")
