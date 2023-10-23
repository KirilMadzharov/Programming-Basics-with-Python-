"""
Write a program that, given the degrees (a real number) entered, prints what the weather is, given the following table:

Degrees Weather
26.00 - 35.00 Hot
20.1 - 25.9 Warm
15.00 - 20.00 Mild
12.00 - 14.9 Cool
5.00 - 11.9 Cold

If degrees other than those listed in the table are entered, print "unknown".
"""

degrees = float(input())

if 26.00 <= degrees <= 35.00:
    print("Hot")
elif 20.10 <= degrees <= 25.9:
    print("Warm")
elif 15 <= degrees <= 20:
    print("Mild")
elif 12 <= degrees <= 14.9:
    print("Cool")
elif 5 <= degrees <= 11.9:
    print("Cold")
else:
    print("unknown")
