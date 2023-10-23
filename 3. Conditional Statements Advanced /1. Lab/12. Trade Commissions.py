"""
A company gives the following commissions to its salespeople according to the city
in which they work and the volume of sales:

City 0 ≤ s ≤ 500 500 < s ≤ 1,000 1,000 < s ≤ 10,000 s > 10,000
Sofia 5% 7% 8% 12%
Varna 4.5% 7.5% 10% 13%
Plovdiv 5.5% 8% 12% 14.5%

Write a console program that reads city name (text) and sales volume (real number)
entered by the user and calculates and outputs the trade commission amount according
to the above table. Output the result formatted to 2 decimal places. Invalid city or
sales volume (negative number) to print "error".
"""

city = input()
sales = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
    elif 500 < sales <= 1000:
        commission = sales * 0.07
    elif 1000 < sales <= 10000:
        commission = sales * 0.08
    elif sales > 10000:
        commission = sales * 0.12

elif city == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
    elif 500 < sales <= 1000:
        commission = sales * 0.075
    elif 1000 < sales <= 10000:
        commission = sales * 0.10
    elif sales > 10000:
        commission = sales * 0.13

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
    elif 500 < sales <= 1000:
        commission = sales * 0.08
    elif 1000 < sales <= 10000:
        commission = sales * 0.12
    elif sales > 10000:
        commission = sales * 0.145

if city in "Sofia Varna Plovdiv" and sales > 0:
    print(f"{commission:.2f}")

else:
    print("error")

