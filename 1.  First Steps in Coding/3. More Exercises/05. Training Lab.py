"""
A classroom has a rectangular dimension w by h meters, without columns in its interior.
The hall is divided into two parts - left and right, with a corridor approximately in the middle.
There are rows of desks on the left and on the right. At the rear of the hall is a large entrance door.

In the front part of the hall there is a chair with a podium for the teacher.
One workplace occupies 70 by 120 cm (table measuring 70 by 40 cm + space for a chair and passage measuring 70 by 80 cm).
The corridor is at least 100 cm wide. It is estimated that exactly 1 job is lost because of the front door
(which has a 160 cm opening) and because of the chair (which is 160 by 120 cm) exactly 2 jobs are lost.

Write a program that enters the dimensions of the classroom and calculates the number
of seats in it for the described layout
"""

w_meters = float(input())
h_meters = float(input())

w = w_meters * 100
h = h_meters * 100
row = w // 120
desk = (h - 100) // 70
total = (desk * row) - 3

print(int(total))
