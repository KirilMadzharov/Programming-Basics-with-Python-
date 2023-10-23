"""
Write a program that reads integers from the console until a "stop" command is received.
To find the sum of all prime numbers entered and the sum of all non-prime numbers entered.
Since, by mathematical definition, negative numbers cannot be prime, if a negative number
is given as input, the following message "Number is negative." should be output.

In this case, an entered number is ignored and not added to either sum, and the program
continues its execution, waiting for the next number to be entered.

On the output, print the two sums found on two lines in the following format:
• "Sum of all prime numbers is: {prime numbers sum}"
• "Sum of all non prime numbers is: {nonprime numbers sum}"
"""


sum_prime = 0
sum_non_prime = 0
stop_command = False

while not stop_command:
    command = input()
    if command == "stop":
        stop_command = True
        break

    command = int(command)
    if command < 0:
        print("Number is negative.")
        continue

    is_prime = True
    for number in range(2, command):
        if command % number == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += command
    else:
        sum_non_prime += command

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
