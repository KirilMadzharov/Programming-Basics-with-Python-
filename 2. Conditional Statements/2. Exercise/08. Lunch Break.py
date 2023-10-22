"""
During your lunch break, you want to watch an episode of your favorite series.
Your task is to write a program that will tell if you have enough time to watch the episode.
During the break, you have time for lunch and time for relaxation.
Lunch time will be 1/8 of break time and recess time will be 1/4 of break time.
"""

from math import ceil

series_name = str(input())
duration = int(input())
lunch_break = int(input())

lunch = lunch_break / 8
chill = lunch_break / 4

total_time = duration + lunch + chill
free_time = abs(lunch_break - total_time)

if lunch_break >= total_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(free_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(free_time)} more minutes.")
