"""
Write a program to calculate the average monthly expenditure of a family for
a given period of time.

For each month, the costs are as follows:

• For electricity – every month is different, it will be read from the console
• for water – BGN 20
• for internet – BGN 15.
• for others - electricity, water and internet for the month are collected and 20% is added to the amount.

For each expense, you need to calculate how much was paid in total for all months.
"""


months = int(input())

electricity_bills = 0
water_bills = months * 20
internet_bills = months * 15
other_bills = 0

for i in range(months):
    electricity = float(input())
    electricity_bills += electricity
    other_bills += (electricity + 20 + 15) * 1.2

average = (electricity_bills + water_bills + internet_bills + other_bills) / months

print(f"Electricity: {electricity_bills:.2f} lv")
print(f"Water: {water_bills:.2f} lv")
print(f"Internet: {internet_bills:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {average:.2f} lv")

