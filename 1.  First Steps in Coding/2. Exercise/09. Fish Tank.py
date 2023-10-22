"""
For his birthday, Lubomir received an aquarium in the shape of a parallelepiped.
Initially, we read from the console in separate lines its dimensions
 - length, width and height in centimeters.

 It is necessary to calculate how many liters of water the aquarium will collect,
 if it is known that a certain percentage of its capacity is occupied by sand, plants,
 heater and pump.

One liter of water equals one cubic decimeter/ 1l=1 dm3/.

Write a program that calculates the liters of water needed to fill the aquarium.
"""

length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
percent = int(input())

litres = (length_cm * width_cm * height_cm) / 1000
occupied = percent / 100
needed_litres = litres * (1 - occupied)

print(needed_litres)
