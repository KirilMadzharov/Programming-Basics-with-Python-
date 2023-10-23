"""
Write a program that calculates how much you will receive at the end of the deposit period at a given interest rate.
Use the following formula:

amount = deposited amount + term of the deposit * ((deposited amount * annual interest rate ) / 12)

"""

deposit_sum = float(input())
deposit_time = int(input())
annual_interest_percent = float(input())

annual_interest = deposit_sum * annual_interest_percent / 100
monthly_interest = annual_interest / 12
sum = deposit_sum + deposit_time * monthly_interest

print(sum)
