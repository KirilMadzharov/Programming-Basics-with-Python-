"""
Climbers from all over Bulgaria gather in groups and mark
the next peaks to climb.

Depending on the size of the group, climbers will climb different peaks.

• Group of up to 5 people - climb Musala
• Group of 6 to 12 people - climb Mont Blanc
• Group of 13 to 25 people - climb Kilimanjaro
• Group of 26 to 40 people - climb K2
• Group of 41 or more people - climb Everest

To write a program that calculates the percentage of climbers who climb each peak.
"""

group = int(input())

musala = 0
mount_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
people_count = 0

for i in range(group):
    climbers = int(input())
    people_count += climbers
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        mount_blanc += climbers
    elif climbers <= 25:
        kilimanjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    elif climbers >= 41:
        everest += climbers

g1 = (musala / people_count) * 100
g2 = (mount_blanc / people_count) * 100
g3 = (kilimanjaro / people_count) * 100
g4 = (k2 / people_count) * 100
g5 = (everest / people_count) * 100

print(f"{g1:.2f}%")
print(f"{g2:.2f}%")
print(f"{g3:.2f}%")
print(f"{g4:.2f}%")
print(f"{g5:.2f}%")

