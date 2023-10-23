"""
Write a program that reads two integers (N1 and N2) and an operator to
perform a given mathematical operation.

Possible operations are:

Addition(+), Subtraction(-),
Multiplication(*), Division(/)
and Modular Division(%).

 Addition, subtraction and multiplication on the console should print the result
 and whether it is even or odd. In ordinary division - the result.

 In the case of modular division - the remainder. It should be noted that the divisor
 can be equal to 0 (zero), and is not divisible by zero. In this case, a special message must be printed.
"""


n1 = int(input())
n2 = int(input())
operator = input()

operation = 0
rest = 0

if operator == "+":
     operation = n1 + n2
     rest = operation % 2
     if rest != 0:
         print(f"{n1} {operator} {n2} = {operation} - odd")
     else:
         print(f"{n1} {operator} {n2} = {operation} - even")

elif operator == "-":
    operation = n1 - n2
    rest = operation % 2
    if rest != 0:
        print(f"{n1} {operator} {n2} = {operation} - odd")
    else:
        print(f"{n1} {operator} {n2} = {operation} - even")

elif operator == "*":
    operation = n1 * n2
    rest = operation % 2
    if rest != 0:
        print(f"{n1} {operator} {n2} = {operation} - odd")
    else:
        print(f"{n1} {operator} {n2} = {operation} - even")

elif operator == "/":
    if n2 != 0:
        operation = n1 / n2
        print(f"{n1} {operator} {n2} = {operation:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")

elif operator == "%":
    if n2 != 0:
        operation = n1 % n2
        print(f"{n1} {operator} {n2} = {operation}")
    else:
        print(f"Cannot divide {n1} by zero")
