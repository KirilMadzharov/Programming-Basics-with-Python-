"""
Bozhidara has several houses on the Black Sea and wants to landscape the yards
 of some of them, thus creating a cozy atmosphere and comfort for his guests.

For this purpose, she hired a company.

Write a program that calculates the necessary amount that Bozhidara will have to pay
to the company executing the project.

The price per square meter is BGN 7.61 including VAT.
Because her yard is quite large, the contractor offers an 18% discount off the final price.
"""


yards = float(input())
price = yards * 7.61
discount = price * 0.18

print(f"The final price is: {price - discount} lv.")
print(f"The discount is: {discount} lv.")
