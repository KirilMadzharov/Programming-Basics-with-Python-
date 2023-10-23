"""
In a movie theater, the chairs are arranged in a rectangular shape in r rows and c columns.

 There are three types of screenings with tickets at different prices:

• Premiere - premiere screening, at a price of BGN 12.00;
• Normal - standard projection, at a price of BGN 7.50;
• Discount - screening for children, schoolchildren and students at a reduced price of BGN 5.00.

Write a program that reads the projection type (text), number of rows and number of columns in the hall
(integers) entered by the user and calculates the total ticket revenue for a full house.

Print the result in 2 decimal places format.
"""

type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if type == "Premiere":
    income = cinema_capacity * 12.00
elif type == "Normal":
    income = cinema_capacity * 7.50
elif type == "Discount":
    income = cinema_capacity * 5.00

print(f"{income:.2f} leva")
