"""
There are a number of books on Joro's must-read list for summer vacation.
Since Joro prefers to play with friends outside, your task is to help him
calculate how many hours a day he should spend to read the necessary literature.
"""

pages_per_book = int(input())
pages_per_hour = int(input())
days_per_book = int(input())

hours_per_day = (pages_per_book // pages_per_hour) // days_per_book

print(hours_per_day)
