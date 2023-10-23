"""
Ivan decides to improve the World Record in long distance swimming.

Enter the record in seconds that Ivan needs to beat, the distance in meters that he needs to swim,
and the time in seconds that he needs to swim 1 m on the console. Write a program that calculates whether
he has completed the task by it is meant that: water resistance slows it down every 15 m by 12.5 seconds.

When calculating how many times Ivancho will slow down due to water resistance, the result must be rounded
down to the nearest whole number.

Calculate the time in seconds for which Ivancho will swim the distance and the difference to the World Record.
"""

from math import floor

record = float(input())
distance = float(input())
time_meter = float(input())

time = (distance * time_meter) + ((floor(distance / 15)) * 12.5)
difference = time - record

if record > time:
    print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
