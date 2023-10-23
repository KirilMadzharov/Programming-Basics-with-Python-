"""
Write a program that displays the room numbers in a building
(in descending order) on the console if the following conditions are met:

• There are only offices on each even floor;
• There are only apartments on each odd floor;
• Each apartment is designated as follows: A{floor number}{apartment number}, apartment numbers start from 0;
• Each office is designated as follows: O{floor number}{office number}, office numbers also start from 0;
• There are always apartments on the top floor and they are bigger than the others,
that's why they have an 'L' in front of the number instead of an 'A'. If there is only one floor,
then there are only large apartments!

Two integers are read from the console - the number of floors and the number of rooms per floor.
"""



floors = int(input())
rooms = int(input())

for current_floor in range(floors, 0, -1):
    for current_room in range(rooms):
        if current_floor == floors:
            print(f"L{current_floor}{current_room}", end = " ")
        elif current_floor % 2 == 0:
            print(f"O{current_floor}{current_room}", end = " ")
        else: #elif current_room % 2 != 0:
            print(f"A{current_floor}{current_room}", end = " ")
    print()
