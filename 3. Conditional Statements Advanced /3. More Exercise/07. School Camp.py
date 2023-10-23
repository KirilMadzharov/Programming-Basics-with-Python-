"""
A private school organizes camps for students during vacations.
Depending on the type of vacation (spring, summer or winter) and the type of group
(boys/girls or mixed), the price of the night at the hotel is different, as well as
the sport that the students will practice.

Winter break Spring break Summer break
boys/girls 9.60 7.20 15
mixed group 10 9.50 20

The school receives a discount from the final price, depending on the number
of students accommodated in the hotel:

• If the number of students is 50 or more, the school receives a 50% discount
• If the number of students is 20 or more and at the same time less than 50, the school receives a 15% discount
• If the number of students is 10 or more and at the same time less than 20, the school receives a 5% discount

The table below shows the sports that will be practiced depending on the type of vacation and the group:
Winter break Spring break Summer break
girls Gymnastics Athletics Volleyball
boys Judo Tennis Football
mixed group Ski Cycling Swimming

Write a program that calculates the price that the school will pay for overnight stays
and prints the sport that will be practiced by the students.
"""


season_type = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

if season_type == "Winter":
    if group_type == "girls":
        price = 9.60
        sport = "Gymnastics"
    elif group_type == "boys":
        price = 9.60
        sport = "Judo"
    elif group_type == "mixed":
        price = 10
        sport = "Ski"

if season_type == "Spring":
    if group_type == "girls":
        price = 7.20
        sport = "Athletics"
    elif group_type == "boys":
        price = 7.20
        sport = "Tennis"
    elif group_type == "mixed":
        price = 9.50
        sport = "Cycling"

if season_type == "Summer":
    if group_type == "girls":
        price = 15
        sport = "Volleyball"
    elif group_type == "boys":
        price = 15
        sport = "Football"
    elif group_type == "mixed":
        price = 20
        sport = "Swimming"

total = students_count * nights_count * price

if students_count >= 50:
    total *= 0.50
elif 20 <= students_count < 50:
    total *= 0.85
elif 10 <= students_count < 20:
    total *= 0.95

print(f"{sport} {total:.2f} lv.")
