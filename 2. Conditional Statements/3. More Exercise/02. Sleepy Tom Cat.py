"""
Tom the cat likes to sleep all day, unfortunately his owner plays with him whenever he has free time.
To get a good night's sleep, Tom's gaming norm is 30,000 minutes a year. Tom's play time depends
 on his owner's days off:
• When he is at work, his owner plays with him for 63 minutes a day.
• When he is resting, his owner plays with him for 127 minutes a day.

Write a program that inputs the number of days off and prints whether Tom can get a good night's
sleep and the difference from the norm for the current year, assuming that the year has 365 days.

Example: 20 days off -> working days are 345 (365 – 20 = 345).
Actual playing time is 24,275 minutes (345 * 63 + 20 *127).
The difference from the norm is 5,725 minutes (30,000 – 24,275 = 5,725) or 95 hours and 25 minutes.
"""

day_off = int(input())

playtime = ((365 - day_off) * 63) + (day_off * 127)
diff = abs(30000 - playtime)
hours = diff // 60
minutes = diff % 60

if playtime > 30000:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
