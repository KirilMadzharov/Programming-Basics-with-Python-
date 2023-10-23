"""
Write a program that reads degrees Celsius (°C) and converts them to degrees Fahrenheit (°F).
Search the Internet for a suitable formula to do the calculations.
Format the output to the second decimal place.
"""

celsius = float(input())

fahrenheit = celsius * 1.8 + 32

print(f"{fahrenheit:.2f}")
